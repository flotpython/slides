#
# NOTES
# playing at the same time with 2 distinct ways to produce decent handouts
# 
# * ipypublish:
#   builds in _ipypublish
# * jupyter-book
#   builds in _book
# 
# targets
# make ipypublish
# make ipypublish-clean
# make book
# make book-clean

#
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _sphinx

NOTEBOOKS = $(shell git ls-files 0*nb)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

#
ipypublish: html

ipypublish-clean: 
	rm -rf _sphinx

ipypublish-view:
	open _sphinx/html/index.html

.PHONY: ipypublish ipypublish-clean ipypublish-clean

### attempt with jupyter book - but giving up for now
book:
	jupyter book build .

book-clean:
	rm -rf _build

book-view:
	open _build/html/index.html

.PHONY: book book-clean book-clean

### all
all: book ipypublish
clean: book-clean ipypublish-clean
.PHONY: all clean


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
