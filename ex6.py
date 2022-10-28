
#root url is https://api.binance.com/api/v3
#endpoint for bitcoin-usd is /klines?symbol=BTCUSDT

#import package to run code
import requests
import pandas as pd
import json
#import datetime

#create our function
def binance_super_function(currency_pair, start_date):
    base_url = "https://api.binance.com/api/v3/klines?symbol="  
    res = f'{base_url}{currency_pair}&interval=1m&limit=75&startTime={start_date}'
    print(res)
    resp = requests.get(res)
    print(resp)
    #data = pd.DataFrame.from_records(resp.json()[1][2]) #, columns=['1', "open_price", 'high_price', 'low_price', 'close_price', 'volume', 'close', 'quote', 'num', 'taker_base', 'taker_quote', 'unused'])
    #data.index = data.pop("time").map(datetime.datetime.fromtimestamp)
    #print(data)
    return resp

#test our function
ex06 = binance_super_function("BTCUSDT", "1641723048000")
print(ex06.json())

#############################################################################################################
#task 2
# 
#root url = https://api.stlouisfed.org/


#endpoint = fred/series/observations

#observation_start:
#https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&frequency=m&observation_start=2020-01-01&api_key=abc123


