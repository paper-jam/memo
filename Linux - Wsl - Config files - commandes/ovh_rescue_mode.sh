# -- ========== RESCUE MODE VPS
# https://docs.ovh.com/fr/vps/affichage-bootlog-dans-kvm/#etape-3-lancer-la-commande-chroot
# sur ovh.com, "redemarrer en mode rescue"
# -> attendre la réception d'un mail avec le nouveau mot de passe root, puis se connecter en ssh sur port 22
umount /dev/sdb1  # il faut commencer par démonter
mount /dev/sdb1 /mnt
mount -t proc none /mnt/proc
mount -o bind /dev /mnt/dev
mount -t sysfs none /mnt/sys/
chroot /mnt
# faire les modifs nécessaires pour cooriger la situation : ssh, firewall ..
# modifier /etc/default/grub
vi  /etc/default/grub # -> GRUB_CMDLINE_LINUX_DEFAULT="console=ttyS0 console=tty0"
update-grub
# redémarre le VPS via le site ovh.com
