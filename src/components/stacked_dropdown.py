from dash import Dash, html
import dash_bootstrap_components as dbc

def render(app: Dash) -> html.Div:
    program_details = [
        "Beds", 
        "Rooms", 
    ]

    return html.Div(
        children=[
            dbc.RadioItems(
                options=[{"label": x, "value": x} for x in program_details],
                value='Beds',
                inline=True,
                id='stacked-radio-selection'
            )
        ]
    )