
#-- ========== scanner les ports ouvrets d'un serveur
#nmap -options ip_du_serveur
nmap -sS -sU ip_du_serveur
nmap -sS -sU localhost
nmap -sS -sU -sV 192.168.1.101


# -- ========== network =========================================
ip a                    # anciennement ifconfig
ifup enp0s8             # active l'interface réseau enp0s8
ifdown enp0s8           # désactive l'interface réseau
ls /sys/class/net/      # donne la liste des interfaces réseaux
hostnamectl set-hostname nouveauNom  # - pour changer le nom du serveur



# ========== fail2ban =====================
fail2ban-client reload              #-- redémarre
fail2ban-server status
fail2ban-client status              #-- prison active
fail2ban-client status sshd         #-- affiche laactivité de la prison


# ========== NF TABLES :  Net Filter projects

# Nftables remplace plusieurs outils
    # iptables: administration des règles du pare-feu pour IPv4
    # ip6tables: administration des règles du pare-feu pour IPv6
    # arptables: administration des règles du pare-feu pour ARP
    # ebtables: administration des règles du pare-feu pour la configuration de bridge (pont)

# install
    apt-get install nftables
    systemctl enable nftables.service

    # -- Tables are containers for chains, sets and stateful objects.
    nft add table Family nomTable
    nft delete table family nomTable      # Family obligatoire
    nft list   table nomTable
    nft flush  table nomTable

    # -- Chains are container for rules
    # -- une "base chain" est une chaîne qui se rattache directement à un hook
    nft add     chain nomTable nomChaine type filter|net|route hook typeHook (device nomDevice) (priority P) (policy P)
    nft create  chain nomTable nomChaine
    nft delete  chain nomTable nomChaine
    nft list    chain nomTable nomChaine
    nft flush   chain nomTable nomChaine
    nft rename  chain nomTable nomChaine nouveauNomChaine

        # -- la priorité la plus basse est la plus prioritaire
        # -- il peut y avoir des priorités négatives
        # -- une priorité négative est prioritaire par rapport à une priorité égale à 0.



    # -- Rules
    nft add     rule nomTable nomChain nomHandle index I
    nft replace rule nomTable nomChain
    nft delete  rule nomTable nomChain

    # -- ruleset
    nft list ruleset Family
    nft flush ruleset Family
    nft export ruleset Family

exemple :

    -- ajout Table
    nft add table inet filter

    -- ajout chaîne
    nft add chain inet filter input { type filter hook input priority 0 \; }
    nft add chain inet filter output { type filter hook output priority 0 \; }

    -- ajout rules
    nft add rule inet filter input tcp dport 80 accept
    nft add rule inet filter input tcp dport 443 accept
    nft add rule inet filter input tcp dport 50702 accept
    nft add rule inet filter input drop

    nft add rule inet filter output tcp sport 80 accept
    nft add rule inet filter output tcp sport 443 accept
    nft add rule inet filter output tcp sport 50702 accept
    nft add rule inet filter output drop




------ bannir une adresse IP
    nft add rule filter input ip saddr 192.168.10.1 drop

------ ICMP
    nft add rule inet filter input meta nfproto ipv4 icmp type { echo-request } counter accept
    nft add rule inet filter input meta nfproto ipv6 icmpv6 type echo-request counter accept



-------- diverses commandes
    nft list tables ip6     -- liste les tables dont la famille est ip V6
    nft list tables ip      -- liste les tables dont la famille est ip v4
    nft list tables inet    -- liste les tables dont la famille est ip V6 ou ipV4

    nft flush  table ip6 mon_filtreIPv6                 -- supprime toutes les chaînes qui sont dans la table
    nft delete table ip6 mon_filtreIPv6                 -- supprime la table seulement si elle est vide (il faut donc la flusher avant !)
    nft list ruleset -a                                 -- permet de voir les rules avec leur handles
    nft delete rule inet monFiltreIP output handle 10   -- supprime la rule qui a pour handle 10

    -- chaine














nft


Family
    - ip (ipv4)
    - ip6
    - inet (ipv4 oi ipv6)
    - arp
    - bridge
    - netdev

TypeHook
    - prerouting
    - input
    - forward
    - output
    - postrouting








-- ===== historique
avec le noyau





- attention : nft est dans /sbin, qui n'est pas dans le path
- il y 3 façons de

--

nft flush ruleset : Clear the whole ruleset
nft list ruleset  : permet de voir les regles en cours
nft list tables   :

nft add table inet tableFilter


-- les tables


-- == une ou plusieurs interfaces

