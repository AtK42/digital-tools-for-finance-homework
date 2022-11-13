#import package to run code
import requests
import pandas as pd
from pandas import json_normalize
import json
import os

from get_FRED_data_fct import *

#test our function
series_id = 'HPIPONM226S'
frequency = 'm'
observation_start = '2000-01-01'
api_key = os.environ['FRED_API_KEY']
fct_call_test = get_FRED_data_fct(series_id, frequency, observation_start, api_key)
#print(fct_call_test.json())

# converting api response from json to pandas dataframe
# see https://deallen7.medium.com/how-to-create-a-pandas-dataframe-from-an-api-endpoint-in-a-jupyter-notebook-f2561f766ca3
json = fct_call_test.json()
print(json.keys())
#print(json['observations'])
#print(type(json['observations'][0]))
df = pd.DataFrame(json['observations'])
df = df.iloc[:, 2:]
print(df.head(5))