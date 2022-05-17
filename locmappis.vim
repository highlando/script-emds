set spell spelllang=de

imap ,eq \begin{equation*}<CR>\end{equation*}<esc>O
imap ,bbm \begin{bmatrix}<CR>\end{bmatrix}<esc>O
imap ,rr \mathbb R^{}

imap mbx \mathbb x
imap mby \mathbb y

map ,m <esc>:w<CR>:!./mkdc.sh<CR>
