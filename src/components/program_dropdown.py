from dash import Dash, html
import dash_bootstrap_components as dbc
import utils

def render(app: Dash) -> html.Div:
    program_details = [
        "PROGRAM_ID", 
        "ORGANIZATION_ID", 
        "SHELTER_ID", 
        "LOCATION_ID"
    ]

    return html.Div(
        children=[
            dbc.RadioItems(
                options=[{"label": utils.data_type_labels[x], "value": x} for x in program_details],
                value='PROGRAM_ID',
                inline=True,
                id='program-radio-selection'
            )
        ]
    )