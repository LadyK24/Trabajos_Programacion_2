import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from backend1.cortedirecto import cortedirecto


ingresodatos=dbc.Container([
    html.H2("Características de la muestra"),
    html.Br(),html.Br(),
])

caracteristicas=dbc.Container([
    html.H3("Características de la muestra"),
    html.Br(),html.Br(),
    html.Button('Diametro'),
    html.Br(),html.Br(),
    html.Button('Altura')
])

Datos_de_corte=dbc.Container([
    html.H3("Datos de corte"),
    html.Br(),html.Br(),
    html.Button('Sobre carga'),
    html.Br(),html.Br(),
    html.Button('Carga nominal')
])


tabla_datos=dbc.Container([
    html.H1("Realización de tablas"),
    dash_table.DataTable(
        id='tabla_granulometria',
        columns=[
            {'name': 'Deformacion', 'id': 'Deformacion','editable': False},
            {'name': 'Fuerza1', 'id': 'Fuerza1','editable': True},
            {'name': 'Fuerza2', 'id': 'Fuerza2', 'editable': True},
            {'name': 'Fuerza3', 'id': 'Fuerza3', 'editable': True},
            {'name': 'Esfuerzo1', 'id': 'Esfuerzo1', 'editable': False},
            {'name': 'Esfuerzo2', 'id': 'Esferzo2', 'editable': False},
            {'name': 'Esfuerzo3', 'id': 'Esfuerzo3', 'editable': False}
            ],
        data=cortedirecto.to_dict('records')           
    ),
])


entrada_datos = dbc.Container([
    dbc.Row([
        dbc.Col('ingresodatos',md=12,style={'background-color':'yellow'}), 
        dbc.Col(caracteristicas,md=6,style={'background-color':'orange'}),
        dbc.Col(Datos_de_corte,md=6,style={'background-color':'gray'}),
        dbc.Col(tabla_datos,md=12,style={'background-color':'green'}),

    ])
])