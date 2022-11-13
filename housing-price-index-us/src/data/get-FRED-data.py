#import package to run code
import requests
import pandas as pd
import json
import os
#import datetime

#create function
def get_FRED_data(series_id, frequency, observation_start, api_key, file_type = 'json'):
# series_id is the name of the series
# # purchase only house price index (monthly): HPIPONM226S
# # unemployment rate (monthly): UNRATE
# # consumer price index (monthly): USACPIALLMINMEI
# # consumer sentiment (monthly): UMCSENT
# # producer price index construction machinery manufacturing (monthly): PCU333120333120
# # inflation rate US (monthly): T10YIEM
# # average mortgage interest (weekly): MORTGAGE30US
# # personla income (monthly): PI
# # moody's seasoned aaa corporate bond yield (monthly): AAA
# # home supply (monthly): MSACSR
# frequency can be 'd' for daily, 'm' for monthly, 'y' for yearly
# observation_start is the first day for which the series should be fetched, format 'yyyy-mm-dd'
# api_key is the api key that can be generated on the FRED website

    base_url = "https://api.stlouisfed.org/fred/series/observations?"
    complete_url = f'{base_url}series_id={series_id}&frequency={frequency}&observation_start={observation_start}&api_key={api_key}&file_type={file_type}'

    resp = requests.get(complete_url)
    print(resp)
    #data = pd.DataFrame.from_records(resp.json()[1][2]) #, columns=['1', "open_price", 'high_price', 'low_price', 'close_price', 'volume', 'close', 'quote', 'num', 'taker_base', 'taker_quote', 'unused'])
    #data.index = data.pop("time").map(datetime.datetime.fromtimestamp)
    #print(data)
    return resp

#test our function
series_id = 'HPIPONM226S'
frequency = 'm'
observation_start = '2000-01-01'
api_key = os.environ['FRED_API_KEY']
fct_call_test = get_FRED_data(series_id, frequency, observation_start, api_key)
#print(fct_call_test.json())

df = pd.read_json(fct_call_test, orient = 'index')


