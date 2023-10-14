#-- ========== APT
apt update                          #  mise à jour de la liste des paquets disponibles
apt upgrade                         #  met à jour les paquets installés
apt install / remove                #  install / supprime
dpkg --get-selections                   #  liste des paquets installés
apt list --installed                    #  liste des paquets installés
sudo apt-get remove --purge application # dégages proprement une application.

                                    #  liste des depots
apt-get --purge remove nomPaquet    #  supprime un paquet
apt-get clean                       #  nettoie la bdd des paquets
apt-rdepends                        #  examine dépendance d un paquet
apt-cache search -n firefox         #  recherche dans les paquets

# -- ========= search
sudo apt-get install apt-file       # outil pour rechercher ds la liste de tous les paquets dispo
apt search --names-only package_name             
             



#-- ========== nettoyer debian
apt-get autoremove
dpkg -P $(dpkg -l | awk '$1~/^rc$/{print $2}') -- nettoie fichierde config orphelin
aptitude purge ~c                               -- supprime dépendance inutile
sudo deborphan
sudo apt-get --purge remove `deborphan -n --guess-all` -- !!! à éviter


# ================= source.list
deb http://ftp.fr.debian.org/debian/ buster main
deb-src http://ftp.fr.debian.org/debian/ buster main

deb http://security.debian.org/debian-security buster/updates main contrib
deb-src http://security.debian.org/debian-security buster/updates main contrib

# buster-updates, previously known as 'volatile'
deb http://ftp.fr.debian.org/debian/ buster-updates main contrib
deb-src http://ftp.fr.debian.org/debian/ buster-updates main contrib
