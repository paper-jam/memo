# ---- ============================== créer un disque (clé -ssd) bootable depuis linux
#  -- http://papy-tux.legtux.org/doc1162/index.html
# 5F33~HX&:jnr\4m+o;\n-%#vI!GG\9u=Rn]pg@y#b-f:)X^4q2V4eMmdDgts

#
sudo dd if=/dev/zero of=/dev/sdc count=600 bs=1M conv=fsync status=progress

# partitionnement avec parted
# 1 partition de type EFI ESP de 512 Mo
# le reste en ext4 (pas besoin de partition pour le swap, on utilise un fichier)
sudo parted /dev/sdb
    mktable gpt
    mkpart primary fat32 1M 256M set 1 boot on name 1 ESP
    mkpart primary ext2 256M 100% name 2 system

# procéder au formatage
/sbin/mkfs.vfat -F 32 -n EFI /dev/sdb1   # si nécessaire : apt install dosfstools
/sbin/mkfs.ext4 -L system /dev/sdb2

# SUPPR /sbin/mkfs.ext4 -L fs_boot -O '^64bit' /dev/sdb2 # 64bit adressing disable
# SUPPR /sbin/mkfs.ext4 -L fs_root  /dev/sdb3
#lsblk -f /dev/sdb -o +UUID # pour verif

# on monte la partition principale et EFI dans /mnt /mnt/boot
sudo mount /dev/sdb2 /mnt

# on vérifier avec :
lsblk -f /dev/sdb

# faut installer debootstrap
apt install debootstrap

# OU montage du .iso (préalablement téléchargé) en cdrom, c'est plus rapide
sudo mount -o /home/francis/tmp/debian-10.3.0-amd64-netinst.iso /media/cdrom/
mount -o loop /home/francis/tmp/debian-9.2.1-amd64-netinst.iso /media/cdrom/

# lancer debootstrap en francis avec sudo, car en root => "unable to execute the target system"
sudo debootstrap --no-check-gpg --include=wireless-tools,console-setup,locales,keyboard-configuration,sudo,firmware-linux-free,cryptsetup --arch=amd64 buster /mnt file:/media/cdrom/

# montage de la partition EFI
mkdir /mnt/boot/efi
mount /dev/sdb1 /mnt/boot/efi

# recup des users et des groupes
grep "^[^:]*:x:[0-9][0-9][0-9][0-9]:" /etc/passwd >> /mnt/etc/passwd
grep "^[^:]*:x:[0-9][0-9][0-9][0-9]:" /etc/group >> /mnt/etc/group

# sources.list - faire une copie de la source
cp /etc/apt/sources.list /mnt/etc/apt/sources.list

# on reprend qq fichiers de configs
sudo cp /etc/{hosts,hostname,resolv.conf,locale.gen} /mnt/etc/
sudo cp /etc/{hosts,hostname,resolv.conf} /mnt/etc/  --> j'ai pris celui-ci au dernier essai


# modification du fstab vi /mnt/etc/fstab
# modifier le fichier fstab --> AVANT de lancer les grub/installe /update... c'est mieux !!
#
PARTLABEL=debootstrap      /               ext4    errors=remount-ro       0       1
PARTLABEL=ESP              /boot/efi       vfat    umask=0077      0       1



# ------------------- Montage du chroot
cd /mnt
bash -c 'for i in proc sys dev dev/pts run; do mount --bind /$i $i;done'
/sbin/chroot /mnt /bin/bash

# pour verif
[[ "$(stat -c %d:%i /)" = "$(stat -c %d:%i /proc/1/root/.)" ]] && echo "We are standalone!" || echo "We are chroot!"


# simplifie la vie
PATH="/sbin:$PATH"

# -- rafraichir APT
apt update
apt upgrade

# --- install paquet et image ==> à re-vérifier
apt install wpasupplicant console-setup console-data firmware-iwlwifi intel-microcode grub-efi wireless-tools
apt install firmware-atheros



# ---- les locales
# export LC_ALL=C  ()
# Vérifier que les paquets locales, console-setup, tzdata et keyboard-configuration sont installés.


/sbin/dpkg-reconfigure locales
/sbin/dpkg-reconfigure tzdata


# pc / azerty / French / Same as X11 (latin9) / Standard /
# keymap fr-latin9
apt install -y console-data
/sbin/dpkg-reconfigure console-setup
/sbin/dpkg-reconfigure keyboard-configuration
debconf-show locales


# ---------------- installation image/ grub / initramfs
# apt-cache search linux-image
apt install linux-image-amd64
grub-install /dev/sdb --removable
update-grub
update-initramfs -u -k all





