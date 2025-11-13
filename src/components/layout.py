from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from components import program_dropdown, program_table, program_line, metric_dropdown, metric_table, metric_line, date_selector, stacked_dropdown, interval_dropdown, stacked_area

import data_analysis as da
import data_management as dm


def render(app: Dash) -> dbc.Container:
    print("Rendering layout")

    df = dm.get_data() # get data within default timeframe

    metric_data = da.data_metrics_by_date(df)

    return dbc.Container([
        dbc.Row([
            html.H1(children=app.title, style={'textAlign':'center'}), # title
        ]),
        dbc.Row([
            date_selector.render(app),
            interval_dropdown.render(app)
        ]),
        dbc.Row([
            html.H2(children="Occupancy metrics")
        ]),
        dbc.Row([
            metric_dropdown.render(app)
        ]),
        dbc.Row([
            dbc.Col([
                metric_table.render(app, df)
            ], width=4),
            dbc.Col([
                metric_line.render(app, df)
            ], width=8),
        ]),
        dbc.Row([
            html.H2(children="Program metrics")
        ]),
        dbc.Row([
            program_dropdown.render(app)
        ]),
        dbc.Row([
            dbc.Col([
                program_table.render(app, df)
            ], width=4),
            dbc.Col([
                program_line.render(app, df)
            ], width=8),
        ]),
        dbc.Row([
            html.H2(children="Occupied vs. Unoccupied metrics")
        ]),
        dbc.Row([
            stacked_dropdown.render(app)
        ]),
        dbc.Row([
            dbc.Col([
                stacked_area.render(app, df)
            ], width=10),
        ])
    ], fluid=True)