import dash 
from dash import html
import dash_bootstrap_components as dbc

corte_directo = dbc.Container([
    html.H1("ENSAYO CORTE DIRECTO",style={'text-align': 'center'})
    


])
subt = dbc.Container([
    html.H1("INV E 154 - 13",style={'text-align': 'center'})
])
titulo = dbc.Container([
    dbc.Row([
        dbc.Col(corte_directo,md=12,style={'background-color':'gray'}),
        dbc.Col(subt,md=12,style={'background-color':'gray'}),
        html.Br(),html.Br()
    ])
])