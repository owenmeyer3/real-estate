
import pandas as pd
import numpy as np

cityCodes = pd.read_csv('FMCityCodes.csv')

team = pd.read_csv('team.csv')

city_mergeDF = pd.merge(team, cityCodes, how = 'left', on='city_string')

