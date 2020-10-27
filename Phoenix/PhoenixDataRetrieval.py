### Phoenix Data Retrieval API Call ###

from keys import q_key
from requests import get
import pandas as pd
import json
import numpy as np 

cityCode = 38060
response = get(f'https://www.quandl.com/api/v3/datasets/FMAC/HPI_{cityCode}')
cityObj = dict(response.json())['dataset']
startDate = cityObj['start_date']
endDate = cityObj['end_date']
indexTable = cityObj['data']
print('Data Range: '+ str(startDate) + ' -- ' + str(endDate))
# not sure if this will work to create dataframe
DF = pd.DataFrame(np.array(indexTable),columns=['date', 'nsa', 'sa'])
print(DF)
##Below is for writing data to a text file so the console does not overflow
#data = data['datatable']['data']
#with open('text.txt', 'w') as file:
    #file.write(str(indexTable))
    
DF.to_csv('Phoenix_House_Data')
PhoenixCSV = pd.read_csv('Phoenix_House_Data')
print(PhoenixCSV)
