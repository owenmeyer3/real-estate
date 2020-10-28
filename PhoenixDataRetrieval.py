### Phoenix Data Retrieval API Call ###

from importingCSVs import city_mergeDF
#from keys import q_key
from requests import get
import pandas as pd
import json
import numpy as np 


print(city_mergeDF)

resultsDict = {}

for row in city_mergeDF[0:4]:
    
    cityCode = row['area_code']
    response = get(f'https://www.quandl.com/api/v3/datasets/FMAC/HPI_{cityCode}')
    cityObj = dict(response.json())['dataset']
    indexTable = cityObj['data']
    # not sure if this will work to create dataframe
    resultsDict.append({str(row['team'], row['first_year']):indexTable}
    print(json.dumps(resultsDict))
          
          
          
    DF = pd.DataFrame(np.array(indexTable),columns=['date', 'nsa', 'sa'])
    print(DF)
    ##Below is for writing data to a text file so the console does not overflow
    #data = data['datatable']['data']
    #with open('text.txt', 'w') as file:
        #file.write(str(indexTable))
        
    DF.to_csv('Phoenix_House_Data')
    PhoenixCSV = pd.read_csv('Phoenix_House_Data')
    print(PhoenixCSV)
