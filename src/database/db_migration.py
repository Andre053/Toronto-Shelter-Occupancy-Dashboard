import pandas as pd

import glob
from db_config import get_engine

def migrate_data():

    engine = get_engine()

    data_files = glob.glob('../resources/data/*.csv')

    data = []
    for f in data_files:
        df = pd.read_csv(f, index_col=None, header=0)
        data.append(df)
    df = pd.concat(data, axis=0, ignore_index=True)

    # convert date column
    df['OCCUPANCY_DATE'] = pd.to_datetime(df['OCCUPANCY_DATE'])

    table_name = 'shelter-occupancy-data'

    df.to_sql(
        table_name,
        engine,
        if_exists='replace',
        index=False,
        method='multi',
        chunksize=1000
    )

    print("Migration complete")

if __name__ == '__main__':
    migrate_data()
