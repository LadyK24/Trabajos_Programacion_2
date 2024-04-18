import dash 
from dash import html
import dash_bootstrap_components as dbc

corte_directo = dbc.Container([
    html.H1("ENSAYO CORTE DIRECTO")
])
subt = dbc.Container([
    html.H1("INV E 154 - 13")
])
titulo = dbc.Container([
    dbc.Row([
        dbc.Col(corte_directo,md=12,style={'background-color':'orange'}),
        dbc.Col(subt,md=12,style={'background-color':'orange'}),
        html.Br(),html.Br()
    ])
])