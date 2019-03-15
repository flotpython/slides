NOTEBOOKS = $(wildcard **.ipynb)

NORM = $(HOME)/git/flotpython-tools/tools/nbnorm.py
# these are NOT slides, so let's not enable rise autolaunch and the like
NORM-OPTIONS = --author "Thierry Parmentelat" --author "Arnaud Legout"

norm normalize:
	$(NORM) $(NORM-OPTIONS) $(NOTEBOOKS)

lsnb:
	@ls $(NOTEBOOKS)
