import dash 
from dash import html
import dash_bootstrap_components as dbc

from frontend.titulo.titulo import titulo

layout = dbc.Container([
    dbc.Row([
        dbc.Col(titulo,md=12,style={'background-color':'orange'}),
        dbc.Col('descripcion',md=12,style={'background-color':'white'}),
        dbc.Col('entradadatos',md=6,style={'background-color':'yellow'}),
        dbc.Col('salidadatos',md=6,style={'background-color':'blue'}),
    ])
])