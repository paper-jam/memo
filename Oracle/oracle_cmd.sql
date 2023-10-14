-- ========== historique version
  - 2009 : version 11g
  - 2013 : version 12c
  - 2018 : version 18
  - 2019 : version 19c


-- ==========


-- ======================= DATA DICTIONNARY
    DBA_    : accessible to poweruser , object in all schema
    ALL_    : objects accessible in all schema by the current user
    USER_   : objects OWNED by the current user
    SELECT table_name from dict; -- all available metada

    -- autre possibilité : les views qui commencent par V$

    SELECT * FROM v$instance; -- notamment version oracle
    SELECT * FROM v$lock;
    SELECT * FROM v$controlfile;
    SELECT * FROM v$logfile;   -- redo files
    SELECT * FROM v$parameter;
    SELECT username, program, machine FROM v$session; -- utilisateurs connectés
    SELECT name, dbid, log_mode, flashback_on, open_mode, created from v$database; -- caractéristiques de la base de données


    SELECT * FROM all_tables;
    SELECT * FROM all_users;
    SELECT * FROM dba_data_files;
    SELECT * FROM dba_tablespaces;
    SELECT * FROM user_tables;
    SELECT * FROM user_tab_columns;
    SELECT * FROM user_ind_columns;

-- ======================= UTILISATEURS
    -- defaut tablespaces par utilisateur
    SELECT username, account_status, default_tablespace FROM dba_users;
    CREATE USER francis IDENTIFIED BY pass DEFAULT TABLESPACE tbs_perm_01 TEMPORARY TABLESPACE tbs_temp_01 QUOTA 20M on tbs_perm_01;
    GRANT CREATE SESSION TO francis;
    GRANT UNLIMITED tablespace, create table to francis;
    DROP USER francis;
    ALTER USER smithj IDENTIFIED BY autumn; -- change password


    -- un privilege est un droit d'utiliser un ordre SQL


    -- Role
    CREATE ROLE connect_and_create;
    GRANT create table to connect_and_create;
    GRANT create session to connect_and_create;
    GRANT connect_and_create to francis;
    GRANT all ON suppliers TO test_role;
    REVOKE privileges ON object FROM role_name;
    GRANT SELECT ON suppliers TO public;
    REVOKE DELETE ON suppliers FROM anderson;
    GRANT EXECUTE ON object TO user;
    REVOKE EXECUTE ON Find_Value FROM public;
    DROP ROLE role_name;

-- ================= SYNONYMES : facilite l'accès aux objets
    CREATE PUBLIC SYNONYM suppliers FOR app.suppliers;
    DROP PUBLIC SYNONYM suppliers;

-- ================= VIEWS
    CREATE OR REPLACE VIEW emp_sales AS SELECT * FROM employees WHERE job_id = 'SA_MAN';
    DROP VIEW emp_sales;


-- ================= TABLE SPACE (PERMANENT, UNDO, TEMPORARY.)
    -- les TableSpace peuvent être réparties sur plusieurs datafiles
    CREATE TABLESPACE tbs_perm_01 DATAFILE 'tbs_perm_01.dat'  SIZE 20M  ONLINE;
    CREATE TEMPORARY TABLESPACE tbs_temp_01 TEMPFILE 'tbs_temp_01.dbf' SIZE 5M AUTOEXTEND ON;
    DROP TABLESPACE ... including contents and datfiles;


