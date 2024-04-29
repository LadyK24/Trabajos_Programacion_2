import dash 
from dash import html
import dash_bootstrap_components as dbc

ensayo=dbc.Container([
    html.H5("Descripción: tiene como objetivo principal determinar la resistencia al corte de materiales granulares,lo que proporciona información crucial para el diseño y la construcción de estructuras de ingeniería.")

])

descripcion = dbc.Container([
    dbc.Row([
        dbc.Col(ensayo,md=12,style={'background-color':'#DCDCDC'},)
        
    ])
])