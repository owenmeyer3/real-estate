from importingCSVs import cityCodes
from getCityData import indicesDict, areaCodes, USIndexDF
import matplotlib.pyplot as plt
#import pandas as pd

####plot date vs. sa for select city
#Choose city
for areaCodeForPlot in areaCodes:
    #get dataframe for city
    plotDF = indicesDict[str(areaCodeForPlot)]
    cityName = cityCodes[cityCodes['area_code'] == areaCodeForPlot]['city_string'].values[0]

    cityUSDF = plotDF.merge(USIndexDF, on='date')
    cityUSDF['sa'] = cityUSDF['sa_x'] - cityUSDF['sa_y']
    cityUSDF.rename(columns = {'sa_x':'sa_city', 'sa_y':'sa_US', 'sa':'sa_city-US'}, inplace = True)
    #set x, y arrays and plot for city
    x1 = cityUSDF['date'].values
    y1 = cityUSDF['sa_city'].values
    plt.plot(x1,y1, label = cityName)

    #set x, y arrays and plot for US
    x2 = cityUSDF['date'].values
    y2 = cityUSDF['sa_US'].values
    plt.plot(x2,y2, label = 'US')

    #set x, y arrays and plot for city - US
    x3 = cityUSDF['date'].values
    y3 = cityUSDF['sa_city-US'].values
    plt.plot(x3,y3, label = 'difference ( city - US)')

    #set labels
    plt.title(cityName)
    plt.xlabel('Date')
    plt.ylabel("SA Index")
    #show plot
    plt.legend()
    plt.savefig('cityPlots/' + cityName + '_plot.png')

