### Phoenix Data Retrieval API Call ###

from importingCSVs import city_mergeDF
from keys import quandlekey
from requests import get
import pandas as pd
import json
import numpy as np 


print(city_mergeDF)

resultsDict = {}

cityCodes = city_mergeDF['area_code'].unique()
#print(cityCodes)

for cityCode in cityCodes:
    
    response = get(f'https://www.quandl.com/api/v3/datasets/FMAC/HPI_{cityCode}?api_key={quandlekey}')
    cityObj = dict(response.json())['dataset']
    indexTable = cityObj['data']
    # not sure if this will work to create dataframe
    resultsDict[str(cityCode)]=indexTable
print(resultsDict['41180'])          
          
          
    DF = pd.DataFrame(np.array(indexTable),columns=['date', 'nsa', 'sa'])
    print(DF)
    ##Below is for writing data to a text file so the console does not overflow
    #data = data['datatable']['data']
    #with open('text.txt', 'w') as file:
        #file.write(str(indexTable))
        
    DF.to_csv('Phoenix_House_Data')
    PhoenixCSV = pd.read_csv('Phoenix_House_Data')
    print(PhoenixCSV)
