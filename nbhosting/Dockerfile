# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/minimal-notebook

# NOTE
# we cannot use jupyter nbextension enable/disable
# because we provide our own nbconfig/notebook.json
# and that is where is stored the enabled/disabled extensions
RUN true \
 && jupyter nbextension enable hide_input/main \
 && pip install -U nb-courselevels \
 && pip install -U nbautoeval \
 && pip install -U ipythontutor \
 && pip install rise --pre \
 && pip install numpy pandas matplotlib ipywidgets \
 && pip install mpld3 bokeh plotly folium vispy seaborn pygal networkx mypy autograd k3d \
 && apt-get install -y graphviz && pip install graphviz \
 && pip install geopandas keplergl \
 && true