-- ================= TABLE
    CREATE TABLE supplier (supplier_id numeric(10) not null, supplier_name varchar2(50) not null, ... CONSTRAINT supplier_pk PRIMARY KEY (supplier_id));
    CREATE TABLE suppliers (  id_client(4), nom  (varchar(4)... CHECK (supplier_id BETWEEN 100 and 9999);


    ALTER TABLE supplier    ADD COLUMN nomColonne KEY (supplier_id);
    ALTER TABLE supplier    ADD CONSTRAINT supplier_pk PRIMARY KEY (supplier_id);
    ALTER TABLE table_name  DROP CONSTRAINT constraint_name;
    ALTER TABLE table_name  DISABLE CONSTRAINT constraint_name;
    ALTER TABLE table_name  ENABLE CONSTRAINT constraint_name;

    -- FK
    CREATE TABLE products ( product_id numeric(10) not null,... CONSTRAINT fk_supplier FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id));
    ALTER TABLE table_name ADD CONSTRAINT constraint_name FOREIGN KEY (column1, column2, ... column_n)  REFERENCES parent_table (column1, ...);
    ALTER TABLE table_name DROP CONSTRAINT constraint_name;
    ALTER TABLE table_name DISABLE CONSTRAINT constraint_name;

    -- unique
    CREATE TABLE table_name ( column1 datatype [ NULL | NOT NULL ], ..  CONSTRAINT constraint_name UNIQUE (uc_col1, uc_col2, ... uc_col_n)

    -- changer le type d'un champ
    ALTER TABLE [ schema. ]table MODIFY { ( column [ datatype ] ) } ;

    -- contraintes sur une table
    SELECT * FROM user_constraints WHERE table_name='CONTACTS';

-- ====================== CONSTRAINTS
    -- primary key
    ALTER TABLE table_name ADD CONSTRAINT constraint_name PRIMARY KEY (column1, column2, ...);
    -- foreign key
    ALTER TABLE child_table ADD CONSTRAINT fk_name FOREIGN KEY (col1,col2) REFERENCES parent_table(col1,col2);
    -- NOT NULL
    ALTER TABLE surcharges MODIFY (amount NOT NULL);
    -- UNIQUE
    ALTER TABLE table_name ADD CONSTRAINT unique_constraint_name UNIQUE(column_name1, column_nam2);
    -- CHECK
    ALTER TABLE parts ADD CONSTRAINT check_positive_cost CHECK (cost > 0);

-- ===================== TEMPORARY TABLE
    -- a global temporary table is a permanent database object that store data on disk and visible to all sessions.
    -- but the data stored in the global temporary table is private to the session
    CREATE GLOBAL TEMPORARY TABLE temp1( id INT, description VARCHAR2(100) ) ON COMMIT DELETE / PRESERVE ROWS;

    -- All private temporary tables have a prefix defaults to to ORA$PTT_. / storage in memory only
    -- impossibilit de créer des index
    CREATE PRIVATE TEMPORARY TABLE ora$ppt_temp2(id INT, description VARCHAR2(100) ) ON COMMIT DROP/PRESERVE DEFINITION;

-- ====================== TABLE PARTITIONING
    - partitionnement horizontal, for performance reason
    - Plusieurs types de partitionnement:
        LIST, RANGE, HASH, INTERVAL, COMPOSITE, AUTOMATIC LIST

    - LIST : selon un critère (région, state, conuntry, salary)
    - RANGE : ranges of value : date de vente / janvier, février,...
    - HASH : for data with no natural ranges (ex : n° de facture)

    ------------ LIST
    CREATE TABLE sales_list
        (
        salesrep_id  NUMBER(5),
            salesrep_name VARCHAR2(40),
            sales_state   VARCHAR2(30),
            sales_value  NUMBER(10),
            sales_date    DATE)
        PARTITION BY LIST(sales_state)
        (
        PARTITION sales_CA VALUES('CA'),
        PARTITION sales_NY VALUES ('NY'),
        PARTITION sales_central VALUES('TX', 'IL'),
        PARTITION sales_other VALUES(DEFAULT)
        );

    ALTER TABLE sales_list
    SPLIT PARTITION sales_other VALUES ('NV')
    INTO
    (PARTITION sales_nv,
    PARTITION sales_other);

    ---------- RANGE
    CREATE TABLE sales_range
        (
        salesrep_id  NUMBER(5),
        salesrep_name VARCHAR2(30),
        sales_amount  NUMBER(10),
        sales_date    DATE)
        PARTITION BY RANGE(sales_date)
        (
        PARTITION sales_jan2017 VALUES LESS THAN(TO_DATE('01/02/2017','DD/MM/YYYY')),
        PARTITION sales_feb2017 VALUES LESS THAN(TO_DATE('01/03/2017','DD/MM/YYYY')),
        PARTITION sales_mar2017 VALUES LESS THAN(TO_DATE('01/04/2017','DD/MM/YYYY')),
        PARTITION sales_apr2017 VALUES LESS THAN(TO_DATE('01/05/2017','DD/MM/YYYY'))
        );

    -----------  HASH
    CREATE TABLE sales_hash
        (
        salesrep_id  NUMBER(5),
        salesrep_name VARCHAR2(30),
        sales_amount  NUMBER(10),
        sale_no       NUMBER(5))
        PARTITION BY HASH(sale_no)
        PARTITIONS 4 ;


-- ====================== XML
    CREATE TABLE EMP_XML (XML_ID NUMBER,XML_DATA XMLTYPE);
    CREATE TABLE EMPLOYEE (EMP_ID VARCHAR2(30),EMP_NAME VARCHAR2(70),EMP_SALARY NUMBER,EMP_DEPT VARCHAR2(20),EMP_JOB_ID VARCHAr2(50));
    INSERT INTO EMP_XML VALUES(500000,'<?xml version="1.0" encoding="UTF-8"?>
        <DETAILS>
          <EMP_ID>105</EMP_ID>
          <EMP_NAME>Raja</EMP_NAME>
          <EMP_SALARY>25000</EMP_SALARY>
          <EMP_DEPT>500</EMP_DEPT>
          <EMP_JOB_ID>CSE01</EMP_JOB_ID>
        </DETAILS>');
    INSERT INTO Employee (Emp_Id,Emp_Name,Emp_Salary,Emp_Dept,Emp_Job_Id)
    Select Emp.*
               FROM EMP_XML x,
                    XMLTABLE (
                       '/DETAILS'
                       Passing X.Xml_Data
                       COLUMNS "EMP_ID"  VARCHAR2 (30 BYTE)
                                  Path 'EMP_ID',
                               "EMP_NAME"  VARCHAR2 (70 BYTE)
                                  Path 'EMP_NAME',
                               "EMP_SALARY"  NUMBER (5, 0)
                                  Path 'EMP_SALARY',
                               "EMP_DEPT"  VARCHAR2 (20 BYTE)
                                  Path 'EMP_DEPT',
                               "EMP_JOB_ID"  Varchar2 (50 Byte)
                                  PATH 'EMP_JOB_ID') Emp;

-- ====================== SQL LOADER
    --
    -- UTL_HTTP -> appel d'API REST directement depuis Oracle

-- ====================== LES TYPES DE DONNEES
    VARCHAR2(taille BYTE | CHAR)    -- contient des caractères du character set ou des octets
    NVARCHAR2(taille)               -- ne contient que des caractères, N -> UNICODE
    CHAR(taille)                    -- chaîne de longueur fixe, complétée par des espaces
    NCHAR(taille)                   -- chaîne de longueur fixe, complétée par des espaces, N -> UNICODE
    NUMBER [(taille[,precision])]   --
    LONG                            -- -> 2Go à éviter
    DATE                            -- A M J H M S
    ROWID                           -- identifiant de ligne
    XMLType                         -- Colonne contenant des données au format XML
    UriType                         -- Colonne contenant une URL

-- ========== EXPLAIN PLAN
    -- https://www.youtube.com/watch?v=Xpmi55rn4YE
    -- permet de voir l'arborescence des opérations
    -- permet de voir si les index sont bien mis en jeu.
    explain plan for select * from customers;
    SELECT * from table(dbms_xplan.display);

    SELECT * from /*+ GATHER_PLAN_STATISTICS */customers;
    SELECT * from table(dbms_xplan.display_cursor(sql_id=>'17vzqf4anm6gm', format=>'ALLSTATS LAST +cost +bytes'));
    SELECT * from table(dbms_xplan.display_cursor(sql_id=>'17vzqf4anm6gm', format=>'ALLSTATS LAST +cost +bytes +outline'));
    -- outline -> la ligne 'LEADING' indique l'ordre dans le quel se font les jointures
    -- liste des plans
    SELECT * FROM PLAN_TABLE;

-- =======================  BOUCLE, CONDITION

    LOOP
        monthly_value := daily_value * 31;
        EXIT WHEN monthly_value > 4000;
    END LOOP;

    CURSOR FOR LOOP
    WHILE

    LOOP
    REPEAT UNTIL LOOP
    EXIT Statement

    IF-THEN-ELSE Statement
    CASE Statement
    GOTO Statement

-- ========= DECLARING VARIABLE
    -- le premier caractère est obligatoirement une lettre
    variable_name [CONSTANT] datatype [NOT NULL] [:= | DEFAULT initial_value]
    -- exemple
    Description varchar2(40);
    LType varchar2(40) := 'techonthenet.com Example';
    LTotal CONSTANT numeric(8,1) := 8363934.1;

-- ========= mini script SQL DVELOPPER
    SET SERVEROUTPUT ON -- ne pas oublier, sinon rien ne s'affiche
    DECLARE
        vEmail contacts.email%TYPE;
    BEGIN
        select EMAIL into vEmail from contacts where customer_id = 106;
        DBMS_OUTPUT.PUT_LINE('Email is:' || vEmail);
    END;
    -- pour info DBMS_OUTPUT.ENABLE/DISABLE/PUT/NEW_LINE/PUT_LINE/GET_LINE/GET_LINES
    -- DBMS_OUTPUT.PUT_LINE(sys.diutil.bool_to_int(vardeTypeBool)); --> affiche 0 ou 1

-- ======== OPERATEURS
    -- := affectation
    -- BETWEEN / IN / IS NULL / LIKE '%... / like '_...'
    -- / < > <= >=  /   <> ou !=
    -- is null / is not null
    -- AND / OR / NOT
    -- % : modulo
    -- || concat

-- =======



-- ========== FONCTIONS ANALYTIQUE
    -- RANK
    -- DENSE_RANK
    -- ROW_NUMBER
    SELECT category_id, ROUND(AVG( list_price ), 2 ) avg_list_price FROM products GROUP BY category_id;
    SELECT AVG( NVL( score, 0 )) FROM tests -- les valeurs nulle sont remplacés par zéro
    SELECT COUNT( DISTINCT val ) FROM items; -- comptage selon valeur distinctes
    SELECT category_id, COUNT(*) FROM products GROUP BY category_id ORDER BY category_id; -- comptage et tri, par catégorie

    -- nombre de produits pour toutes les catégories
    SELECT category_name, COUNT( product_id ) FROM product_categories LEFT JOIN products USING(category_id) GROUP BY category_name ORDER BY category_name;

    -- catégories qui comportent plus de 50 produits
    SELECT category_name, COUNT( product_id ) FROM product_categories LEFT JOIN products USING(category_id) GROUP BY category_name HAVING COUNT( product_id ) > 50 ORDER BY category_name;

    -- catégorie dont le prix du produit est le plus élevé, est compris entre 3000 et 6000
    SELECT category_name, MAX( list_price ) FROM products INNER JOIN product_categories USING(category_id) GROUP BY category_name HAVING MAX( list_price ) BETWEEN 3000 AND 6000 ORDER BY category_name;

    -- aggrégations sur liste
    SELECT job_title, LISTAGG(first_name, ',') WITHIN GROUP(ORDER BY first_name ) AS employees FROM employees GROUP BY job_title ORDER BY job_title;


-- ===================== UNION - INTERSECT - MINUS
    SELECT first_name FROM contacts UNION [ALL] SELECT first_name FROM employees;
    SELECT last_name  FROM contacts INTERSECT   SELECT last_name  FROM employees ORDER BY last_name;
    SELECT last_name  FROM contacts MINUS       SELECT last_name  FROM employees ORDER BY last_name;

-- ===================== INNER JOIN
    -- inner join         INNER JOIN : seulement les lignes de la table de gauche auxquelles correspondance des lignes de la table de droite
    -- left  join         LEFT  JOIN : toutes les lignes de la table de gauche, avec les valeurs correspondantes de la table de droite ou NULL
                            => WHERE O.salesman_id = E.employee_id(+)
    -- left outer join    LEFT JOIN with null : lignes de table de gauche qui n'existent pas dans la table de droite
    -- right join         RIGHT JOIN : toutes les lignes de la table de droite, avec les valeurs correspondantes de la table de gauche ou NULL
    -- right  outer join  RIGHT JOIN with null : lignes de table de droite qui n'existent pas dans la table de gauche
    -- full outer join    FULL OUTER JOIN : union de toutes les lignes,  avec ou sans les lignes communes, si l'on utilise une clause where ... NULL


-- ========== RECORD
    DECLARE
    CURSOR c_contacts IS
        SELECT first_name, last_name, phone
        FROM contacts;
    r_contact c_contacts%ROWTYPE; -- declare une variable typée grâce au curseur
    r_customer customers%ROWTYPE; -- declare une variable directement sur la structure d'une table
    -- il n'est pas possible de comparer 2 record par un simple =
    select * into R_customer from customers where customer_id = 1;
    INSERT INTO customers VALUES r_person;  -- insertion de données directement à partir

-- ========= TABLE
    CREATE TYPE t_customer_row as OBJECT ( id NUMBER, description VARCHAR2(50));
    CREATE TYPE t_customer_tab IS TABLE OF t_customer_row;


-- ========== CURSOR
    DECLARE
        CURSOR c_sales IS SELECT * FROM sales ORDER BY total DESC;
        r_sales c_sales%ROWTYPE;
    BEGIN
        OPEN c_sales;
        LOOP
            FETCH  c_sales  INTO r_sales;
            EXIT WHEN c_sales%NOTFOUND;
            -- DML
        END LOOP;
        CLOSE c_sales;
    END;

-- ====================== LES FONCTIONS

    -- agrégation
        AVG, SUM, MIN, MAX,

    -- string
        LENGTH, LTRIM, RTRIM, TRIM, REGEXP_SUBSTR, REGEXP_REPLACE, RPAD, LPAD, LOWER, UPPER, TRANSLATE

    -- date
       ADD_MONTHS, CURRENT_DATE, CURRENT_TIMESTAMP, LAST_DAY, MONTHS_BETWEEN, NEXT_DAY, ROUND, SYSDATE, TO_CHAR, TO_DATE
       EXTRACT : extract a field from a date

    -- math
        ROUND



-- ======================= MULTITENANT ARCHITECTURE - Oracle 12c
    -- schema approach : security issues, moving schema beetween server is difficult, ...
    -- CDB : Container database : Container ID : 0
    -- CDB = n PDBs + root container + Seed PDB

    -- root container : CDB$ROOT with common containers (Container ID : 1)
    -- PDBs : utilisent les redolog, les ctl files, undo table du ROOT container !!
    -- PDB$SEED (Container ID : 2) for creating new PDB
    -- Enable Multitenant Architecture =>

    show con_name -- nom du container auquel je suis connecté
    show con_id   -- id du container auquel je suis connecté

    select CON_ID, NAME  FROM V$CONTAINERS;
    select CON_ID, NAME  FROM V$PDBS;

    -- changer de container
    ALTER SESSION SET CONTAINER = XEPDB1 ;
    ALTER SESSION SET CONTAINER = CDB$ROOT ;

    -- pour une connexion directe sur un PDB
    sqlplus my_pdb_admin/password@localhost:1521/XEPDB2

    -- creating a new PDB
    CREATE PLUGGABLE DATABASE XEPDB2
        ADMIN USER my_pdb_admin IDENTIFIED BY password
        ROLES = (dba)
        DEFAULT TABLESPACE USERS
        DATAFILE 'C:\appli\oracle\product\18.0.0\oradata\XE\XEPDB2\data_file1.dbf' SIZE 50M AUTOEXTEND ON
        FILE_NAME_CONVERT=('C:\appli\oracle\product\18.0.0\oradata\XE\pdbseed','C:\appli\oracle\product\18.0.0\oradata\XE\XEPDB2');

    ALTER PLUGGABLE DATABASE  XEPDB2 OPEN ;

    -- liste des PDBS, containers
    SELECT CON_ID, NAME  FROM V$CONTAINERS;
    SELECT CON_ID, NAME, OPEN_MODE  FROM V$PDBS;
    SELECT * from dba_pdbs;

    -- dropper un PDB
    ALTER PLUGGABLE DATABASE XEPDB2 CLOSE IMMEDIATE;
    DROP PLUGGABLE DATABASE XEPDB2 including datafiles;

    -- transporter un PDB
    ALTER PLUGGABLE DATABASE XEPDB2 CLOSE IMMEDIATE;
    ALTER PLUGGABLE DATABASE XEPDB2 UNPLUG INTO 'C:\appli\oracle\product\18.0.0\oradata\XEPDB2.xml';
    DROP PLUGGABLE DATABASE XEPDB2 keep datafiles; -- keep datafiles !!!!!!!!
    CREATE PLUGGABLE DATABASE XEPDB2 using 'C:\appli\oracle\product\18.0.0\oradata\XEPDB2.xml' NOCOPY  TEMPFILE REUSE;
    ALTER PLUGGABLE DATABASE  XEPDB2 OPEN ;

    -- cloning
    alter pluggable database source_pdb close;
    alter pluggable database source_pdb open read only;
    create pluggable database target_pdb from source_pdb FILE_NAME_CONVERT=('/oradata/orcl/source_pdb/','/oradata/orcl/target_pdb/');
    alter pluggable database target_pdb open;

    -- ---------------- Dictionnary
    ---- views
    CDB_    : all objets in all containers
    DBA_    : all objets in the database
    ALL_    : all objets in the database the user has access to
    USER_   : all objets in the database owned by the user

    -- ---------------- Multitenant managing users
    -- local user : specific to a PDB
    -- common user : known in the whole container = root + all pdbs

    -- Create the common user using the default CONTAINER setting.
    -- can perform administrative task on the pdbs
    CREATE USER C##dba_user IDENTIFIED BY pass;
    GRANT CREATE SESSION to c##dba_user container=all;

    CREATE USER user_xepdb1 IDENTIFIED BY pass CONTAINER=CURRENT;
    GRANT CREATE SESSION TO test_user3 CONTAINER=CURRENT;


    -- comment voir les droits et les rôle d'un utilisateur


    -- ================================================= PL

    -- FUNCTION
    CREATE OR REPLACE Function FindCourse
       ( name_in IN varchar2 )
       RETURN number
    IS
       cnumber number;

       cursor c1 is
       SELECT course_number
         FROM courses_tbl
         WHERE course_name = name_in;

    BEGIN

       open c1;
       fetch c1 into cnumber;

       if c1%notfound then
          cnumber := 9999;
       end if;

       close c1;

    RETURN cnumber;

    EXCEPTION WHEN OTHERS THEN
       raise_application_error(-20001,'An error was encountered - '||SQLCODE||' -ERROR- '||SQLERRM);
    END;


    -- procedure
    create or replace PROCEDURE proc1 (emp_id IN NUMBER)
    IS
        emp_fname VARCHAR2(20);
    BEGIN
        SELECT nom  INTO emp_fname FROM employees where id_employee = emp_id;
        DBMS_OUTPUT.PUT_LINE('Employee name is: ' || emp_fname);
    END;


    -- package
    CREATE PACKAGE customer AS
        PROCEDURE find_salary(cust_id customer.id%TYPE)
        FUNCTION ...
    END customer

    CREATE PACKAGE BODY customer AS
        PROCEDURE
            ...
        END

    )




