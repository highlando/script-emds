# R -e 'install.packages("kableExtra")'
# R -e 'install.packages("bookdown")'

Rscript -e 'bookdown::render_book("index.md", "bookdown::pdf_book", quiet=FALSE)'
# Rscript -e 'bookdown::render_book("index.md", "bookdown::gitbook", quiet=FALSE)'