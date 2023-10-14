#-- ========= VirtualBox
# monter le cdrom
mount /dev/sr0

# prérequis installation des "guests-additions"
sudo apt-get install linux-source
sudo apt-get install linux-headers-$(uname -r)
sudo apt-get install make

# on peut alors installer les guestAdditions
sudo sh ./VBoxLinuxAdditions.run

# indiquer le point de montage pour les shared folder
sudo VBoxControl guestproperty set /VirtualBox/GuestAdd/SharedFolders/MountDir /home/toto/
# et pour vérifier
sudo VBoxControl guestproperty get /VirtualBox/GuestAdd/SharedFolders/MountDir
