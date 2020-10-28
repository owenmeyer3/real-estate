from keys import quandlekey
from requests import get
import pandas as pd
import numpy as np
import json

cityCode = 11700
response = get(f'https://www.quandl.com/api/v3/datasets/FMAC/HPI_{cityCode}?api_key={quandlekey}')
cityObj = dict(response.json())['dataset']
startDate = cityObj['start_date']
endDate = cityObj['end_date']
indexTable = cityObj['data']
print('Data Range: '+ str(startDate) + ' -- ' + str(endDate))

DF = pd.DataFrame(np.array(indexTable),columns=['date', 'nsa', 'sa'])

print(DF)

#data = data['datatable']['data']

#with open('text.txt', 'w') as file:
    #file.write(str(indexTable))
