import numpy as np
from bokeh.plotting import figure
from bokeh.layouts import layout
from bokeh.models import (HoverTool, Slider, ColumnDataSource)
from bokeh.io import curdoc


n = 10000
x = np.linspace(1, 100, n)
y = 2*np.log(x) + np.random.rand(n) - 0.5

# Compute 2d histogram. Note the order of x/y and xedges/yedges
H, yedges, xedges = np.histogram2d(y, x, bins=(5,7))

# Compute coordinates at the center of the grid
Xs = (xedges[:-1]+xedges[1:])/2
Ys = (yedges[:-1]+yedges[1:])/2

# Flatten and normalize the histogram data
HH = H.flatten()
HH = HH/np.linalg.norm(HH)

# Create a linear combiination of x and y coordinates
YY = np.repeat(Ys,len(Xs))
XX = np.tile(Xs,len(Ys))

# Define plot properties
plot = figure(
    x_range=(xedges[0], xedges[-1]),
    y_range=(yedges[0], yedges[-1]),
    title='Interactive bubble heatmap',
    height=300
)

# Circle plot
c = plot.circle(
    x=XX,
    y=YY,
    size=HH,
)

# Add plot tooltip
plot.add_tools(HoverTool(tooltips="X: @x</br>Y: @y</br>probability: @size", show_arrow=True, point_policy='follow_mouse'))
    
# Reference to datasource
ds = c.data_source

def slider_callback(attr, old, new):
    # lay.children[1] = create_figure(slider.value)
    new_data = dict()
    new_data['x'] = ds.data['x']
    new_data['y'] = ds.data['y']
    new_data['size'] = HH*slider.value
    ds.data = new_data

def modify_doc(doc): 
    doc.add_root(lay)


slider = Slider(
    start = 1,
    end = 100,
    value = 1
)

slider.on_change('value', slider_callback)

lay = layout([slider],[plot])

curdoc().add_root(lay)

# EOF
