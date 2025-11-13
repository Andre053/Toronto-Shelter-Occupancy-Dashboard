


def current_service_users(df):
    print("Getting occupancy stats")

    # STAT 1, total service users today
    #   - COLUMN: SERVICE_USER_COUNT
    #   - AGGREGATION: SUM
    #   - DATE RANGE: TODAY (or last element)
    #   Steps
    #       1. Get the final date
    #       2. Get all related records
    #       3. Aggregate the service user count

    # 1. get final date
    final_date = df['OCCUPANCY_DATE'].unique()[-1]
    print("Final date in dataset is:", final_date)

    # 2. get all related records
    df_today = df[df['OCCUPANCY_DATE'] == final_date]

    # 3. sum user counts
    total_users = df_today['SERVICE_USER_COUNT'].sum()

    return total_users

def data_metrics_by_date(df, start="2025-01-01", end="2025-10-01"):
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
    df_filtered = data_in_date_range(df, start, end)[cols]

    df_grouped = df_filtered.groupby('OCCUPANCY_DATE', as_index=False).agg('sum')

    return df_grouped

def data_unique_by_date(df, start="2025-01-01", end="2025-10-01"):
    cols = [
        "OCCUPANCY_DATE",
        "ORGANIZATION_ID",
        "PROGRAM_ID",
        "SHELTER_ID",
        "LOCATION_ID",
    ]
    df_filtered = data_in_date_range(df, start, end)[cols]
    df_grouped = df_filtered.groupby('OCCUPANCY_DATE', as_index=False).agg('nunique')

    return df_grouped

def data_in_date_range(df, start, end):
    df_filtered = None
    
    if start and end:
        #df_filtered = df[df['OCCUPANCY_DATE'] >= start and df['OCCUPANCY_DATE'] <= end]
        df_filtered = df[df['OCCUPANCY_DATE'] >= start]
    elif start: 
        df_filtered = df[df['OCCUPANCY_DATE'] >= start]
    elif end: 
        df_filtered = df[df['OCCUPANCY_DATE'] <= end]

    return df_filtered

def mean_service_users(df, stat, start, end):
    df_filtered = data_in_date_range(df, start, end)
    # 2. sum for each date
    df_agg = df_filtered.groupby('OCCUPANCY_DATE').agg('sum')
    # 3. mean over all dates
    mean_val = df_agg[stat].mean()
    

