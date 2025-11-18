from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import utils

from dash import Dash, html, dcc, callback, Output, Input, ctx

from datetime import datetime, timedelta

def render(app: Dash) -> html.Div:

    @app.callback(
        Output('date-picker', 'start_date'),
        Output('date-picker', 'end_date'),
        Input('btn-last-month', 'n_clicks'),
        Input('btn-last-6-months', 'n_clicks'),
        Input('btn-last-year', 'n_clicks'),
        Input('btn-all-data', 'n_clicks')
    )
    def update_date_range(btn_month, btn_6_months, btn_year, btn_all):
        end_date = datetime.now()

        if ctx.triggered_id == 'btn-last-month':
            start_date = end_date - timedelta(days=30)
        elif ctx.triggered_id == 'btn-last-6-months':
            start_date = end_date - timedelta(days=180)
        elif ctx.triggered_id == 'btn-last-year':
            start_date = end_date - timedelta(days=365)
        elif ctx.triggered_id == 'btn-all-data':
            start_date = datetime(2021, 1, 1)
        else:
            start_date = end_date - timedelta(days=180)

        return start_date, end_date

    return dcc.DatePickerRange(
        id='date-picker',
        start_date=datetime.now() - timedelta(days=180),
        end_date=datetime.now(),
        display_format='YYYY-MM-DD'
    )