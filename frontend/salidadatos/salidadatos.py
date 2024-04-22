import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from backend1.esfuerzos import esfuerzos

resultados=dbc.Container([
    html.H5("Curvas - Deformación horizontal", style={'text-align': 'center'}),
])



esfuerzos_tabla=dbc.Container([
    html.H5("Resultados de los esfuerzo de las muestras"),
    dash_table.DataTable(
        id='esfuerzos_tabla',
        columns=[
            {'name': 'Muestra', 'id': 'Muestra','editable': False},
            {'name': 'Normal', 'id': 'Normal','editable': False},
            {'name': 'Cortante', 'id': 'Cortante', 'editable': False},
            {'name': 'Residual', 'id': 'Residual', 'editable': False},
            ],

        data=esfuerzos.to_dict('records')           
    ),
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
        dbc.Col('Gráfica',md=12,style={'background-color':'#DCDCDC'}),
        html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),    
        dbc.Col(esfuerzos_tabla,md=6,style={'background-color':'#DCDCDC'}),
        html.Br(),html.Br(),html.Br(),
        dbc.Col('Gráfica',md=6,style={'background-color':'#DCDCDC'}),
        dbc.Col(parametros,md=12,style={'background-color':'#DCDCDC'}),


    ])
])