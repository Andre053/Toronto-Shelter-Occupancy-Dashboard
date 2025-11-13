from dash import Dash, html
import dash_bootstrap_components as dbc
import utils

def render(app: Dash) -> html.Div:
    date_intervals = ["Daily", "Monthly"] # TODO add in Yearly metrics

    return html.Div(
        children=[
            dbc.RadioItems(
                options=[{"label": x, "value": x} for x in date_intervals],
                value="Daily",
                inline=True,
                id='interval-radio-selection'
            )
        ]
    )