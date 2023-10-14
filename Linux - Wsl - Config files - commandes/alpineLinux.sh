## --  ALPINE LINUX

#--- lancement manuel
wsl -d Alpine --CD ~

# installation documentation
apk add man man-pages

#--- install
adduser -g "francis" francis


apk add doas
adduser francis 
adduser francis wheel
vi /etc/doas.conf # and Ensure that this file contains : permit persist francis as root 

# package complémentaire
apk add openrc
doas apk add nginx






# -- package manager apk, s
# repositories dans /etc/apk/repositories
# https://www.cyberciti.biz/faq/10-alpine-linux-apk-command-examples/
apk add/del/
apk -s add nginx	# install nginx en mode simulation
apk -i upgrade 		# upgrade en mode Interactif 

add 	# install new package : apk add nodejs
info 	# prints information about installed or available packages


del 	Delete packages from the running system
fix 	Attempt to repair or upgrade an installed package
update 	Update the index of available packages
search 	Search for packages or descriptions with wildcard patterns
upgrade 	Upgrade the currently installed packages
cache 	Maintenance operations for locally cached package repository
version 	Compare version differences between installed and available packages
index 	create a repository index from a list of packages
fetch 	download (but not install) packages
audit 	List changes to the file system from pristine package install state
verify 	Verify a package signature
dot 	Create a graphviz graph description for a given package
policy 	Display the repository that updates a given package, plus repositories that also offer the package
stats 	Display statistics, including number of packages installed and available, number of directories and files, etc.
manifest 	Display checksums for files contained in a given package 







# ------------ installation mongodb
#https://www.how2shout.com/linux/how-to-install-mongodb-server-on-alpine-linux/
# data dans : /var/db

