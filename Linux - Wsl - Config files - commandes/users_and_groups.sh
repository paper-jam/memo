#-- ==========  users & groups =======
awk -F ":" '{print $1}' /etc/group  -- liste des groupe
awk -F ":" '{print $1}' /etc/passwd -- liste de tous les users (system ou classiques)
sudo adduser postgres --shell /bin/bash --home /home/postgres  # création utilisateur
deluser --remove-home joletaxi                                 # suppression d'un utilisateur
groups                                                         # liste des groupes d'un utilisateur
sudo usermod -a -G staff francis                               # ajout de l'utilisateur francis au group staff
id                                                             # id + gid + ... de l'utilisateur connecté
groups username             -- liste des groupes dun user
newgrp groupname            -- change le groupe à la volée
id                          -- retourne les ids dun user
who                         -- liste des utilisateurs connectés
netstat -antu               -- liste des ports ouverts
sudo service xdm start/stop -- demarre arrête le serveur X

# -- change password for a user 
passwd bob

# -- ========= SUDO 
apt install sudo
adduser francis sudo      # apt install adduser, si nécessaire
sudo -lU francis  			-- francis posséde les droits sudo ?


# -- ========= DOAS
# in /etc/doas.s/doas.conf, add the line
permit francis as root

# -- ======== changer un shell pour un utilisateur
cat /etc/shells 				# voir les shells disponibles
chsh --shell /bin/zsh bob       # necessite le package shadow sous alpine


# -- then
doas commandWithNoParameters 
doas -- command -param1...	# if one or more parameters



