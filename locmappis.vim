set spell spelllang=de

imap ,eq \begin{equation*}<CR>\end{equation*}<esc>O
imap ,bbm \begin{bmatrix}<CR>\end{bmatrix}<esc>O

imap mbx \mathbf x
imap mby \mathbf y

map ,m <esc>:w<CR>:!./mkdc.sh<CR>


