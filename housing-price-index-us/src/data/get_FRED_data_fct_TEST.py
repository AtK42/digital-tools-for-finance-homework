#import package to run code
import requests
import pandas as pd
from pandas import json_normalize
import json
import os
from datetime import date
from get_FRED_data_fct import *

#test our function
#series_id_vec = ['HPIPONM226S']
series_id_vec = ['HPIPONM226S', 'UNRATE', 'USACPIALLMINMEI', 'UMCSENT', 'PCU333120333120', 'MORTGAGE30US', 'PI', 'AAA', 'MSACSR', 'POPTHM', 'GDP', 'GNP', 'HOUST', 'LFWA64TTUSM647S', 'FIXHAI', 'USSTHPI']
frequency = 'm'
observation_start = '2000-01-01'
observation_end = '2022-06-30'
api_key = os.environ['FRED_API_KEY']
project_name = 'housing-price-index-us'
fct_call_test = get_FRED_data_fct(series_id_vec, frequency, observation_start, api_key, project_name, observation_end = observation_end)
