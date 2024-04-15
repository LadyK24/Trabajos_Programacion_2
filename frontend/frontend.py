import dash 
from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col('ENSAYO CORTE DIRECTO',md=80,style={'background-color':'orange'}),
        dbc.Col('Descripción',md=30,style={'background-color':'white'}),
        dbc.Col('Datos',md=80,style={'background-color':'yellow'}),
        dbc.Col('Resultados',md=80,style={'background-color':'blue'}),
    ])
])