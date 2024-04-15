import dash 
from dash import html
import dash_bootstrap_components as dbc

from frontend.titulo.titulo import titulo
from frontend.descripción.descripción import descripcion
from frontend.entradadatos.entradadatos import entrada_datos


layout = dbc.Container([
    dbc.Row([
        dbc.Col(titulo,md=12,style={'background-color':'orange'}),
        dbc.Col(descripcion,md=12,style={'background-color':'white'}),
        dbc.Col(entrada_datos,md=6,style={'background-color':'yellow'}),
        dbc.Col('salidadatos',md=6,style={'background-color':'blue'}),
    ])
])