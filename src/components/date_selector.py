from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import utils

def render(app: Dash) -> html.Div:
    return dcc.DatePickerRange()