
-- ========== WHOAMI
show user
select user from dual;
select distinct username from user_users;
select sys_context('USERENV', 'SESSION_USER') "USER" from dual;



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

