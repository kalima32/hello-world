set nocompatible              " be iMproved, required
filetype off                  " required
"These edits to .vimrc were recommended by RealPython 
"https://realpython.com/vim-and-python-a-match-made-in-heaven/

"setup screen splitting
set splitbelow	              " specify screen split area below
set splitright                " specify screen split area right

"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

"Enable folding
set foldmethod=indent
set foldlevel=99
"Enable folding with the spacebar
nnoremap <space> za

"Enable Python PEP 8 indentation
au BufNewFile,BufRead *.py
    \ set tabstop=4
    \ set softtabstop=4
    \ set shiftwidth=4
    \ set textwidth=79
    \ set expandtab
    \ set autoindent
    \ set fileformat=unix

"Enable buffers for full stack development
au BufNewFile,BufRead *.js, *.html, *.css
    \ set tabstop=2
    \ set softtabstop=2
    \ set shiftwidth=2

"Enable flagging of unnecessary whitespaces
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

"Set encoding to UTF-8
set encoding=utf-8

"Plugin modifications SimpylFold
let g:SimpylFold_docstring_preview=1
"Plugin modification YouCompleteMe
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

"Setup virtualenv for vim
"python with virtualenv support
py << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
  project_base_dir = os.environ['VIRTUAL_ENV']
  activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
  execfile(activate_this, dict(__file__=activate_this))
EOF

"This is for cleaning up code and making it look good
let python_highlight_all=1
syntax on

"This addes logic to set colorscheme based on running mode
if has('gui_running')
  set background=dark
  colorscheme solarized
  "Add color scheme toggle from dark to light with F5 for Solarized
  call togglebg#map("<F5>")
else
  set t_Co=256
  colorscheme zenburn
endif

"This turns line numbers on by default
set nu

"Allow copy/paste in and out of vim
set clipboard=unnamed

"This is end of edits from RealPython

"This setup was found at https://shapeshed.com/vim-netrw/
"It will give you a nerdtree like file explorer view with the native netrw
"file browser that comes with vim
let g:netrw_banner = 0
let g:netrw_liststyle = 3
let g:netrw_browse_split = 4
let g:netrw_altv = 1
let g:netrw_winsize = 25
augroup ProjectDrawer
  autocmd!
  autocmd VimEnter * :Vexplore
augroup END

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/fugitive'

" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'

" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'

" git repos on your local machine (i.e. when working on your own plugin)
" Plugin 'file:///home/gmarik/path/to/plugin'

" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}

" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}

"This plugin is for python code folding from RealPython
Plugin 'SimpylFold'

"This plugin is for python autoindenting from RealPython
Plugin 'vim-scripts/indentpython.vim'

"This plugin is for python code completion from RealPython
Plugin 'Valloric/YouCompleteMe'

"This plugin does syntax checking from RealPython
Plugin 'vim-syntastic/syntastic'

"This plugin adds PEP 8 syntax checking from RealPython
Plugin 'nvie/vim-flake8'

"This plugin adds color mark-up for GUI mode from RealPython
Plugin 'altercation/vim-colors-solarized'

"This plugin adds color mark-up for terminal mode from RealPython
Plugin 'jnurmine/Zenburn'

"This plugin allows searching for things from vim from RealPython
Plugin 'kien/ctrlp.vim'

"This plugin allows git integration into vim from RealPython
Plugin 'tpope/vim-fugitive'

"This plugin configures the powerline status bar from RealPython
"Docs are found here http://powerline.readthedocs.io/en/latest/
"Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line