# -- ========== install FTP (pro-ftp)
# linuxconfig.org/how-to-configure-ftp-server-on-debian-9-stretch-linux
sudo apt-get install proftpd
systemctl restart proftpd
adduser userftp
# -- modif dans /etc/proftpd/proftpd.conf :
# default Root      ~
sudo apt-get install quota
# modifier /etc/fstab en rajoutant usrquota (ou groupquota)
# UUID=1ec70269-92d1-4c9d-9a71-83b9b5e6c8e7 /               ext4    errors=remount-ro,usrquota 0       1
mount -o remount /
quotacheck -cum /       # Crée le sytème pour les Utilisateus linux, pas besoin de reMonter
quota on /
edquota francis         # fixe la quota : 1000 blocks = 1 Mo # pas besoin de redémarrer
quota francis           # affichage
repquota -a             # Pour un rapport global sur tous les utilisateurs
