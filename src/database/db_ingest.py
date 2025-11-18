import requests
import pandas as pd
from db_config import get_engine

from datetime import datetime
from db_config import get_engine
from sqlalchemy import text
from io import StringIO
from db_utils import prep_df

def fetch_data():
    base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
    	
    url = base_url + "/api/3/action/package_show"
    params = { "id": "daily-shelter-overnight-service-occupancy-capacity"}
    package = requests.get(url, params = params).json()
	
    for idx, resource in enumerate(package["result"]["resources"]):
        # for datastore_active resources:
        if resource["datastore_active"] and resource["package_id"] == '21c83b32-d5a8-4106-a54f-010dbe49f6f2':
            # To get all records in CSV format:
            url = base_url + "/datastore/dump/" + resource["id"]
            data = requests.get(url).text

            return data
    return None
    
def get_last_ingested_data():
    engine = get_engine()

    query = text('SELECT MAX("OCCUPANCY_DATE") as last_date FROM "SHELTER_OCCUPANCY"')

    with engine.connect() as conn:
        res = conn.execute(query).fetchone()
        return res[0] if res[0] else datetime.now()

def filter_data(df, last_ingested):
    # only want records newer than last ingested
    df = df[(df['OCCUPANCY_DATE'] > last_ingested)]
    
    return df

def ingest_data():
    last_ingested = get_last_ingested_data()
    print("[INFO] Last ingested date:", last_ingested)

    data = fetch_data()

    df = pd.read_csv(StringIO(data))
    df = prep_df(df)
    
    new_data_df = filter_data(df, last_ingested)

    if new_data_df.empty:
        print("[WARNING] No data to ingest")
        return None

    engine = get_engine()
    new_data_df.to_sql(
        'SHELTER_OCCUPANCY',
        engine,
        if_exists='append',
        index=False,
        method='multi',
        chunksize=1000
    )
    print(f"[INFO] Ingested {len(new_data_df)} new rows in the date range: {new_data_df['OCCUPANCY_DATE'].min()} - {new_data_df['OCCUPANCY_DATE'].max()}")

if __name__ == '__main__':
    print(f"[INFO] Started data ingest at {datetime.now()}")
    ingest_data()
    print(f"[INFO] Completed data ingest at {datetime.now()}")