# targets
# make html			(for html)
# make html-clean
# make pdf			(for pdf)
# make pdf-clean

###
html:
	jupyter-book build .

html-clean:
	rm -rf _build/html

html-view:
	open _build/html/index.html

.PHONY: html html-clean html-clean



### NOTE
# requires
# pip install pyppeteer

requirements:
	pip install pyppeteer

pdf:
	jupyter-book build ./ --builder pdfhtml

pdf-clean:
	rm -rf _build/pdf

pdf-view:
	open _build/pdf/book.pdf

.PHONY: pdf pdf-clean pdf-clean
