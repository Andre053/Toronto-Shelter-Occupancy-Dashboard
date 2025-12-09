from dash import Dash, html, dcc, callback, Output, Input
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import utils
import data_analysis as da
import pandas as pd

def render(app: Dash, name, id) -> dcc.Graph:
    return dbc.Card([
        dbc.CardBody([
            html.H5(name),
            html.H6(id=id, children="--"),
            html.Small(children="")
        ])
    ])