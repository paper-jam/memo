
# -- ===== doc 
# https://learn.microsoft.com/fr-fr/powershell/scripting/windows-powershell/install/windows-powershell-system-requirements?view=powershell-7.2

get-help *

#  -- ==== editeur
powershell_ise.exe

# -- ===== powershell version
# version 7 are bases on dotnet core and no more .net fr
# version 6-7 assume backward compatibility with 5.01 and >
winget search Microsoft.PowerShell
winget install --id Microsoft.Powershell --source winget


compte utilisé pour le listener : NT SERVICE\OracleOraDB21Home1TNSListener
compte utilisé pour le OracleServiceXE : NT SERVICE\OracleServiceXE
localhost:1521/XEPDB1
localhost:5000/em


# -- ========== les cmdlets
# - get-command *service* : tous les commandes qui contiennent *service*
# - Add, Get, New, Set




# -- ========== les alias
get-alias

# -- ======== les scripts
get-ExecutionPolicy  # niveau execution scripts
# -> Allsigned    : tous les scripts doivent être signés
# -> Bypass       : open bar
set-ExecutionPolicy

# -- ======== les modules, enrichissent powershell
# - module officiel :
# - module communautaire :
# Installation dans ->
$env:psmodulepath
get-module -listAvailable
find-module
install-module

# -- ======== les variables
$MaVariable = "Hello"
[string]$MaVariable = "Hello"   # forcer le type

$resultat = get-Service | Where-Object{ $_.Status -eq "running"}
write-output $resultat    # eq de la commande echo en dos
Get-Service -Name wSearch # recherche un service nommé wSearch
Get-Service -Name wSearch | stop-service
stop-service -name wSearch
Get-Command -Module ActiveDirectory    # liste des commandes du module AD

# -- ======== les types powershell


# -- ======== le pipeline
get-Service | Where-Object{ $_.Status -eq "running"}



#https://www.youtube.com/watch?v=Ecdl1pOMtmE
#reprendre à 30:12







# -- ==========
$PSVersionTable      # version
get-ExecutionPolicy  # niveau execution scripts
set-ExecutionPolicy ... # https://learn.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2
Get-Hotfix | Select-Object HotFixID, InstalledOn, InstalledBy  # list des hotfix installés
get-psdrive -psprovider filesystem # file system
get-Localuser | ft name, Enabled,  Description, lastlogon
get-localGroupMember Administrateurs | ft name # membre du groupe administrateurs

get-clipboard
get-process | where {$_.ProcessName -notlike '' }
get-netipConfiguration -All

# === fichiers
get-Location    # pwd 
get-childitem   # dir
new-item test.txt # touch
set-content test.txt "contenu bidon"
get-content test.txt
gci | measure  # nombre de fichier dans le dossier 
gci | select-string 'chaine recherchée'












