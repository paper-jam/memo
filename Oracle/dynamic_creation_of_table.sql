-- PS pour la création dynamique de table selon les informations contenues dans les tables suivantes 
-- table LISTE_TABLES, contient les noms des tables
-- table LISTE_COLONNES, contient les noms des colonnes, leur type, et le nullable
-- pour EXECUTE IMMEDIATE, le grant explicite suivant peut-etre obligatoire : grant create table to nomUtilisateur
CREATE OR REPLACE PROCEDURE dynamic_creation_of_table IS

    sqlcommand VARCHAR2(4000);
    
    CURSOR c1 IS
    WITH column_concat AS (
        SELECT
            id,
            LISTAGG(nom_colonne
                    || ' '
                    || type_colonne
                    || ' '
                    || decode(nullable, 'OUI', 'NULL', 'NON', 'NOT NULL'), ',') WITHIN GROUP(
            ORDER BY
                nom_colonne
            ) AS sql_for_col
        FROM
            liste_colonnes
        GROUP BY
            id
    )
    SELECT DISTINCT
        'CREATE TABLE '
        || t.nom_table
        || ' ('
        || c.sql_for_col
        || ')'
    FROM
             column_concat c
        JOIN liste_tables t ON t.id = c.id;

BEGIN
    OPEN c1;
    LOOP
        FETCH c1 INTO sqlcommand;
        EXIT WHEN c1%notfound;
        dbms_output.put_line(sqlcommand);
        EXECUTE IMMEDIATE sqlcommand;
    END LOOP;

END;