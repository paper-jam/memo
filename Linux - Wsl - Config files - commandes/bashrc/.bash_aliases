# python 3 par défaut
# alias python='/usr/bin/python3'

# format Long ,exclus cachés, exclus . et .. , Tri sur date modif inveRsé
alias ll='ls -lrt'

# format Long, incl. cachés, excl . et .. , Tri sur date modif inveRsé
alias lla='ls -lArt'

# ajoute un signe (*/=>@| ) selon le type du fichier (pratique quand on a pas la couleur)
alias l='ls -F'

# ajoute un signe (*/=>@| ) selon le type du fichier (pratique quand on a pas la couleur), incl. cachés, excl . et ..
alias la='ls -AF'

# format Long, uniquement les dossiers visibles
alias ld='ls -dl */'

# format Long, uniquement les dossiers, incl. cachés, tri cachés-visibles
alias lda='ls -dlX */ .*/'

alias u='cd .. && ls'
alias cl='clear'
alias stop='sudo systemctl poweroff'
alias reboot='sudo systemctl reboot'
alias lu='systemctl list-units'

# list des paquets installés
alias aptlist='apt list --installed'

# divers
alias h10='history 10'
alias cdvv='cd /var/www/vvcol'

# GIT
# Git Aliases
alias gs="git status"
alias gc="git commit"
alias gca="git commit --amend"
alias gco="git checkout"
alias gcom="git checkout master"
alias gap="git add -p"
alias gpl="git pull"
alias gr="git rebase"
alias gst="git stash"
alias gw="git web"
alias gwu="git web upstream"
alias gwi="git web --issues"
alias gwp="git web --pulls"
alias gwup="git web upstream --pull-request"
alias gpum="git pull upstream master"
alias gpoh="git push -u origin HEAD"
alias gri="git rebase -i \$(git merge-base HEAD master)"
alias gd="git diff"
alias gcb="git clean-branches"
alias gpohw="gpoh && git web --pull-request"



