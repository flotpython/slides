# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/minimal-notebook

# already in nbhosting image

# --------
# a decent stack
RUN true \\
 && pip install numpy pandas matplotlib ipywidgets \\
 && pip install mpld3 bokeh plotly folium vispy seaborn pygal networkx mypy autograd k3d \\
 && apt-get install -y graphviz && pip install graphviz \\
 && pip install geopandas keplergl \\
 && true
