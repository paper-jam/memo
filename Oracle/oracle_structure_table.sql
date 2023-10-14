
-- ========== historique version
  - 2009 : version 11g
  - 2013 : version 12c
  - 2018 : version 18
  - 2019 : version 19c


-- ====================== version oracle



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

