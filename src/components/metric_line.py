from dash import Dash, html, dcc, callback, Output, Input
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import utils
import data_analysis as da

def render(app: Dash, data) -> dcc.Graph:

    @app.callback(
        Output('metric-line', 'figure'),
        Input('metric-radio-selection', 'value')
    )
    def update_metric_line(selected_metric):
        fig = px.line(
            data, 
            x='OCCUPANCY_DATE', 
            y=selected_metric,
            title=f'{utils.data_type_labels[selected_metric]} Count over Time',
            labels={
                "OCCUPANCY_DATE": utils.data_type_labels["OCCUPANCY_DATE"],
                selected_metric: utils.data_type_labels[selected_metric],
            }
        )
        fig.update_yaxes(range=[0, data[selected_metric].max() * 1.1])
        return fig

    return dcc.Graph(figure={}, id='metric-line')