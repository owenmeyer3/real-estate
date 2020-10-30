import pandas as pd
import numpy as np

## This file reads csv data needed for the analysis

#import FMAC area codes for cities. FMAC API accesses city data by its FMAC area code
cityCodes = pd.read_csv('FMCityCodes.csv')

#Imports our csv which describes teams that we want to analyze, thier cities, and dates of move
team = pd.read_csv('team.csv')

#merge these tables on the city name (as formatted in the FMAC API) for use throughout the script
city_mergeDF = pd.merge(team, cityCodes, how = 'left', on='city_string')