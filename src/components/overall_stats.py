from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import utils

import data_analysis as da

# Update all overview stats
@callback(
    Output('stat-total', 'children'),
    Output('stat-total-days', 'children'),
    Output('stat-average', 'children'),
    Output('stat-average-change', 'children'),
    Output('stat-max', 'children'),
    Output('stat-min', 'children'),
    Input('filtered-data-store', 'data')
)
def update_overview_stats(json_data):
    if not json_data:
        return "--", "--", "", "--", "", "--", ""
    df = utils.json_to_df(json_data)
    df_by_date = da.data_metrics_by_date(df)
    
    total_records = len(df) # calculated on regular df
    total_days = len(df_by_date) # calculated on regular df

    average = f"{df_by_date['SERVICE_USER_COUNT'].mean():.1f}"
    max_val = int(df_by_date['SERVICE_USER_COUNT'].max())
    max_date = df_by_date.loc[df_by_date['SERVICE_USER_COUNT'].idxmax(), 'OCCUPANCY_DATE'].strftime('%Y-%m-%d')
    min_val = int(df_by_date['SERVICE_USER_COUNT'].min())
    min_date = df_by_date.loc[df_by_date['SERVICE_USER_COUNT'].idxmin(), 'OCCUPANCY_DATE'].strftime('%Y-%m-%d')
    
    avg_change_stat = (df_by_date['SERVICE_USER_COUNT'].iloc[-1] - df_by_date['SERVICE_USER_COUNT'].iloc[0])/df_by_date['SERVICE_USER_COUNT'].iloc[0]
    avg_change = ""
    
    if avg_change_stat > 0:
        avg_change = f"+{avg_change_stat*100:.2f}%"
    else: 
        avg_change = f"{avg_change_stat*100:.2f}%"

    return (
        f"{total_records:,}",
        f"{total_days:,}",
        average,
        avg_change,
        f"{max_val:,} on {max_date}",
        f"{min_val:,} on {min_date}",
    )