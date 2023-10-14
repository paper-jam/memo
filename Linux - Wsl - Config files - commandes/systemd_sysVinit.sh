# -- ========== new systemD -- certaine commande peuvent nécessiter un SUDO
systemctl status
systemctl status apache2
systemctl list-units                    # tous les services, socket, device,mount, path
systemctl -t service list-units         # seulement les services
systemctl disable nginx.service         # désactive - lors du démarrage de l'ordi
systemctl enable nginx.service          # réactive - lors du démarrage de l'ordi
systemctl stop nginx.service            # stop un service
systemctl restart nginx.service         # redémarre un service
systemctl is-enabled nginx              # indique si une service est actif
systemctl list-units --type=target -all # affiche les targets
systemctl --failed                      # indique les services qui n'ont pas démarré
systemctl --system daemon-reload        # recharge systemd
systemctl daemon-reload                 # load the updated service file from disk
journalctl -b                           # message en provenance du boot processus
journalctl -u nginx                     # message du daemon nginx
journalctl -xe

systemctl get-default                   # conaître le run-level actuel
systemctl reboot                        # redémarre l'ordi
systemctl poweroff                      # éteint l'ordi

-- ========= Debian runlevel
0 (halt the system) 
1 (single-user / minimal mode) 
2 through 5 (multiuser modes) //  Default Debian installation does not make any difference between runlevels 2-5
6 (reboot the system). 

-- ==========  SysVinit
service <nomDuService> stop/start/restart/reload/status
service --status-all
service <nomDuService> condrestart		# Restarts if the service is already running. 
chkconfig --list						# Print a table of services that lists which runlevels each is configured on or off 
ls /etc/rc.d/init.d/					# Used to list the services that can be started or stopped 
service <nomDuService> on/off

-- ========== openrc -- https://wiki.gentoo.org/wiki/OpenRC
rc-status --list		# ???
rc-status --manual 		# To see manually started services
rc-status <runlevel>   	# Runlevel : sysinit ---> boot ----> default (nonetwork shutdown) 
rc-status -runlevel 	# print the current runlevel name
rc-status --servicelist # show all services

/etc/init.d/<serviceName> stop/start/restart  	# stop/start/restart a service
/etc/init.d/<serviceName> zap 					# reset the status in case of crash

# all runlevels have a folder in /etc/runlevels, with symlinks to /etc/init.d/
rc-update add <serviceName> runlevel			# adding a service in a runlevel (do not start it)
rc-update delete <serviceName> runlevel 		# remove a service from a runlevel
rc-update -v 									# show all service with runlevel

rc-service --list								# list all available services
rc-service <serviceName> start/stop/restart  	# easier syntax to start/stop...

-- /etc/rec.conf 
rc_parrallel="YES"			# Speed up booting process






-- ====== divers

/sbin/init -- --> PID = 1 











