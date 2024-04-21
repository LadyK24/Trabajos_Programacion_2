import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd


from frontend.titulo.titulo import titulo
from frontend.descripción.descripción import descripcion
from frontend.entradadatos.entradadatos import entrada_datos
from frontend.salidadatos.salidadatos import salida_datos


from backend1.cortedirecto import corte_directo


layout = dbc.Container([
    dbc.Row([
        dbc.Col(titulo,md=12,style={'background-color':'orange'}),
        dbc.Col(descripcion,md=12,style={'background-color':'white'}),
        dbc.Col(entrada_datos,md=6,style={'background-color':'yellow'}),
        dbc.Col(salida_datos,md=6,style={'background-color':'blue'}),
    
    ])
])