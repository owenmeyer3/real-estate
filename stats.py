from importingCSVs import cityCodes
from getCityData import areaCodes
from plot import saDiffDict

#get dataframe for city
areaCode = areaCodes[0]
statsDF = saDiffDict[str(areaCode)]
cityName = cityCodes[cityCodes['area_code'] == areaCode]['city_string'].values[0]
mean = statsDF['sa_city-US'].mean()
std = statsDF['sa_city-US'].std()
print('mean:' + str(mean))
print('stfd: ' + str(std))