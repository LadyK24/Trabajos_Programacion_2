import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from backend1.esfuerzos import esfuerzos

resultados=dbc.Container([
    html.H5("Resultados", style={'text-align': 'center'}),
])


grafica=dbc.Container([
    html.Br(),
    html.H5("Curva Deformación horizontal - Esfuerzo cortante", style={'text-align': 'center'}),
    dcc.Graph(id="cortedirecto_plot")
])


esfuerzos_tabla=dbc.Container([
    html.Br(),html.Br(), # AGREGAR ESPACIO
    html.H5("Resultados de los esfuerzos de las muestras", style={'text-align': 'center'}),
    dash_table.DataTable(
        id='esfuerzos_tabla_dataframe',
        columns=[
            {'name': 'Muestra', 'id': 'Muestra','editable': False},
            {'name': 'Normal', 'id': 'Normal','editable': False},
            {'name': 'Cortante', 'id': 'Cortante', 'editable': False},
            {'name': 'Residual', 'id': 'Residual', 'editable': False},
            ],

        data=esfuerzos.to_dict('records')           
    ),
])

html.Br(),

grafica2=dbc.Container([
    html.Br(),html.Br(),
    html.H5("Curva  Esfuerzo Normal - Esfuerzo Cortante", style={'text-align': 'center'}),
    dcc.Graph(id="Esfuerzos_plot")
])

parametros=dbc.Container([
    html.Br(),
    html.H4("Parámetros del suelo",style={'text-align': 'center'}),
    html.Br(),


    html.Button('Cohesión máxima'),
    html.Br(),html.Br(),
    html.Button('Cohesión residual'),
    html.Br(),html.Br(),
    html.Button('Fricción máxima'),
    html.Br(),html.Br(),
    html.Button('Fricción residual')
])




salida_datos = dbc.Container([
    dbc.Row([
        dbc.Col(resultados,md=12,style={'background-color':'gray'}), 
        dbc.Col(grafica,md=12,style={'background-color':'#DCDCDC'}),  
        dbc.Col(esfuerzos_tabla,md=12,style={'background-color':'#DCDCDC'}),
        html.Br(),html.Br(),html.Br(),
        dbc.Col(grafica2,md=12,style={'background-color':'#DCDCDC'}),
        html.Br(),


    ])
])