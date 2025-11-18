from dash import Dash, html, dcc, callback, Output, Input, dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import utils
import pandas as pd
import data_analysis as da

def render(app: Dash) -> dash_table:
    @callback(
        Output('metric-table', 'data'),
        Input('filtered-data-store', 'data'),
        Input('metric-radio-selection', 'value'),
        Input('interval-radio-selection', 'value')
    )
    def update_metric_table(json_data, metric, interval):
        df = utils.json_to_df(json_data)
        data = da.data_metrics_by_date(df, utils.date_intervals[interval])

        filtered_data = data[['DATE_INTERVAL', metric]].to_dict('records')
        return filtered_data

    return dash_table.DataTable(
        data=None, 
        page_size=10, 
        style_table={'overflowX': 'auto'}, 
        id='metric-table'
    )