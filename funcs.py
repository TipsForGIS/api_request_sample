import os
import sys
import requests
import pandas as pd
from pandas.api.types import is_numeric_dtype

####################
##hepler functions##
####################

# parse response for temperature API
def _parse_temp_resp(x,y):

    api_key = os.environ['OWM_API_KEY']
    temp_url = 'https://api.openweathermap.org/data/2.5/onecall'
    full_url = '{}?lon={}&lat={}&appid={}&units=metric'.format(temp_url,x,y,api_key)
    resp_dict = requests.get(full_url).json()

    temp = round(resp_dict['current']['temp'],2)
    humidity = round(resp_dict['current']['humidity'],2)
    uvi = round(resp_dict['current']['uvi'],2)
    clouds = round(resp_dict['current']['clouds'],2)
    wind_speed = round(resp_dict['current']['wind_speed'],2)
    wind_deg = round(resp_dict['current']['wind_deg'],2)
    
    return temp, humidity, uvi, clouds, wind_speed, wind_deg

# parse response for pollution API
def _parse_polt_resp(x,y):

    api_key = os.environ['OWM_API_KEY']
    polt_url = 'http://api.openweathermap.org/data/2.5/air_pollution'
    full_url = '{}?lon={}&lat={}&appid={}&units=metric'.format(polt_url,x,y,api_key)
    resp_dict = requests.get(full_url).json()

    co = round(resp_dict['list'][0]['components']['co'],2)
    no = round(resp_dict['list'][0]['components']['no'],2)
    no2 = round(resp_dict['list'][0]['components']['no2'],2)
    o3 = round(resp_dict['list'][0]['components']['o3'],2)
    so2 = round(resp_dict['list'][0]['components']['so2'],2)
    pm2_5 = round(resp_dict['list'][0]['components']['pm2_5'],2)
    pm10 = round(resp_dict['list'][0]['components']['pm10'],2)
    nh3 = round(resp_dict['list'][0]['components']['nh3'],2)
    
    return co, no, no2, o3, so2, pm2_5, pm10, nh3

# parse response for elevation API
def _parse_elev_resp(x,y):

    api_key = os.environ['GOOG_API_KEY']
    elev_url = 'https://maps.googleapis.com/maps/api/elevation/json'
    full_url = '{}?locations={},{}&key={}'.format(elev_url,y,x,api_key)
    resp_dict = requests.get(full_url).json()

    elv = round(resp_dict['results'][0]['elevation'],2)

    return elv


########################
##validation functions##
########################

# validate if sys argv are in format: python3 get_weather_data.py input.csv output.csv
def sys_argv_valid():
    if len(sys.argv) != 3:
        print('you should run the script as as:')
        print('python3 get_weather.py {input-coords-csv} {outut-csv}')
        exit()
    else:
        return sys.argv[1:]

# check if input file exists
def input_file_exists(f):
    try:
        with open(f) as io:
            return (True,'')
    except:
        return (False,'file "{}" does not exist!'.format(f))

# check if the input file can be read by pandas
def input_file_valid(f):
    try:
        testing_df = pd.read_csv(f)
        testing_df = None
        return (True,'')
    except:
        return (False,'file "{}" is not in proper format!'.format(f))

# check if there are x and y columns in lowercase
# and check if their values are numeric
# and check if their values are in range (-180.0,180.0) for x and (-90.0,90.0) for y
# the function returns the dataframe itself if everything is valid
def get_df_if_columns_valid(f):
    
    testing_df = pd.read_csv(f)

    if 'x' in testing_df.columns and 'y' in testing_df.columns:
        if is_numeric_dtype(testing_df['x']) and is_numeric_dtype(testing_df['y']):
            if testing_df['x'].between(-180.0,180.0).all() and testing_df['y'].between(-90.0,90.0).all():
                return (True,testing_df)
            else:
                return (False,'xs and ys in file "{}" should be in ranges (-180.0,180.0) and (-90.0,90.0) respectively!'.format(f))
        else:
            return (False,'columns x and y in file "{}" should have all numeric values!'.format(f))
    else:
        return (False,'file "{}" should have x an y columns!'.format(f))


##################
##main functions##
##################

# update the dataframe with temperature columns
def update_df_temp(df):
    df['temperature (C)'], df['humidity'], df['uvi'], df['clouds'], df['wind_speed'], df['wind_deg']  = zip(*df.apply(lambda r: _parse_temp_resp(r['x'],r['y']), axis=1))
    return df

# update the dataframe with pollution columns
def update_df_polt(df):
    df['co'], df['no'], df['no2'], df['o3'], df['so2'], df['pm2_5'], df['pm10'], df['nh3']  = zip(*df.apply(lambda r: _parse_polt_resp(r['x'],r['y']), axis=1))
    return df

# update the dataframe with elevation column
def update_df_elev(df):
    df['elevation (m)'] = df.apply(lambda r: _parse_elev_resp(r['x'],r['y']), axis=1)
    return df

