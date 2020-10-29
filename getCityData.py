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


for areaCode in areaCodes[0:1]:
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
    indicesDict[str(areaCode)]=cityIndexDF

