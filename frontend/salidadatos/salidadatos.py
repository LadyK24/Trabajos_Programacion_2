import dash 
from dash import html
import dash_bootstrap_components as dbc

salida_datos = dbc.Container([
    dbc.Row([
        dbc.Col('Curvas - Deformación horizontal',md=12,style={'background-color':'yellow'}), 
        dbc.Col('Tabla - Deformaciones y esfuerzo',md=6,style={'background-color':'orange'}),
        dbc.Col('Gráfica',md=6,style={'background-color':'gray'}),
        dbc.Col('Esfuerzos normales y',md=12,style={'background-color':'green'}),
        dbc.Col('Gráfica',md=12,style={'background-color':'pink'}),
        dbc.Col('Parámetros del suelo',md=12,style={'background-color':'purple'}),

    ])
])