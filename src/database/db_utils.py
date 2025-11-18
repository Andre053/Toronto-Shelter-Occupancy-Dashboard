import pandas as pd

def parse_date(date):
    date_length = len(date)

    # dates must be in %Y-%m-%d form, some had T00:00:00 appended or were %y at start
    if pd.isna(date): return None
    if date_length == 19: date = date[:-9]
    elif date_length == 8: date = '20' + date
    else: return date

    return date

def prep_df(df):
    df['OCCUPANCY_DATE'] = df['OCCUPANCY_DATE'].apply(lambda x: parse_date(x)) # data cleanup required
    df['OCCUPANCY_DATE'] = pd.to_datetime(df['OCCUPANCY_DATE'], format='%Y-%m-%d')

    return df