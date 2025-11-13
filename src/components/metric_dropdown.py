from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import utils

def render(app: Dash) -> html.Div:
    metric_names = [
        "SERVICE_USER_COUNT", 
        "OCCUPIED_BEDS", 
        "UNOCCUPIED_BEDS", 
        "OCCUPIED_ROOMS",
        "UNOCCUPIED_ROOMS"
    ]

    return html.Div(
        children=[
            dbc.RadioItems(
                options=[{"label": utils.data_type_labels[x], "value": x} for x in metric_names],
                value='SERVICE_USER_COUNT',
                inline=True,
                id='metric-radio-selection'
            )
        ]
    )