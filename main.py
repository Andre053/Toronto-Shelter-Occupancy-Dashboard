from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.io as pio
import pandas as pd
import data_management as dm
import data_analysis as da
import utils

df = dm.get_data()

external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# LAYOUT
#   - Show key statistics with captions and change arrow
#   - Show accompanying graphs
app.layout = dbc.Container([
    dbc.Row([
        html.H1(children='Toronto Overnight Shelter Data Dashboard', style={'textAlign':'center'}), # title
    ]),
    dbc.Row([
        dcc.DatePickerRange(), # choose dates for the dashboard, default is YTD
        dbc.RadioItems(options=[{"label": utils.data_type_labels[x], "value": x} for x in ["SERVICE_USER_COUNT", "OCCUPIED_BEDS", "UNOCCUPIED_BEDS", "OCCUPIED_ROOMS","UNOCCUPIED_ROOMS"]],
                       value='SERVICE_USER_COUNT',
                       inline=True,
                       id='metric-radio-selection')
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(data=None, 
                                 page_size=10, 
                                 style_table={'overflowX': 'auto'}, 
                                 id='stat-table')
        ], width=4),
        dbc.Col([
            dcc.Graph(figure={}, id='stat-graph')
        ], width=8),
    ]),
    #html.Label(children="Drill down by feature"),
    #dcc.RadioItems(["SHELTER_GROUP", "ORGANIZATION_NAME", "LOCATION_NAME", "FSA"], 'SHELTER_GROUP', id='su-radio-selection'),
    #dcc.Dropdown(value=None, id='su-dropdown-selection'), # service user drill-down, 
    #dcc.Graph(id='su-graph-content'), # service user graph, id is needed for the output of callback
    #dcc.Graph(id='su-graph-multi'),
    #html.Div("Graph metrics"),
    #dcc.RadioItems(["FSA", "Neighbourhood"]),
    #dcc.Graph(id='map-toronto'),
    #dcc.Graph(id='map-drilldown')
], fluid=True)

# Q1: Occupancy of the shelter system
#   1) Current statistics
#       - Overall count of daily users
#       - Overall shelters
#       - Overall rooms in use
#       - Average occupancy rates
#       - Change over day, week, month, year


# DYNAMIC CONTENT

@callback(
    Output('stat-table', 'data'),
    Input('metric-radio-selection', 'value')
)
def update_stat_table(selected_metric):
    data = da.data_metrics_by_date(df)
    data = data[['OCCUPANCY_DATE', selected_metric]].to_dict('records')
    return data

@callback(
    Output('stat-graph', 'figure'),
    Input('metric-radio-selection', 'value')
)
def update_stat_plot(selected_metric):
    print("Service user plot called with", selected_metric)
    data = da.data_metrics_by_date(df)
    fig = px.line(
        data, 
        x='OCCUPANCY_DATE', 
        y=selected_metric,
        title=f'{utils.data_type_labels[selected_metric]} over Time',
        labels={
            "OCCUPANCY_DATE": utils.data_type_labels["OCCUPANCY_DATE"],
            selected_metric: utils.data_type_labels[selected_metric],
        }
    )
    fig.update_yaxes(range=[0, data[selected_metric].max() * 1.1])
    return fig

if __name__ == '__main__':
    app.run(debug=True)
