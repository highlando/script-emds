# R -e 'install.packages("kableExtra")'
# R -e 'install.packages("bookdown")'

Rscript -e 'bookdown::render_book("index.Rmd", "bookdown::pdf_book", quiet=FALSE)'
# Rscript -e 'bookdown::render_book("index.Rmd", "bookdown::gitbook", quiet=FALSE)'

# pdftk docs/EMDS.pdf cat 7 9 11 12 19 output formelsammlung.pdf
