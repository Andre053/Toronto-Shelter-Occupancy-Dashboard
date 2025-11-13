from dash import Dash, html
import dash_bootstrap_components as dbc
import components.layout as layout

external_stylesheets = [dbc.themes.PULSE]
app = Dash(__name__, external_stylesheets=external_stylesheets)

def main():
    app.title = "Toronto Shelter Occupancy Dashboard"
    app.layout = layout.render(app)
    app.run(debug=True)

if __name__ == '__main__':
    main()