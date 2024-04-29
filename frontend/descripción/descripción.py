import dash 
from dash import html
import dash_bootstrap_components as dbc

ensayo=dbc.Container([
<<<<<<< HEAD
    html.H5("Descripción: Determinar la resitencia al corte de una muetra de suelo consolidado y drenado...")
=======
    html.H5("Descripción: Determinar la resitencia al corte de una muetra de suelo consolidado y drenado......")
    #Añadir más descripción
>>>>>>> a6764733d9add19721f0dcdfea2961125b00fa6a

])

descripcion = dbc.Container([
    dbc.Row([
        dbc.Col(ensayo,md=12,style={'background-color':'#DCDCDC'},)
        
    ])
])