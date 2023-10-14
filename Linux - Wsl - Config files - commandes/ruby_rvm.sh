#-- ============  RVM GEM
rvm list known          -- liste les versions de ruby connues
rvm list                -- liste les versions installés
rvm use 2.1 --default   -- utilise la version 2.1
rvm install 2.0.0       -- installe la version 2.0.0
rvm system              -- ??

rvm gemset create nomGemset -- créer un gemset
rvm gemset use nomGemset    -- utilise le gemset
rvm gemdir                  -- affiche $GEM_GOME, le gemset en cours
rvm gemset list             -- liste des gemset
rvm current                 -- affiche rvm en cours

#-- ============  RVM GEM
where gem                   # où est installé l éxécutable gem
gem list -la     (ou -lda)  # liste des gems installés, local, détail
gem env gemdir
gem outdated                # liste des gems périmés
gem update                  # met à jour les gems installés

#-- ========= removing RVM
sudo rm -rf $HOME/.rvm $HOME/.gem $HOME/.bundle  $HOME/.rvmrc /etc/rvmrc /etc/profile.d/rvm.sh /usr/local/rvm /usr/local/bin/rvm
sudo groupdel rvm

#   -- Please check also
sudo vi .bashrc .bash_profile
sudo vi .profile .zshrc .zlogin
sudo vi /etc/profile.d/sm.sh
sudo vi /etc/profile.d/rvm.sh
sudo vi /etc/profile
sudo apt-get remove ruby-rvm
