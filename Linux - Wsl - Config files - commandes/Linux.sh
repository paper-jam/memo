
#-- ========== divers
    cat /etc/lsb-release	# pour connaître la version sur UBUNTU
    cat /etc/debian_version # pour connaître la version sur DEBIAN
    unalias tree			# retire alias
    systemctl status		# show system status
    cat /proc/cpuinfo		# info sur processeur
    who -r 					# runlevel actuel
    man                     # use Space key to scroll page by page   
    clear -x                # n'efface pas le scroll
    move -u                 # move only when the SOURCE file is newer than the destination file or when the destination file is miss‐
    move fic1 fic2 /folder  # move fic1 and fic 2 into folder
    head / tail fic -n      # n lignes at the begin 
    tail -f fic             # display and refresh as the file grows
    date                            

    chown 					# change le propriétaire d'un fichier
    sudo !!					# ré-exécute la commande précédente avec sudo
    ldconfig                # pour mettre à jour / recharger les librairies disponibles LD_LIBRARY_PATH
    chroot                  # chroot /mnt /bin/bash, change la racine du système

    # --- open file
    sudo lsof -p $!







# ------------------------------------ redirecting - piping

# file descriptor
0 stdin     # data from keyboard, file , program
1 stout
2 sterror

# -- anamymous pipe
ls -l  | grep tot | wc -l

# --  sortie standard, erreur standard
ls > files.txt # - créé un nouveau fichier
ls 1> files.txt 2> out.log
ls 1>> files.txt 2>> out.log    # - ajoute au fichier existant 
ls 1>> files.txt 2>&1           # idem
ls > /dev/null  2>&1            # redirection dans le vide

# --  entrée standard
grep francis < /etc/passwd


# ------  suspended tasks  ->
#  ctrl + z -> send the current process in the background and stop it (alpine suspended)
fg      # bring the most recent task put in the background
fg 2    # bring the jobs #1 on foreground (Alpine : no parameter is allowed)
jobs    # list process in bacground (+ : default job   - : le suivant // default job )
jobs -l # print the pid of the jobs
bg 2    # re-start the job #2, still in the background






# ---- état du système
    htop                    # état des processus
    xrandr                  # à tester ... affiches les écrans dispo.
    free                    # état de la mémoire

# -- grep
    grep -v                             # inversion de la sélection
    grep -i                             # ignore la casse
    grep "this" demo_*                  # recherche this dans tous les fichiers qui commencent par demo_
    grep "first.*upper" demo_file       # qui contient une chaîne de caractère
    grep "first.\?upper" demo_file      # qui contient "first" et "upper", séparé par aucun ou un seul caractère
    grep -w "is" demo_file              # recherche du mot is, tout seul.
    grep -ir "this" *                   # recherche this dans tous les fichiers y compris ss-arborescence

    # - grep with regexp
    ? The preceding item is optional and matched at most once.
    * The preceding item will be matched zero or more times.
    + The preceding item will be matched one or more times.
    {n} The preceding item is matched exactly n times.
    {n,} The preceding item is matched n or more times.
    {,m} The preceding item is matched at most m times.
    {n,m} The preceding item is matched at least n times, but not more than m times.

    grep "^GNU" GPL-3                   # ligne qui commence par "GNU"
    grep "GNU$" GPL-3                   # ligne qui se termine par "GNU"
    grep -c "^$" fichier.log            # count empty lines

    grep -A 3 -i "example" demo_text    # affiche la ligne trouvée, ainsi que les 3 lignes qui suivent. A comme after
    grep -B 2 "single WORD" demo_text   # affiche la ligne trouvée, ainsi que les 3 lignes qui précèdent. B comme before
    grep -C 2 "Example" demo_text       # affiche la ligne trouvée, ainsi que les 2 suivantes et 2 précédentes

    # grep -- mettre les résulat en couleur
    export GREP_OPTIONS='--color=auto'  # à placer dans le .bashrc

    grep -v -e "a" -e "b" -e "c" test-file.txt  # qui ne contient ni a, ni b , ni c.
    grep -c this demo_file          # pour compter les occurences
    grep -l this demo_*             # ne retourne que le nom du fichier
    grep -lr this *                 # nom des fichiers de l'arbo. qu contiennent this
    grep -o "is.*line" demo_file    # affiche uniquement la pattern trouvée
    grep -o -b "pattern" file       # affiche l'offset en byte // au début du fichier
    grep -n "go" demo_text          # affiche le numéro de ligne



#-- ========== scripting
bash -x script 		-- mode debug
echo "$var"			-- double quote -> interprétaion des vars.
`pwd`				-- exec du code bash ds les back quote
read -p 'saisir votre nom : ' nom 	-- saisie var avec message
let "a = 5" 		-- affect. var numérique et calcul
$# $1 $2 $3 ...		-- contiennent les valeurs passés en paramètres
if [ test ] 		-- condition ... (ne pas oublier espace avant et après crochet)
test sur nombre/caractère/fichier
if [ ! -e fichier ]	-- si le fichier n existe pas...
while / for			-- boucle


#-- ========== background foreground
ctrl+z          # back to prompt
jobs            #  will list the jobs that have been started in the current terminal session.
[1]+  Stopped   # + -> indique default job
bg #            # continue process in background
fg #            # bring back the job in the foreground terminal

# -- ========= list process







# -- ========== dossier de base linux
/bin 		# exécutable du système
/sbin		# idem
/usr/bin 	# programme de l'utilisateur
/etc 		# fichier de configuration
/mnt 		# point de montage
/media		# pour cd dvd
/root 		# home du root
/srv
/opt 		# logiciel propriétaire
/run
/sys/
/var 		# contient backup/cache/log/www
