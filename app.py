import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc


#importar el frontend
from frontend.frontend import layout

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)



app = dash.Dash(__name__external_stylesheets=[dbc.themes.BOOTSTRAP])

