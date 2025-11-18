import pandas as pd
from database.db_config import get_engine


def get_data(start_date, end_date):
    engine = get_engine()

    query = f"""
        SELECT *
        FROM "SHELTER_OCCUPANCY"
        WHERE "OCCUPANCY_DATE" >= '{start_date}' AND "OCCUPANCY_DATE" <= '{end_date}'
        ORDER BY "OCCUPANCY_DATE";
    """
    df = pd.read_sql(query, engine)
    df['OCCUPANCY_DATE'] = pd.to_datetime(df['OCCUPANCY_DATE'])

    #print("Loaded data with rows:", len(df))
    return df

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