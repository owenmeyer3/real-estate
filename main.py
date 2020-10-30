from importingCSVs import cityCodes
from getCityData import indicesDict, areaCodes, USIndexDF
import matplotlib.pyplot as plt
from scipy import stats

### This file is used to:
###### find the 0.95 statistical significance x-value
###### on 1 plot:
######### SA Index for a city as a timeseries
######### SA Index for the USA as a timeseries
######### SA Index for a city minus SA Index for the USA as a timeseries
######### 0.95 statistical significance x-value for SA Index for a city minus SA Index for the USA as a timeseries

### We use the 0.95 statistical significance line to visually compare which date the city - US line has a significant high value.
### We can see if these dates occur shortly after teams were established in the city

##Loop: plot date vs. sa (city, US and city - US) for select city
#Choose city
for areaCode in areaCodes:
    #get dataframe for city
    plotDF = indicesDict[str(areaCode)]
    cityName = cityCodes[cityCodes['area_code'] == areaCode]['city_string'].values[0]

    #make dataframe comparing city and US sa indices
    cityUSDF = plotDF.merge(USIndexDF, on='date')
    cityUSDF['sa'] = cityUSDF['sa_x'] - cityUSDF['sa_y']
    cityUSDF.rename(columns = {'sa_x':'sa_city', 'sa_y':'sa_US', 'sa':'sa_city-US'}, inplace = True)

    #find 0.95 sample limit
    mean = cityUSDF['sa_city-US'].mean()
    std = cityUSDF['sa_city-US'].std()
    t_95 = stats.norm.ppf(0.95, loc = 0, scale = 1)
    x_95 = t_95*std + mean
    x_min = cityUSDF['date'].min()
    x_max = cityUSDF['date'].max()
    plt.hlines(x_95, x_min, x_max, 'k', label = '0.95 significance limit')

    #set x, y arrays and plot for city
    x1 = cityUSDF['date'].values
    y1 = cityUSDF['sa_city'].values
    plt.plot(x1,y1, 'b', label = cityName)

    #set x, y arrays and plot for US
    x2 = cityUSDF['date'].values
    y2 = cityUSDF['sa_US'].values
    plt.plot(x2,y2, 'r', label = 'US')

    #set x, y arrays and plot for city - US
    x3 = cityUSDF['date'].values
    y3 = cityUSDF['sa_city-US'].values
    plt.plot(x3,y3, 'g', label = 'difference ( city - US)')

    #set labels
    plt.title(cityName)
    plt.xlabel('Date')
    plt.ylabel("SA Index")

    #show plot
    plt.legend()
    plt.savefig('cityPlots/' + cityName + '_plot.png')
    plt.clf()

