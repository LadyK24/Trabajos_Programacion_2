import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from backend1.cortedirecto import cortedirecto1


ingresodatos=dbc.Container([
    html.H5("¡Ingrese los datos de las muestras!",style={'text-align': 'center'}),
])

caracteristicas=dbc.Container([
    html.Br(),
    html.H6("Características de la muestra:"),
    
    html.Div([
        html.Label('Diametro (cm):', style={'display': 'inline-block', 'margin-right': '2px'}),
        dcc.Input(type='number', value=6, id="Diametro",step=0.1),
        html.Label(id='salidaarea'),       
    ]),

    html.Div([
        html.Label('Altura (cm):', style={'display': 'inline-block', 'margin-right': '2px'}),
        dcc.Input(type='number', value=2, id="Altura",step=0.1),       
    ]),
])

Datos_de_corte=dbc.Container([
    html.Br(),
    html.H6("Datos de corte:"),
    html.Div([
        html.Label('Sobre carga (g):', style={'display': 'inline-block', 'margin-right': '2px'}),
        dcc.Input(type='number', value=503.5, id="Sobrecarga",step=0.1),       
    ]),

    html.Div([
        html.Label('Relacióncarga1:', style={'display': 'inline-block', 'margin-right': '2px'}),
        dcc.Input(type='number', value=0.5, id="Relacioncarga1",step=0.1),       
    ]),

    html.Div([
    html.Label('Relacióncarga2:', style={'display': 'inline-block', 'margin-right': '2px'}),
    dcc.Input(type='number', value=1.0, id="Relacioncarga2",step=0.1),       
    ]),
   
    html.Div([
    html.Label('Relacióncarga3:', style={'display': 'inline-block', 'margin-right': '2px'}),
    dcc.Input(type='number', value=1.5, id="Relacioncarga3",step=0.1),       
    ]),
    html.Br(),

])

# Tabla de datos

tabla_datos=dbc.Container([
    html.H5("Tabla deformación, fuerzas y esfuerzos",style={'text-align': 'center'}),
    html.H6("Deformación (mm)"),
    html.H6("Fuerzas (N)"),
    html.H6("Esfuerzos (kg/cm2)"),
    dash_table.DataTable(
        id='tabla_cortedirecto',
        columns=[
            {'name': 'Deformacion', 'id': 'Deformacion','editable': False},
            {'name': 'Fuerza1', 'id': 'Fuerza1','editable': True},
            {'name': 'Fuerza2', 'id': 'Fuerza2', 'editable': True},
            {'name': 'Fuerza3', 'id': 'Fuerza3', 'editable': True},
            {'name': 'Esfuerzo1', 'id': 'Esfuerzo1', 'editable': False},
            {'name': 'Esfuerzo2', 'id': 'Esfuerzo2', 'editable': False},
            {'name': 'Esfuerzo3', 'id': 'Esfuerzo3', 'editable': False}
            ],

        data=cortedirecto1.to_dict('records')           
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