import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd


Deformación=[
    0,
    5,		
    10,		
    15,		
    20,		
    30,		
    40,		
    50,		
    65,		
    80,		
    100,		
    120,		
    140,		
    160,		
    180,		
    200,		
    220,		
    240,		
    260,		
    280,		
    300,		
    320,		
    340,		
    360,		
    380,		
    400,		
    420,		
    440,		
    460,		
    480,		
    500
]



Muestra_1_fuerza_cortante=[
    0,
    5,		
    10,		
    15,		
    20,		
    30,		
    40,		
    50,		
    65,		
    80,		
    100,		
    120,		
    140,		
    160,		
    180,		
    200,		
    220,		
    240,		
    260,		
    280,		
    300,		
    320,		
    340,		
    360,		
    380,		
    400,		
    420,		
    440,		
    460,		
    480,		
    500
]

Muestra_2_fuerza_cortante=[
    0,
    5,		
    10,		
    15,		
    20,		
    30,		
    40,		
    50,		
    65,		
    80,		
    100,		
    120,		
    140,		
    160,		
    180,		
    200,		
    220,		
    240,		
    260,		
    280,		
    300,		
    320,		
    340,		
    360,		
    380,		
    400,		
    420,		
    440,		
    460,		
    480,		
    500
]

cortedirecto = pd.DataFrame({
    "Deformación (mm)": Deformación,
    "Muestra 2. Fuerza cortante (N)": Muestra_1_fuerza_cortante,
    "Muestra 1. Fuerza cortante (N)": Muestra_2_fuerza_cortante
})