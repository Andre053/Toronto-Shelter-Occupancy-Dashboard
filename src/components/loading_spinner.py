from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import utils

def render(app: Dash, id, children) -> html.Div:

    @app.callback(
        Input('filtered-data-store', 'data'),
        Input('metric-radio-selection', 'value'),
        Input('interval-radio-selection', 'value')
    )
    def loading_value(d, v1, v2):
        pass

    return dcc.Loading(
        id=id,
        children=children,
        type="circle",
    )