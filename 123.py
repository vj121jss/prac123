'''
from matplotlib import pyplot as plt
from bokeh.io import curdoc
import seaborn as sb
import pandas as pd
newdf = pd.DataFrame({"Datum": ['1/1/2018 0:00',
                             '1/1/2018 0:15',
                             '1/1/2018 0:30',
                             '1/1/2018 0:45',
                             '1/1/2018 1:00',
                             '1/1/2018 1:15',
                             '1/1/2018 1:30',
                             '1/1/2018 1:45 '],
                   "Menge": [19.5, 19.,19.5,19.5,21,19.5,20,23]})
sb.lineplot(x="Datum", y="Menge", data=newdf)
plt.xticks(rotation=15)
plt.title('seaborn-matplotlib example')
s=plt
curdoc().add_root(s)
#plt.show()
'''
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.io import curdoc
output_file("area.html")
p = figure(plot_width=400, plot_height=400)

p.varea(x=[1, 2, 3, 4, 5],
        y1=[4, 5, 1, 2, 7],
        y2=[1, 4, 2, 2, 3])
curdoc().add_root(p)
#show(p)