# verif du hostname
cat /etc/hostname



# autre fichier
vi /etc/locale.conf
LANG=fr_FR.UTF-8

# ----- network
# The loopback network interfaces
# auto lo
# iface lo inet loopback
# The primary network interface
# allow-hotplug $iface
# iface $iface inet dhcp

echo "# The loopback network interfaces" >> /etc/network/interfaces
echo "auto lo" >> /etc/network/interfaces
echo "iface lo inet loopback" >> /etc/network/interfaces
echo " " >> /etc/network/interfaces
echo "# The primary network interface" >> /etc/network/interfaces
echo "allow-hotplug \$iface" >> /etc/network/interfaces
echo "iface \$iface inet dhcp" >> /etc/network/interfaces

# ******** FIN



#  -- =====================================================================================================


s# /etc/locale.gen
echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen
echo "fr_FR@euro ISO-8859-15" >> /etc/locale.gen

# ---- configuration de reseau
grub-install --efi-directory=/boot/efi --removable
grub-install --root-directory=/mnt/chroot/ --recheck /dev/hda
grub-install --efi-directory=/mnt/boot/efi --boot-directory=/mnt/boot --removable


# localtime
ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime


# Installer les firmwares et microcodes nécessaires
sudo apt install firmware-iwlwifi intel-microcode


# sudo debootstrap \
# --no-check-gpg \
# --arch=amd64 \
# --include=aptitude,console-setup,locales,keyboard-configuration,\
# command-not-found,sudo,intel-microcode,firmware-linux-free,firmware-misc-nonfree,\
# firmware-iwlwifi,cryptsetup,network-manager \
# --exclude=vim \
# --components=main,contrib,non-free \
# buster \
# /mnt \
# file:/media/cdrom/

# echo "deb http://deb.debian.org/debian/ buster main contrib non-free" >> /mnt/etc/apt/sources.list
# echo "deb http://security.debian.org/ buster/updates main contrib non-free" >> /mnt/etc/apt/sources.list
# echo "deb http://deb.debian.org/debian/ buster-updates main contrib non-free" >> /mnt/etc/apt/sources.list
# echo "deb http://deb.debian.org/debian/ buster-proposed-updates main contrib non-free" >> /mnt/etc/apt/sources.list
# echo "deb http://ftp.debian.org/debian buster-backports main contrib non-free" >> /mnt/etc/apt/sources.list





# on génère le fstab (
apt-get install arch-install-scripts
genfstab -L /mnt
genfstab -L /mnt | grep -v sda # OK !!
genfstab -L /mnt | grep -v sda >> /mnt/etc/fstab


# --- Vérifications

# si message d'erreur :
# GPG error: .... The following signatures were invalid...
apt-get clean
rm /var/lib/apt/lists/*
apt-get update

# configuration des locales
apt install -y locales
dpkg-reconfigure locales # fr.UTF8
dpkg-reconfigure tzdata  # pour le fuseau horaire


hwclock --systohc --utc
apt install -y ntpdate


# --- apt source.list
vi /etc/apt/sources.list

echo "deb http://deb.debian.org/debian/ buster main contrib non-free" >> /mnt/etc/apt/sources.list
echo "deb http://security.debian.org/ buster/updates main contrib non-free" >> /mnt/etc/apt/sources.list
echo "deb http://deb.debian.org/debian/ buster-updates main contrib non-free" >> /mnt/etc/apt/sources.list
echo "deb http://deb.debian.org/debian/ buster-proposed-updates main contrib non-free" >> /mnt/etc/apt/sources.list
echo "deb http://ftp.debian.org/debian buster-backports main contrib non-free" >> /mnt/etc/apt/sources.list

apt update && apt upgrade -y

# clavier
# pc / azerty / French / Same as X11 (latin9) / Standard ==> fr-latin9
apt install -y console-data
# si besoin de recommencer :
dpkg-reconfigure -plow console-data

# sortir du CHROOT
exit
# qq fichiers à récupérer

sudo cp /etc/network/interfaces /mnt/etc/network/



# Nous entrons à nouveau dans notre système chrooté
sudo chroot /mnt /bin/bash

# Finalisation
export LC_ALL=C
debconf-show locales



apt install grub-efi #en cours
grub-install --target=x86_64-efi --efi-directory=/boot/efi
update-grub

grub-mkconfig -o /boot/grub/grub.cfg


# Mettre à jour l'initramfs
sudo update-initramfs -u -k all


#  =============================== FIN
