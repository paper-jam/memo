# ajout d(une clé ssh pour accès aux repo git
# depuis l'accédant, génerer ET enregistrer la clé vps_git (vps_git.pub est la clé publique)
ssh-keygen -t ed25519 -b 4096 -C "francis.jam@gmail.com"
eval "$(ssh-agent -s)" # déarre l'agent
ssh-add ~/.ssh/vps_git
# depuis l'IHM de git -> settings -> SSH and GPG keys -> New SSH key -> paste public key content



# les token ne peuvent être utilisé uniquemenet pour les opération SSH
# pour forcer git à utiliser la connexion en SSH

git config --global url."git@github.com:".insteadOf https://github.com/
git config --global url."git://".insteadOf https://

# ce qui aboutit à une modification du fichier ~/.gitconfig
[url "git@github.com:"]
        insteadOf = https://github.com/
[url "git://"]
        insteadOf = https://


 # git & linux
git config --global credential.helper cache


 # git and vs code
- cliquer en bas à gauche pour avoir le menu relatif aux branches
# Menu en haut de l'explorateur, pour voir
# Explorateur -> CHRONOLOGIE, pour voir la structure du projet
- Commit avec ammend (à revoir)


 # config
git config --global  -l 	# liste des param. globaux
git config --local   -l 	# liste des param. locaux

# -- token valbale jusqu'au 31/05/2023
# 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

# - init et config
mkdir nomprojet && cd nomprojet
git init
git config --local
git config --global -> enregistré dans ~/.gitconfig
git config --global user.email "francis.jam@gmail.com"
git config --global user.name "paper-jam"
git config --global color.ui true

git add README.md
git commit -m "first commit"
git branch -M main     # renomme master en main (master et main, c'est du kiff-kiff)
git remote add origin https://github.com/paper-jam/dotfiles.git   # bien utiliser https si token, mais git:.. avec ssh
git remote add origin git@github.com:paper-jam/dotfiles.git  		# bien utiliser https si token, mais git:.. avec ssh
git ls-remote      // verifie la connection au dossier local
git pull 		   // demande le token, les passwords sont interdits depuis 2021


# spécifie la stratégie pour les rebase
git config pull.rebase false

# ------ connecet with ssh
#1 -- génération d'une cle ssh
ssh-keygen -t ed25519 -C "francis.jam@gmail.com"

#2 --  ajout d'une clé à ssh-agent
# start the ssh-agent in the background
$ eval "$(ssh-agent -s)"
> Agent pid 59566
$ ssh-add ~/.ssh/id_ed25519

# test
ssh -T git@github.com




-- pour verif
git config --list
git status
git ls-files
git add nomFic
git commit -m "mon premier commit"
git commit -a -m "commit tous les fichiers concernés"
git add "*.html"
git add --all


# -- pour ignorer des fichiers
touch .gitignore  # (y placer la liste des fichiers que l'on veut ignorer)

# -- historique
git log
git log -n 2                -- les 2 derniers
git log --oneline
git log -p index.html       -- uniquement ce fichier
git log -n 2-p index.html

-- différence
git diff                -- tous les fichiers supprimés depuis la dernière modification

-- revenir en arrière pour visualiser  (il sera impossible de faire des modifs)
git log --oneline -p index.html
git checkout id_commit
git checkout master                 #-- reviens en tête
git checkout id_commit nomFichier   #-- reprend un fichier tel qu'il était dans un commit pour le remettre en tête
git checkout master nomFichier      #-- reprend un fichier tel qu'il était dans le master

-- revert : permet de défaire un commit, n'altère pas l'historique
git revert id_commit
git revert id_commit nomFic

-- reset :
git reset id_commit			#-- a l'historique des commit tout ce qui a été fait, mais laisse les modifs dans les fichiers
git reset --hard id_commit	#-- reviens au commit, et dégage tout ce qui a été fait

-- partir en branche
git branch nomBranche       #-- créé la branche
git checkout nomBranch      #-- permet de sauter sur la branche
git checkout master         #-- revient à la branche
git branch 					#-- liste des branches
git branch -r 				#-- liste des branches sur depôt remote



-- réintégration des modifs
- se placer sur la branche qui va accueillir les modifs
git checkout master
git merge nomBranche            #-- recup des modifs de la branche
git merge --no-ff nomBranche    #-- recup des modifs de la branche sans fast forward
git branch -d nomBranche        #-- suppression de la branche (impossible si les commit des modifs n'ont pas été réalisé)


# -- manipuler l'historique (8/18)




# -- remisage
git stash ---> à revoir
git stash                   #-- met de côté les modifs en cours en vue d'un remisage
git stash list              #-- pour voi
git stash apply             #-- remet les modifs à leur place
git statsh drop             #-- supprime le stash

-- depot en remote
git remote add origin git@github.com:paper-jam/vvcol.git
git push -u origin --all        # -- envoie tout
git remote -v                   # -- affiches l'URL du dépôt
git branch -r                   # -- list des branches dans le depot remote


# -- fork
#
# - sur un fork, ne jamais travailler sur la branche master
# - créer une branche sur la quelle on peut faire des modifs
#
# -- hook
# - permet d'automatiser une action (envoie mail, twitter..) lorsque le repository est modifié

