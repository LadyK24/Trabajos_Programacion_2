import dash 
from dash import html
import dash_bootstrap_components as dbc

resultados=dbc.Container([
    html.H2("Curvas - Deformación horizontal"),
    html.Br(),html.Br(),
])


parametros=dbc.Container([
    html.H1("Parámetros del suelo"),
    html.Br(),html.Br(),
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
        dbc.Col(resultados,md=12,style={'background-color':'yellow'}), 
        dbc.Col('Tabla - Deformaciones y esfuerzo',md=6,style={'background-color':'orange'}),
        dbc.Col('Gráfica',md=6,style={'background-color':'gray'}),
        dbc.Col('Esfuerzos normales y',md=6,style={'background-color':'green'}),
        dbc.Col('Gráfica',md=6,style={'background-color':'pink'}),
        dbc.Col(parametros,md=12,style={'background-color':'purple'}),

    ])
])