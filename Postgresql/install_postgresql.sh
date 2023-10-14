# -- ==========  POSTGRESQL

# -- install via APT

# -- pré-requis
sudo apt-get install libreadline-dev
sudo apt-get install zlib1g-dev
sudo apt-get install libsystemd-dev
sudo apt-get install libssl-dev
sudo apt-get install gcc
sudo apt-get install make




mkdir ~/installPG && cd ~/installPG
curl -LO https://ftp.postgresql.org/pub/source/v10.4/postgresql-10.4.tar.bz2
tar xvjf postgresql-10.4.tar.bz2
cd postgresql-10.4/

sudo ./configure --with-systemd --with-openssl


sudo make
sudo make install

# ajout utilisateur
sudo adduser postgres --shell /bin/bash --home /home/postgres
sudo adduser postgres sudo
sudo login postgres
sudo cp /home/francis..bash_aliases .

# modif du .profile
export PATH=/usr/local/pgsql/bin:$PATH
export PGDATA="/data/pgsql/vvcol"

# verif
locale -a
# il ne doit pas y avoir de messages d'erreur
# sinon dpkg-reconfigure locales

# pour les datas
sudo mkdir -p /data/pgsql/vvcol
sudo chown -R postgres /data/pgsql/vvcol

# a supprimer ...
# pour les log ??
#udo mkdir -p /var/log/pgsql/
#sudo chown postgres:postgres /var/log/pgsql/

# init de la BSS , va utiliser $PGDATA pour y créer l'instance
/usr/local/pgsql/bin/initdb -D $PGDATA

# test manuel start / test / stop server
pg_ctl -D $PGDATA -l /var/log/postgresql/pg_start.log start
# y a t il une instance postgresl qui tourne ?
ps -ef | grep postgres
pg_ctl -D $PGDATA stop

# le client en mode commande :
psql

# si problème : uninstall postgresql
make uninstall
sudo rm -rf /usr/local/pgsql
sudo rm -rf /usr/share/postgresql/
sudo rm -rf /usr/share/postgresql/postgresql-common
sudo rm -rf /var/lib/sudo/lectured/postgres
sudo rm -rf /var/lib/sudo/ts/postgres
sudo rm -rf /etc/postgresql/
sudo rm -rf /etc/postgresql-common/
sudo rm -rf /var/lib/postgresql/
sudo rm -rf /var/log/postgresql/

# démarrage postgresql en mode systemd
sudo vi /etc/systemd/system/postgresql.service
# y placer le code ci-dessous
[Unit]
Description=PostgreSQL database server
Documentation=man:postgres(1)
[Service]
Type=notify
User=postgres
ExecStart=/usr/local/pgsql/bin/postgres -D /usr/local/pgsql/data
ExecReload=/bin/kill -HUP $MAINPID
KillMode=mixed
KillSignal=SIGINT
TimeoutSec=0
[Install]
WantedBy=multi-user.target

sudo systemctl daemon-reload # load the updated service file from disk
sudo systemctl enable postgresql
sudo systemctl start postgresql

