import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc

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
    html.H3("Igrese sus datos en deformación y fueza"),
    dash_table.DataTable(
        id= 'tabla_corte_directo',
        columns=[
            {'name':'Deformación','id':'Deformación','editable':False},
        ],
        #data=
    )

])


entrada_datos = dbc.Container([
    dbc.Row([
        dbc.Col(ingresodatos,md=12,style={'background-color':'yellow'}), 
        dbc.Col(caracteristicas,md=6,style={'background-color':'orange'}),
        dbc.Col(Datos_de_corte,md=6,style={'background-color':'gray'}),
        dbc.Col(tabla_datos,md=12,style={'background-color':'green'}),

    ])
])