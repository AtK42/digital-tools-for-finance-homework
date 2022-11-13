def get_FRED_data_fct(series_id, frequency, observation_start, api_key, file_type = 'json'):
# series_id is the name of the series
# # purchase only house price index (monthly): HPIPONM226S
# # unemployment rate (monthly): UNRATE
# # consumer price index (monthly): USACPIALLMINMEI
# # consumer sentiment (monthly): UMCSENT
# # producer price index construction machinery manufacturing (monthly): PCU333120333120
# # inflation rate US (monthly): T10YIEM !! same as cpi -> multicollinearity !!
# # average mortgage interest (weekly): MORTGAGE30US
# # personla income (monthly): PI
# # moody's seasoned aaa corporate bond yield (monthly): AAA
# # home supply (monthly): MSACSR
# frequency can be 'd' for daily, 'm' for monthly, 'y' for yearly
# observation_start is the first day for which the series should be fetched, format 'yyyy-mm-dd'
# api_key is the api key that can be generated on the FRED website

    import requests

    # cat all data needed for api call
    base_url = "https://api.stlouisfed.org/fred/series/observations?"
    complete_url = f'{base_url}series_id={series_id}&frequency={frequency}&observation_start={observation_start}&api_key={api_key}&file_type={file_type}'

    # make api call and print the response (only number code)
    resp = requests.get(complete_url)
    print(resp)

    # return the result of the api get request
    return resp