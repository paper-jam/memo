
sqlplus francis@localhost:1521/XEPDB1


-- ========== WHOAMI
show user
select user from dual;
select distinct username from user_users;
select sys_context('USERENV', 'SESSION_USER') "USER" from dual;


-- ======== current user privilege
SELECT * FROM USER_SYS_PRIVS;
SELECT * FROM USER_TAB_PRIVS;
SELECT * FROM USER_ROLE_PRIVS;


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







