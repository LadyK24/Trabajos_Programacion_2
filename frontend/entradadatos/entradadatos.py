import dash 
from dash import html
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

entrada_datos = dbc.Container([
    dbc.Row([
        dbc.Col(ingresodatos,md=12,style={'background-color':'yellow'}), 
        dbc.Col(caracteristicas,md=6,style={'background-color':'orange'}),
        dbc.Col(Datos_de_corte,md=6,style={'background-color':'gray'}),
        dbc.Col('Tabla con datos',md=12,style={'background-color':'green'}),

    ])
])