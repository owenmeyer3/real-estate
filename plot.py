from importingCSVs import cityCodes
from getCityData import indicesDict, areaCodes
import matplotlib.pyplot as plt
#import pandas as pd

####plot date vs. sa for select city
#Choose city
areaCodeForPlot = areaCodes[0]
#get dataframe for city
plotDF = indicesDict[str(areaCodeForPlot)]
#set x, y arrays and plot
x = plotDF['date'].values
y = plotDF['sa'].values
plt.plot(x,y)
#set labels
title = cityCodes[cityCodes['area_code'] == areaCodeForPlot]['city_string'].values[0]
plt.title(title)
plt.xlabel('Date')
plt.ylabel("SA Index")
#show plot
plt.show()

