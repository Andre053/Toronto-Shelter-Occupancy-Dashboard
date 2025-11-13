from dash import Dash, html, dcc, callback, Output, Input
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import utils
import data_analysis as da

def get_graph_details(metric, time_interval, df):
    data = None
    title = ""
    if metric == 'Beds':
        data = da.data_stacked_by_date_beds(df, "OCCUPIED_BEDS", "UNOCCUPIED_BEDS", time_interval)
        title='Average Monthly Occupied vs. Unoccupied Beds'
    elif metric == 'Rooms':
        data = da.data_stacked_by_date_beds(df, "OCCUPIED_ROOMS", "UNOCCUPIED_ROOMS", time_interval)
        title='Average Monthly Occupied vs. Unoccupied Rooms'
    return data, title

def render(app: Dash, df) -> dcc.Graph:

    @app.callback(
        Output('stacked-bar', 'figure'),
        Input('stacked-radio-selection', 'value'),
        Input('interval-radio-selection', 'value')
    )
    def update_stacked_bar(selected_metric, selected_interval):
        data, title = get_graph_details(selected_metric, utils.date_intervals[selected_interval], df)
        fig = px.area(
            data, 
            x='DATE_INTERVAL',
            y='value',
            color='variable',
            title=title,
            labels={
                'DATE_INTERVAL': utils.data_type_labels["OCCUPANCY_DATE"],
                'value': 'Count',
                'variable': 'Metric'
            }
        )
        fig.update_yaxes(range=[0, data['value'].max() * 1.5])

        return fig
    
    return dcc.Graph(figure={}, id='stacked-bar')