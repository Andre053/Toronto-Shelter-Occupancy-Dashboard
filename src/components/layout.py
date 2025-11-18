from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from components import program_dropdown, program_table, program_line, metric_dropdown, metric_table, metric_line, date_selector, stacked_dropdown, interval_dropdown, stacked_area

import data_analysis as da
import data_management as dm

from datetime import datetime, timedelta

def render(app: Dash) -> dbc.Container:
    print("Rendering layout")

    @app.callback(
        Output('filtered-data-store', 'data'),
        Input('date-picker', 'start_date'),
        Input('date-picker', 'end_date')
    )
    def update_data(start_date, end_date):
        print("updating data store")

        start = None
        end = None
        if not start_date or not end_date:
            end = datetime.now() 
            start = datetime.now() - timedelta(days=180)
        else:
            start = pd.to_datetime(start_date)
            end = pd.to_datetime(end_date)

        df = dm.get_data()

        df = df[(df['OCCUPANCY_DATE'] >= start) & (df['OCCUPANCY_DATE'] <= end)]

        return df.to_json(date_format='iso', orient='split')

    return dbc.Container([
        dbc.Row([
            html.H1(children=app.title, style={'textAlign':'center'}), # title
        ], style={'margin': '10px', 'fontWeight': 'bold'}),
        dbc.Row([
            html.Div([
                html.Label("Quick select:", style={'marginRight': '10px'}),
                html.Button("Last month", id='btn-last-month', n_clicks=0, style={'marginRight': '5px'}),
                html.Button("Last 6 months", id='btn-last-6-months', n_clicks=0, style={'marginRight': '5px'}),
                html.Button("Last year", id='btn-last-year', n_clicks=0, style={'marginRight': '5px'}),
                html.Button("All time", id='btn-all-data', n_clicks=0, style={'marginRight': '5px'})
            ], style={'display': 'flex', 'alignItems': 'center'}),
            html.Div([
                html.Label("Data interval:", style={'marginRight': '10px'}),
                interval_dropdown.render(app)
            ], style={'display': 'flex', 'alignItems': 'center'}),
            date_selector.render(app),
        ], style={'marginTop': '5px', 'marginBottom': '10px'}),
        dbc.Row([
            html.H2(children="Occupancy metrics")
        ]),
        dbc.Row([
            metric_dropdown.render(app)
        ]),
        dbc.Row([
            dbc.Col([
                metric_table.render(app)
            ], width=4),
            dbc.Col([
                metric_line.render(app)
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
                program_table.render(app)
            ], width=4),
            dbc.Col([
                program_line.render(app)
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
                stacked_area.render(app)
            ], width=10),
        ]),
        dcc.Store(id='filtered-data-store')
    ], fluid=True)