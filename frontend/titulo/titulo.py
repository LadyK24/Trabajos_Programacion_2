import dash 
from dash import html
import dash_bootstrap_components as dbc

titulo = dbc.Container([
    dbc.Row([
        dbc.Col('ENSAYO CORTE DIRECTO',md=12,style={'background-color':'orange'}),
        dbc.Col('INV E 154 13',md=12,style={'background-color':'orange'}),
        html.Br(),html.Br()
    ])
])