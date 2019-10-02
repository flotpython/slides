# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/minimal-notebook


# --------
# auto-evaluated exercices & ipythontutor magic
RUN pip install nbautoeval ipythontutor


# --------
# install jupyter extensions and enable the one about split cells
# to find out an extension's name
# look in the console in a jupyter that has it enabled
RUN jupyter nbextension enable splitcell/splitcell


# install rise
RUN pip install --pre rise


# --------
# a decent stack
RUN pip install numpy pandas matplotlib ipywidgets 

RUN pip install mpld3 bokeh plotly folium vispy seaborn pygal networkx mypy

# graphviz
RUN apt-get install -y graphviz && pip install graphviz

### speed up jupyter lab startup
RUN jupyter lab build
