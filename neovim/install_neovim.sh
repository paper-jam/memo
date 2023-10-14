#-- ======== install neovim
sudo apt-get install fuse
sudo modprobe fuse
user="$(whoami)"
sudo groupadd fuse
sudo usermod -a -G fuse $user

cd /usr/local/bin
sudo apt install curl
sudo curl -LO https://github.com/neovim/neovim/releases/download/nightly/nvim.appimage
sudo chmod +007 nvim.appimage
sudo ln -s /usr/local/bin/nvim.appimage /usr/bin/vi
curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

sudo apt install python3-dev python3-pip curl exuberant-ctags git ack-grep
sudo pip3 install neovim pep8 flake8 pyflakes pylint isort



#-- ========= NEOVIM
sudo apt-get install neovim
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
sudo pip3 install jedi
# recopier le fichier init.vim dans ~/.config/nvim/init.vim


# -- ===== LUA
require('plugins.telescope') 	// loadding modules
require "telescope.builtin".find_files({}) // parenthèses optionnelles
name:match('ben')				// eq  : string.match('name','ben')

-- variables 
vim.g.nameVariable = 'i am a global variable'
vim.t.nameVariable = 'i am a tabpage variable'
vim.w.nameVariable = 'i am a window variable'
vim.b.nameVariable = 'i am a buffer variable'

-- 3 types of configurations options
vim.o. ... 		// global options 
vim.wo. ... 	// window option 
vim.bo. ... 	// buffer optionnelles





-- divers
vim : set autoindent/noautoindent
lua : vim.opt.autoindent = true
      vim.opt.shiftwitdh = 2

-- keymaps
vim -> nnoremap (normal mode ), inoremap (insertmode), vnoremap (visual mode)
lua -> vim.api.nvim_set_keymap('n', '<leader>ff', ':lua require('telascope.builtin').
	find_files()<cr>', {noremap = true})

-- help
help telescope.builtin
helpgrep directory (serach in the entire runtime doc) 
	cnext,  cprev to navigate
www.discourse.neovim.io

vim.opt.formatoptions.append('jnrql')



# ------ init.lua sample
https://github.com/wincent/wincent/blob/main/aspects/nvim/files/.config/nvim/init.lua

# ----- bon youtuber : https://www.youtube.com/channel/UCs5oIDq24BgBQN5tl2IcHOg

-- nvim-lsp-installer
https://github.com/williamboman/nvim-lsp-installer



[nvim-lsp-installer] /usr/local/bin/neovim/share/nvim/runtime/lua/vim/uri.lua:62: attempt to index local 'path' (a nil value)




# -- ===== best plugins to use
0:25 brew install neovim
0:40 No more Vimscript
2:25 Treesitter and syntax highlighting ====> treesiter in neovim 0.7
3:33 Built in LSP Client
5:18 Formatter
5:43 Telescope
6:36 ThePrimeagen shoutout
7:08 Minimap
8:06 Lualine
9:06 Hop
10:16 Summary


-- configuration nvim-lsp 
https://github.com/neovim/nvim-lspconfig/wiki/Autocompletion

https://github.com/tjdevries/config_manager/tree/master/xdg_config/nvim !!!!!
