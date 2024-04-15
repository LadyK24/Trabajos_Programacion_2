import dash 
from dash import html
import dash_bootstrap_components as dbc

caracteristicas=dbc.Container([
    html.H1("Características de la muestra"),
    html.Button('Diametro'),
    html.Button('Altura')
])

Datos_de_corte=dbc.Container([
    html.H1("Datos de corte"),
    html.Button('Sobre carga'),
    html.Button('Carga nominal')
])

entrada_datos = dbc.Container([
    dbc.Row([
        dbc.Col('Ingreso de datos',md=12,style={'background-color':'yellow'}), 
        dbc.Col(caracteristicas,md=6,style={'background-color':'orange'}),
        dbc.Col(Datos_de_corte,md=6,style={'background-color':'gray'}),
        dbc.Col('Tabla con datos',md=12,style={'background-color':'green'}),

    ])
])