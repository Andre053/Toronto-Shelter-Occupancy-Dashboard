import pandas as pd
from glob import glob
import os

# TODO get all data
def get_data():
    print("Getting data")

    #path = '../resources/data'
    data_files = glob("../resources/data/*.csv")

    data = []
    for f in data_files:
        df = pd.read_csv(f, index_col=None, header=0)
        data.append(df)
    df = pd.concat(data, axis=0, ignore_index=True)

    return prep_data(df)

def parse_date(date):
    date_length = len(date)

    # dates must be in %Y-%m-%d form, some had T00:00:00 appended or were %y at start
    if pd.isna(date): return None
    if date_length == 19: date = date[:-9]
    elif date_length == 8: date = '20' + date
    else: return date

    return date

def prep_data(df):
    df['OCCUPANCY_DATE'] = df['OCCUPANCY_DATE'].apply(lambda x: parse_date(x))
    df['OCCUPANCY_DATE'] = pd.to_datetime(df['OCCUPANCY_DATE'], format='%Y-%m-%d')
    df['LOCATION_FSA_CODE'] = df['LOCATION_POSTAL_CODE'].apply(lambda x: x[:3] if pd.notnull(x) else "N/A")

    return df