
-- la date du jour
SELECT CURRENT_DATE from dual;                          -- date courante
SELECT nvl(NULL, 'bonjour') FROM dual;                                    -- retourne bonjour
SELECT ... FROM ... ORDER BY ... FETCH NEXT 5 ROWS ONLY;        -- les 5 premières lignes
SELECT ... FROM ... ORDER BY ... FETCH NEXT 5 ROWS WITH TIES;   -- les 5 premières lignes + ... voir doc
SELECT ... FROM ... ORDER BY ... FETCH FIRST 5 PERCENT ROWS ONLY;  -- 5% des lignes
SELECT ... FROM ... ORDER BY ... OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;
SELECT ROWNUM, ROWID from employees where ROWNUM < 10;  -- pas le même comportement que fetch
SELECT ... FROM .... WHERE order_date BETWEEN DATE '2016-12-01' AND DATE '2016-12-31';
SELECT ... FROM ... WHERE UPPER(first_name) LIKE 'JE_%';    -- prenom commence par JE
SELECT ... FROM ... WHERE salesman_id IS NULL

-- comment dedoublonner
SELECT   COUNT(*) AS nbr_doublon, champ1, champ2, champ3
FROM     table
GROUP BY champ1, champ2, champ3
HAVING   COUNT(*) > 1

-- sur un seul champ
SELECT   COUNT(email) AS nbr_doublon, email
FROM     utilisateur
GROUP BY email
HAVING   COUNT(email) > 1



-- comment optimiser




--


