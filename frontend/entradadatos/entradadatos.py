import dash 
from dash import html
import dash_bootstrap_components as dbc

entrada_datos = dbc.Container([
    dbc.Row([
        dbc.Col('Ingreso de datos',md=6,style={'background-color':'yellow'}), 
        dbc.Col('Característica de la muestra',md=3,style={'background-color':'orange'}),
        dbc.Col('Datos de corte',md=3,style={'background-color':'gray'}),
        dbc.Col('Tabla con datos',md=3,style={'background-color':'green'}),

    ])
])