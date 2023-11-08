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

-- ======== OPERATEURS
    -- := affectation
    -- BETWEEN / IN / IS NULL / LIKE '%... / like '_...'
    -- / < > <= >=  /   <> ou !=
    -- is null / is not null
    -- AND / OR / NOT
    -- % : modulo
    -- || concat

-- ========== EXPLAIN PLAN
    -- https://www.youtube.com/watch?v=Xpmi55rn4YE
    -- permet de voir l'arborescence des opérations
    -- permet de voir si les index sont bien mis en jeu.
    explain plan for select * from customers;
    SELECT * from table(dbms_xplan.display);

    -- no need to use explain before
    -- 3 steps : execute request, get id request, show plan
    select /*+ GATHER_PLAN_STATISTICS */ /*toto*/ co.contact_id, co.email, customers.name  from CONTACTS co inner join CUSTOMERS using (customer_id);
    select * from v$SQL where sql_text like '%toto%';
    SELECT * FROM table(DBMS_XPLAN.DISPLAY_CURSOR('f0fyu0r7m028x',format=>'ALLSTATS LAST +cost +bytes +outline'));

    -- dans la section outline_data  -> la ligne 'LEADING' indique l'ordre dans le quel se font les jointures
    dans SQL developper
    F10 : explain plan ou F6 ;: autotrace



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


-- ========= select and fetch
select * from products FETCH NEXT 5 ROWS ONLY;          -- 5 premières lignes
select * from products FETCH FIRST 5 ROWS ONLY;         -- first = next
select * from products FETCH FIRST 5 PERCENT ROWS ONLY; -- 5% des lignes




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


    -- ================================================= FUNCTION - PROCEDURE - PACKAGE

    -- FUNCTION

    -- pour executer une fonction rapide
    declare
    v_Return NUMBER;
    begin
        v_Return := 1;
        v_Return := get_total_sales(2016);
        DBMS_OUTPUT.PUT_LINE('v_Return = ' || v_Return);
    end;

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


    -- procedure -- (pour executer EXEC proc1(312)    )
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

