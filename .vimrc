" Установка основных параметров
syntax on
set number
set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set smartindent

" Подсветка синтаксиса для Python
au BufNewFile,BufRead *.py set filetype=python

" Подсветка синтаксиса для HTML и CSS
au BufNewFile,BufRead *.html set filetype=html
au BufNewFile,BufRead *.css set filetype=css

" Установка темы
colorscheme desert

" Плагины
" Установка менеджера плагинов Vundle (если он еще не установлен)
if empty(glob('~/.vim/bundle/Vundle.vim'))
    silent !mkdir -p ~/.vim/bundle
    silent !git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
endif

" Список плагинов
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'vim-python/python-syntax'
Plugin 'pangloss/vim-javascript'
Plugin 'mxw/vim-jsx'
Plugin 'mattn/emmet-vim'
Plugin 'scrooloose/nerdtree'
Plugin 'tpope/vim-surround'
Plugin 'tpope/vim-commentary'
call vundle#end()

" Активация плагинов
filetype plugin indent on

" Настройки плагинов
" NERDTree
map <C-n> :NERDTreeToggle<CR>
let NERDTreeShowHidden=1

" Emmet
let g:user_emmet_leader_key='<C-e>'

" Дополнительные настройки
set mouse=a
set hlsearch
set incsearch
set ignorecase
set smartcase

