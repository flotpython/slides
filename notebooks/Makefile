include Makefile.book
include Makefile.style

# should work now
NOTEBOOKS = [0-9]*.py
NBNORMFLAGS = -l1 -L Licence -s2 -S 'IPython.display' -t h1
include Makefile.norm

# derive jb toc from nbhosting
include Makefile.toc

### NOTE
# requires
# pip install pyppeteer

pdf-clean:
	rm -rf _build/pdf

pdf-view:
	open _build/pdf/book.pdf

.PHONY: pdf pdf-clean pdf-clean
