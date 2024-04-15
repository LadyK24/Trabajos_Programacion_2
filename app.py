import dash 
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1('ENSAYO DE CORTE DIRECTO')
])
if __name__ == '__main__':
    app.run_server(debug=True)




"""algo"""
"""Calma"""