from dash import Dash, html, dcc, callback, Output, Input, dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import utils
import data_analysis as da

def render(app: Dash, df) -> html.Div:

    @app.callback(
        Output('program-table', 'data'),
        Input('program-radio-selection', 'value'),
        Input('interval-radio-selection', 'value')
    )
    def update_program_table(selected_metric, interval):
        data = da.data_unique_by_date(df, utils.date_intervals[interval])

        filtered_data = data[['DATE_INTERVAL', selected_metric]].to_dict('records')
        
        return filtered_data

    return dash_table.DataTable(
        data=None, 
        page_size=10, 
        style_table={'overflowX': 'auto'}, 
        id='program-table'
    )