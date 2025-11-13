from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from components import program_dropdown, program_table, program_line, metric_dropdown, metric_table, metric_line
import data_analysis as da
import data_management as dm


def render(app: Dash) -> dbc.Container:
    print("Rendering layout")

    df = dm.get_data() # get data within default timeframe

    metric_data = da.data_metrics_by_date(df)
    program_data = da.data_unique_by_date(df)

    return dbc.Container([
        dbc.Row([
            html.H1(children='Toronto Overnight Shelter Data Dashboard', style={'textAlign':'center'}), # title
            dcc.DatePickerRange(), # choose dates for the dashboard, default is YTD
        ]),
        dbc.Row([
            metric_dropdown.render(app)
        ]),
        dbc.Row([
            dbc.Col([
                metric_table.render(app, metric_data)
            ], width=4),
            dbc.Col([
                metric_line.render(app, metric_data)
            ], width=8),
        ]),
        dbc.Row([
            program_dropdown.render(app)
        ]),
        dbc.Row([
            dbc.Col([
                program_table.render(app, program_data)
            ], width=4),
            dbc.Col([
                program_line.render(app, program_data)
            ], width=8),
        ]),
    ], fluid=True)