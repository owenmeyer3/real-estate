from importingCSVs import city_mergeDF
from keys import quandlekey
from requests import get
import pandas as pd
import json
import numpy as np 

#create empty dictionary to hold sa/nsa indices for all cities
indicesDict = {}

#get unique area codes for included cities
areaCodes = city_mergeDF['area_code'].unique()


for areaCode in areaCodes:
    #query city data for each city and put in dataframe
    cityResponse = get(f'https://www.quandl.com/api/v3/datasets/FMAC/HPI_{areaCode}?api_key={quandlekey}')
    cityObj = dict(cityResponse.json())['dataset']
    cityIndexTable = cityObj['data']
    cityIndexDF = pd.DataFrame(np.array(cityIndexTable), columns = ['date', 'nsa', 'sa'])
    #reformat columns
    cityIndexDF['date'] = pd.to_datetime(cityIndexDF['date'])
    cityIndexDF['nsa'] = cityIndexDF['nsa'].astype(float)
    cityIndexDF['sa'] = cityIndexDF['sa'].astype(float)
    #sort dictionary by date and add to dictionary
    cityIndexDF = cityIndexDF.sort_values('date', ascending = True)
    indicesDict[str(areaCode)]=cityIndexDF[['date', 'sa']]

#query US Data and put in dataframe
USResponse = get(f'https://www.quandl.com/api/v3/datasets/FMAC/HPI_USA?api_key={quandlekey}')
USObj = dict(USResponse.json())['dataset']
USIndexTable = USObj['data']
USIndexDF = pd.DataFrame(np.array(USIndexTable), columns = ['date', 'nsa', 'sa'])
#reformat columns
USIndexDF['date'] = pd.to_datetime(USIndexDF['date'])
USIndexDF['nsa'] = USIndexDF['nsa'].astype(float)
USIndexDF['sa'] = USIndexDF['sa'].astype(float)
#sort dictionary by date and add to dictionary
USIndexDF = USIndexDF.sort_values('date', ascending = True)
USIndexDF=USIndexDF[['date', 'sa']]