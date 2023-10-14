# -- ======== commandes de manipulations de fichiers
blkid           # identifiant de toutes les partitions, cohérence avec /etc/fstab
mount           # indique la liste de tous les montages
umount          # démontage
swapon --show   # affiche les espaces de swap
swapoff         # démonte un swap
chroot          # chroot /mnt /bin/bash, change la racine du système
tree -ad        # directory only

# -- occupation du disque
df      # df -h / df -i / espace disponible sur disque
du -sh  # espace occupé par les fichiers
ncdu    # autre u

xxd nomfic      # -- xxd -- affichage en hexa <-> decimal d'un fichie
chroot path     #-- indique la nouvelle racine du système

# -- dd -- disk destroy, data dump, control the bytes that are copied, duplicate same disk...
dd if=inFile of=outFile bs= count= skip= seek= conv=notrunc
    # bs is block size, default 512, à modifier pour optimiser
    # count = number of block to move (non  )
    # skip = nombre de bloc à sauter, en début de fichier. Skip avec un I,comme celui de If
    # seek = sauter les x premiers caractères in the output file => suppose d'utiliser conv=notrunc

# -- lsblk
 - RO : Real-Only /
 - RM : removable
 - MAJ / MIN : major and minor device number
 - ROTA : ROTATION

-g --files0-from=


#to make a bootable key, rapidement
sudo dd if=debian-10.3.0-amd64-netinst.iso of=/dev/sdb
# to erase the drive
sudo dd if=/dev/zero of=/dev/sdb bs=1M count=1024
# moving data from a drive to another
# à éviter : depuis un disque dur (spinning drive) vers un SSD
dd if=/dev/sdb of=/dev/sdc

# make a bootable





# ----- creating a swapfile
sudo dd if=/dev/zero of=swapfile bs=1MiB count=512
$ ls -l swapfile    # to verify
sudo chmod 600 /swapfile
sudo mkswap /swapfile     # set the swap file
sudo swapon /swapfile     # enable the swap file
sudo swapon --show        # to verify

# dans etc/fstab, ajouter :
/swapfile none swap defaults 0 0

# -- wc

# -- ==========  find / grep pour rechercher des fichiers
#  recherche unfichier qui comorte tel mot cle, en maj ou min
find /etc -name passwd 2> /dev/null     # redirection mes. erreurs vide
find /rep1 /rep2 -name 'set*' -type d   # dossiers qui commencent pas 'set' depuis les doosiers rep1 et rep2
find . -size +10k                       # k, M or G
find . -size +100k -exec ls -lh {} \;   # nom et taill lisible des fichiers de + de 100k

grep --include=\*.py -rnw . -e "math"   # r recurse / n number line / w whole word / -l just the file name
grep -Ril "text-to-find-here" /         #  Recurse / Ignore case /  l : file name only
grep --include=\*.py --exclude-dir=venv -Ril "math" .; # idem mais exclu venev



# -- ==========  LVM
# -- https://access.redhat.com/documentation/fr-fr/red_hat_enterprise_linux/6/html/logical_volume_manager_administration/lv_extend
df -h
fdisk -l

lvs     # lists out logical volumes within an LVM group
vgs     # list out the volume groups within a an LVM group
pvs     # lists out the physical volume in a LVM group

pvcreate
# étndre un physical volume (ex : suite à acroissement du disque sous oracle VM)
# utilisation de Gaprted requise
pvdisplay /dev/sda2     # affiche les caractéristiques du volume physique
lvscan                  # les volumes logiques
lvchange -a n /dev/ol/swap
lvchange -a n /dev/ol/root
xfs_growfs /dev/mapper/ol-root

# autre commande
pvcreate
vgextend nom_volume_a_etendre patition physique

-- to resize a partion
-- restart in rescue mode
lsblk
