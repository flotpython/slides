# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/minimal-notebook

# NOTE
# removing pip install keplergl because it forces a downgrade of
# ipywidgets to 7.x, which is not compatible with ipythontutor
# also I am removing jupyterlab-rise from the mix for now -
# and probably for good...
RUN true \
 && pip install jupyterlab notebook jupytext jupyterlab-myst \
 && pip install jupyterlab-courselevels jupyterlab-gridwidth \
 && pip install nbautoeval ipythontutor \
 && pip install numpy pandas matplotlib ipywidgets \
 && pip install mpld3 bokeh jupyter-bokeh plotly folium \
 && pip install vispy seaborn pygal networkx mypy autograd k3d \
 && apt-get install -y graphviz && pip install graphviz \
 && pip install geopandas \
 && pip install scikit-learn \
 && true
