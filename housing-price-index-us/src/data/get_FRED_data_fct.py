from datetime import date
def get_FRED_data_fct(series_id_list: list, frequency, observation_start, api_key, project_name, observation_end = date.today()):
# requires the import of date module of package datetime

# series_id_list: a list with the names of the series
    # # purchase only house price index (monthly): HPIPONM226S
    # # unemployment rate (monthly): UNRATE
    # # consumer price index (monthly): USACPIALLMINMEI
    # # inflation rate US (monthly): T10YIEM
    # # consumer sentiment (monthly): UMCSENT
    # # producer price index construction machinery manufacturing (monthly): PCU333120333120
    # # average mortgage interest (weekly): MORTGAGE30US
    # # personla income (monthly): PI
    # # moody's seasoned aaa corporate bond yield (monthly): AAA
    # # home supply (monthly): MSACSR
# frequency: can be 'd' for daily, 'm' for monthly, 'y' for yearly
# observation_start: the first day for which the series should be fetched, format 'yyyy-mm-dd'
# api_key: api key for FRED
# project_name: name of your project
# observation_end (optional): the last day for which the series should be fetched, format 'yyyy-mm-dd'
# file_type (optional)

    import requests
    import pandas as pd
    import json
    import os

    if not isinstance(series_id_list, list):
        raise TypeError

    for series_id in series_id_list:

        # cat all data needed for api call
        base_url = "https://api.stlouisfed.org/fred/series/observations?"
        complete_url = f'{base_url}series_id={series_id}&frequency={frequency}&observation_start={observation_start}&observation_end={observation_end}&api_key={api_key}&file_type=json'
        #print(complete_url)

        # make api call and print the response (only number code)
        resp = requests.get(complete_url)
        print(resp)

        # converting api response from json to pandas dataframe
        # see https://deallen7.medium.com/how-to-create-a-pandas-dataframe-from-an-api-endpoint-in-a-jupyter-notebook-f2561f766ca3
        json_resp = resp.json()

        # print keys
        #print(json.keys())

        # convert to pd.DF
        df = pd.DataFrame(json_resp['observations']) # check that the key is always called 'observations'
        df = df.iloc[:, 2:]
        #print(df.head(5))

        # save data to ..housing-price-index-us\data\raw
        save_folder = os.path.join(os.environ['RESEARCH_PATH'], project_name, 'data', 'raw')

        # set file name (differentiate whether observation_end argument had been passed to function)
        if 'observation_end' in locals():
            save_filename = f'data_{series_id}_{observation_start}_to_{observation_end}.feather'
        else:
            today = date.today()
            save_filename = f'data_{series_id}_{observation_start}_to_{today}.feather'

        # save data as .feather to above defined location
        save_path = os.path.join(save_folder, save_filename)
        df.to_feather(save_path)

        # return the result of the api get request
        #return resp