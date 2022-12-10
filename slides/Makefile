all: book

include Makefile.book

include Makefile.style

# not used yet, but well
include Makefile.norm

### NOTE
# requires
# pip install pyppeteer

pdf-clean:
	rm -rf _build/pdf

pdf-view:
	open _build/pdf/book.pdf

.PHONY: pdf pdf-clean pdf-clean
