import pandas as pd
from datetime import datetime

import utils

def current_service_users(df):
    # 1. get final date
    final_date = df['OCCUPANCY_DATE'].unique()[-1]
    print("Final date in dataset is:", final_date)
    # 2. get all related records
    df_today = df[df['OCCUPANCY_DATE'] == final_date]
    # 3. sum user counts
    total_users = df_today['SERVICE_USER_COUNT'].sum()

    return total_users

def data_metrics_by_date(df, time_interval=utils.TimeInterval.DAILY):
    cols = [
        "OCCUPANCY_DATE",
        "SERVICE_USER_COUNT",
        "CAPACITY_ACTUAL_BED",
        "CAPACITY_FUNDING_BED",
        "OCCUPIED_BEDS",
        "UNOCCUPIED_BEDS",
        "CAPACITY_ACTUAL_ROOM",
        "CAPACITY_FUNDING_ROOM",
        "OCCUPIED_ROOMS",
        "UNOCCUPIED_ROOMS"
    ]
    df_filtered = df[cols]

    if time_interval == utils.TimeInterval.DAILY:
        df_grouped = df_filtered.groupby(['OCCUPANCY_DATE'], as_index=False).agg('sum')
        df_grouped['DATE_INTERVAL'] = df_grouped['OCCUPANCY_DATE'].dt.date

        return df_grouped
    
    elif time_interval == utils.TimeInterval.MONTHLY:
        df_filtered['MONTH_YEAR'] = df_filtered['OCCUPANCY_DATE'].apply(lambda d: datetime(d.year, d.month, 1))
    
        df_grouped = df_filtered.groupby(['OCCUPANCY_DATE', 'MONTH_YEAR'], as_index=False).agg('sum')
        df_grouped = df_grouped.groupby('MONTH_YEAR', as_index=False).agg('mean').round(2)
        df_grouped['DATE_INTERVAL'] = df_grouped['MONTH_YEAR'].dt.date

        return df_grouped

    return "ERROR"

def data_unique_by_date(df, time_interval=utils.TimeInterval.DAILY):
    cols = [
        "OCCUPANCY_DATE",
        "ORGANIZATION_ID",
        "PROGRAM_ID",
        "SHELTER_ID",
        "LOCATION_ID",
    ]
    df_filtered = df[cols]

    if time_interval == utils.TimeInterval.DAILY:
        df_grouped = df_filtered.groupby(['OCCUPANCY_DATE'], as_index=False).agg('nunique')
        df_grouped['DATE_INTERVAL'] = df_grouped['OCCUPANCY_DATE'].dt.date

        return df_grouped
    
    elif time_interval == utils.TimeInterval.MONTHLY:
        df_filtered['MONTH_YEAR'] = df_filtered['OCCUPANCY_DATE'].apply(lambda d: datetime(d.year, d.month, 1))
    
        df_grouped = df_filtered.groupby(['OCCUPANCY_DATE', 'MONTH_YEAR'], as_index=False).agg('nunique')
        df_grouped = df_grouped.groupby('MONTH_YEAR', as_index=False).agg('mean').round(2)
        df_grouped['DATE_INTERVAL'] = df_grouped['MONTH_YEAR'].dt.date

        return df_grouped

    return "ERROR"

# monthly
def data_stacked_by_date_beds(df, metric1, metric2, time_interval=utils.TimeInterval.DAILY, start="2025-01-01", end="2025-10-01"):
    cols = [
        "OCCUPANCY_DATE",
        metric1,
        metric2,
    ]
    df_filtered = df[cols]

    if time_interval == utils.TimeInterval.DAILY:
        df_grouped = df_filtered.groupby(['OCCUPANCY_DATE'], as_index=False).agg('nunique')
        df_grouped['DATE_INTERVAL'] = df_grouped['OCCUPANCY_DATE'].dt.date

        df_melted = pd.melt(df_grouped, id_vars=['DATE_INTERVAL'], value_vars=[metric1, metric2])
        return df_melted
    
    elif time_interval == utils.TimeInterval.MONTHLY:
        df_filtered['MONTH_YEAR'] = df_filtered['OCCUPANCY_DATE'].apply(lambda d: datetime(d.year, d.month, 1))
    
        df_grouped = df_filtered.groupby(['OCCUPANCY_DATE', 'MONTH_YEAR'], as_index=False).agg('nunique')
        df_grouped = df_grouped.groupby('MONTH_YEAR', as_index=False).agg('mean').round(2)
        df_grouped['DATE_INTERVAL'] = df_grouped['MONTH_YEAR'].dt.date

        df_melted = pd.melt(df_grouped, id_vars=['DATE_INTERVAL'], value_vars=[metric1, metric2])

        return df_melted

    return "ERROR"

def mean_service_users(df, stat, start, end):
    # 2. sum for each date
    df_agg = df.groupby('OCCUPANCY_DATE').agg('sum')
    # 3. mean over all dates
    mean_val = df_agg[stat].mean()
    

