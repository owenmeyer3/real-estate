from importingCSVs import city_mergeDF
from keys import quandlekey
from requests import get
import pandas as pd
import json
import numpy as np 

##This file querys the FMAC api for SA Index values for cities and the USA as a whole

#create empty dictionary to hold sa/nsa indices for all cities
indicesDict = {}

#get unique area codes for included cities (to inject into query string)
areaCodes = city_mergeDF['area_code'].unique()


for areaCode in areaCodes:
    #query city data for each city and put in dataframe
    try:
        cityResponse = get(f'https://www.quandl.com/api/v3/datasets/FMAC/HPI_{areaCode}?api_key={quandlekey}')
    except:
        print('FMAC Area Code ' + str(areaCode) + ' query failed')
    cityObj = dict(cityResponse.json())['dataset']
    cityIndexTable = cityObj['data']
    cityIndexDF = pd.DataFrame(np.array(cityIndexTable), columns = ['date', 'nsa', 'sa'])
    #reformat columns
    cityIndexDF['date'] = pd.to_datetime(cityIndexDF['date'])
    cityIndexDF['nsa'] = cityIndexDF['nsa'].astype(float)
    cityIndexDF['sa'] = cityIndexDF['sa'].astype(float)
    #sort DF by date, remove nsa, and add to dictionary {key = FMAC area code: value = SA Index DF for area code}
    cityIndexDF = cityIndexDF.sort_values('date', ascending = True)
    indicesDict[str(areaCode)]=cityIndexDF[['date', 'sa']]

#query US Data and put in dataframe
try:
    USResponse = get(f'https://www.quandl.com/api/v3/datasets/FMAC/HPI_USA?api_key={quandlekey}')
except:
    print('FMAC US query failed')
USObj = dict(USResponse.json())['dataset']
USIndexTable = USObj['data']
USIndexDF = pd.DataFrame(np.array(USIndexTable), columns = ['date', 'nsa', 'sa'])
#reformat columns
USIndexDF['date'] = pd.to_datetime(USIndexDF['date'])
USIndexDF['nsa'] = USIndexDF['nsa'].astype(float)
USIndexDF['sa'] = USIndexDF['sa'].astype(float)
#sort DF by date and remove nsa
USIndexDF = USIndexDF.sort_values('date', ascending = True)
USIndexDF=USIndexDF[['date', 'sa']]