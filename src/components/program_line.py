from dash import Dash, html, dcc, callback, Output, Input
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import utils
import data_analysis as da

def render(app: Dash, df) -> dcc.Graph:

    @app.callback(
        Output('program-line', 'figure'),
        Input('program-radio-selection', 'value'),
        Input('interval-radio-selection', 'value')
    )
    def update_program_line(selected_metric, interval):
        data = da.data_unique_by_date(df, utils.date_intervals[interval])
        
        fig = px.line(
            data, 
            x='DATE_INTERVAL', 
            y=selected_metric,
            title=f'{utils.data_type_labels[selected_metric]} Count over Time',
            labels={
                "DATE_INTERVAL": utils.data_type_labels["OCCUPANCY_DATE"],
                selected_metric: utils.data_type_labels[selected_metric],
            }
        )
        fig.update_yaxes(range=[0, data[selected_metric].max() * 1.1])
        return fig

    return dcc.Graph(figure={}, id='program-line')