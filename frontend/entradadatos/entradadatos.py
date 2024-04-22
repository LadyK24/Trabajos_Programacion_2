import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from backend1.cortedirecto import cortedirecto


ingresodatos=dbc.Container([
    html.H5("¡Ingrese los datos de las muestras!",style={'text-align': 'center'}),
])

caracteristicas=dbc.Container([
    html.H6("Características de la muestra:"),
    
    html.Div([
        html.Label('Diametro (cm):', style={'display': 'inline-block', 'margin-right': '2px'}),
        dcc.Input(type='number', value=8, id="Diametro (cm)",step=0.1),       
    ]),

    html.Div([
        html.Label('Altura (cm):', style={'display': 'inline-block', 'margin-right': '2px'}),
        dcc.Input(type='number', value=8, id="Altura (cm):",step=0.1),       
    ]),
])

Datos_de_corte=dbc.Container([
    html.H6("Datos de corte:"),
    html.Div([
        html.Label('Sobre carga (g):', style={'display': 'inline-block', 'margin-right': '2px'}),
        dcc.Input(type='number', value=8, id="Sobre carga (g)",step=0.1),       
    ]),

    html.Div([
        html.Label('Carga normal(kg):', style={'display': 'inline-block', 'margin-right': '2px'}),
        dcc.Input(type='number', value=8, id="Carga normal (kg):",step=0.1),       
    ]),
    html.Br(),
])


tabla_datos=dbc.Container([
    html.H6("Tabla deformación, fuerzas y esfuerzo",style={'text-align': 'center'}),
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
        dbc.Col(ingresodatos,md=12,style={'background-color':'gray'}), 
        dbc.Col(caracteristicas,md=6,style={'background-color':'#DCDCDC'}),
        dbc.Col(Datos_de_corte,md=6,style={'background-color':'#DCDCDC'}),
        dbc.Col(tabla_datos,md=12,style={'background-color':'#DCDCDC'}),

    ])
])