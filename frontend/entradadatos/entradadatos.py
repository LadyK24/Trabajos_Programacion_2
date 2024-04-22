import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from backend1.cortedirecto import cortedirecto


ingresodatos=dbc.Container([
    html.H5("¡Ingrese los datos de las muestras!"),
])

caracteristicas=dbc.Container([
    html.H5("Características de la muestra:"),
    
    html.Div([
        html.Label('Diametro (m):   '),
        html.Label('__________',style={'color':'green'}),
        dcc.Input(type='number', value=5, id="Diametro (m)")
    ]),

    html.H5('Diametro'),
    dcc.Input(type='number', value=5, id="edad"),
    html.Br(),
    html.H5('Altura'),
    dcc.Input(type='number', value=5, id="edad")
])

Datos_de_corte=dbc.Container([
    html.H5("Datos de corte:"),
    html.Br(),
    html.H5('Sobre carga'),
    dcc.Input(type='number', value=5, id="edad"),
    html.H5('Carga nominal'),
    dcc.Input(type='number', value=5, id="edad")
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
        dbc.Col(ingresodatos,md=12,style={'background-color':'yellow'}), 
        dbc.Col(caracteristicas,md=6,style={'background-color':'orange'}),
        dbc.Col(Datos_de_corte,md=6,style={'background-color':'gray'}),
        dbc.Col(tabla_datos,md=12,style={'background-color':'green'}),

    ])
])