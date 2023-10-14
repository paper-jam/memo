----------- installing Debian through debootstrap with UEFI boot using Arch Linux live CD -----------
# 1. Select ‘Arch Linux archiso x86_64 UEFI CD’ in UEFI boot menu

# 2. establish an internet connection - wifi for example
wifi-menu wlp2s0

# 3. install debootstrap from Arch Linux AUR
pacman -Sy
cd /usr/share/kbd/consolefonts
pacman -S terminus-font
pacman -S gcc fakeroot
setfont ter-v18n.psf.gz
su arch
wget http://archlinux.thaller.ws/community/os/x86_64/debootstrap-1.0.93-2-any.pkg.tar.xz
pacman -U debootstrap-1.0.93-2-any.pkg.tar.xz

# 4. partitioning
parted -a optimal /dev/sda
mklabel gpt
unit MB
mkpart EFIBOOT fat32 0% 256M
set 1 boot on
mkpart root ext4 256M 100%
quit
mkfs.vfat -F32 -n EFIBOOT /dev/sda1
mkfs.ext4 -L root /dev/sda2

# 5. mount partition
mount /dev/sda2 /mnt
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi

# 6. install base system - jessie for example
debootstrap --variant=minbase --arch amd64 jessie /mnt http://http.debian.net/debian/

# 7. generate fstab
genfstab -p -U /mnt > /mnt/etc/fstab

# 8. configure apt
arch-chroot /mnt /bin/bash
export PATH=/bin:/sbin:/usr/bin:/usr/sbin
export LANG=C
dpkg --add-architecture i386 - if you have 64 bit system
apt update
apt install debian-keyring vim
vim /etc/apt/sources.list

deb http://http.debian.net/debian jessie main contrib non-free
deb-src http://http.debian.net/debian jessie main contrib non-free

deb http://security.debian.org jessie-updates main contrib non-free
deb-src http://security.debian.org jessie-updates main contrib non-free

apt update

# 9. configuring locale
apt install locales console-setup
dpkg-reconfigure locales
dpkg-reconfigure console-setup

# 10. clock and time zone
dpkg-reconfigure tzdata

# 11. hostname
echo debserver > /etc/hostname

# 12. root password and add users - admin user "username" for example
passwd
useradd -m -g users -s /bin/bash username
passwd username
13. install kernel and firmware - for 64 bit system
apt install init dbus linux-base linux-image-amd64 linux-headers-amd64
apt install firmware-linux

or install

apt install firmware-linux-free

and if you want

apt install ifupdown openssh-server

# 14. configure network - dhcp lan for example
vim /etc/network/interfaces - add this:

auto eth0
allow-hotplug eth0
iface eth0 inet dhcp

# 15. NOT install bootloader - EFIStub for uefi systems
mkdir -p /boot/efi/EFI/debian
vim /etc/kernel/postinst.d/zz-update-efistub - add this:

#!/bin/sh
cp /vmlinuz /initrd.img /boot/efi/EFI/debian/

chmod +x /etc/kernel/postinst.d/zz-update-efistub
/etc/kernel/postinst.d/zz-update-efistub

exit
    $UUID replace by your / root uuid
    for example, if your root is /dev/sda2 , then: blkid /dev/sda2
efibootmgr -c -g -L "Debian - EFI stub" -l '\EFI\debian\vmlinuz' -u 'root=UUID=$UUID ro quiet rootfstype=ext4 add_efi_memmap initrd=\\EFI\\debian\\initrd.img'

# 16. unmount the partitions and reboot
umount -R /mnt
reboot
