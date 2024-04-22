import dash 
from dash import html, dcc 
import dash_bootstrap_components as dbc

resultados=dbc.Container([
    html.H5("Curvas - Deformación horizontal", style={'text-align': 'center'}),
])


parametros=dbc.Container([
    html.H1("Parámetros del suelo"),
    html.Br(),html.Br(),
    html.Button('Cohesión máxima'),

    html.Div([
        html.Label('Cohesión máxima:', style={'display': 'inline-block', 'margin-right': '10px'}),
        dcc.Input(type='number', value=5, id="Cohesión máxima")
    ]),
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
        dbc.Col('Esfuerzos normales y',md=6,style={'background-color':'green'}),
        dbc.Col('Gráfica',md=6,style={'background-color':'pink'}),
        dbc.Col(parametros,md=12,style={'background-color':'purple'}),

    ])
])