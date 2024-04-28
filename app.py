import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd


#importar el frontend
from frontend.frontend import layout

from backend1.cortedirecto import cortedirecto


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = layout


# Definiión del diámetro

@app.callback(
    Output('salidaarea', 'children'),
    Input('Diametro','value'),
)


def area(Diametro):
    calculoarea = Diametro **2 
    return 'area:' +str(calculoarea)


# Definición de la tabla 

@app.callback(
    Output('tabla_cortedirecto', 'data'),
    Input('tabla_cortedirecto', 'data'),
    Input('tabla_cortedirecto', 'columns')
)

def update_cortedirecto_table(rows,columns):
    cortedirecto=pd.DataFrame(rows)

    cortedirecto['Fuerza1'] = cortedirecto['Fuerza1'].astype("int")
    cortedirecto['Fuerza2'] = cortedirecto['Fuerza2'].astype("int")
    cortedirecto['Fuerza3'] = cortedirecto['Fuerza3'].astype("int")

    cortedirecto["Esfuerzo1"]=round((cortedirecto["Fuerza1"]/9.81)/(36 /(1-((cortedirecto["Deformacion"]/100)/(2*10)))),2)
    cortedirecto["Esfuerzo2"]=round((cortedirecto["Fuerza2"]/9.81)/(36 /(1-((cortedirecto["Deformacion"]/100)/(2*10)))),2)
    cortedirecto["Esfuerzo3"]=round((cortedirecto["Fuerza3"]/9.81)/(36 /(1-((cortedirecto["Deformacion"]/100)/(2*10)))),2)
    
    return cortedirecto.to_dict('records')


# Definición de la grafica 

@app.callback(
    Output('cortedirecto_plot','figure'),
    Input('tabla_cortedirecto','data')
)




def update_cortedirecto_plot(rows):
    
    cortedirecto = pd.DataFrame(rows)

    trace1 = go.Scatter(
        x=cortedirecto["Deformacion"],
        y=cortedirecto["Esfuerzo1"],
        mode='lines',
        name='Esfuerzo 1',
        line=dict(color='blue'),
    )

    trace2 = go.Scatter(
        x=cortedirecto["Deformacion"],
        y=cortedirecto["Esfuerzo2"],
        mode='lines',
        name='Esfuerzo 2',
        line=dict(color='red'),
    )

    trace3 = go.Scatter(
        x=cortedirecto["Deformacion"],
        y=cortedirecto["Esfuerzo3"],
        mode='lines',
        name='Esfuerzo 3',
        line=dict(color='green'),
    )

    fig = go.Figure(data=[trace1, trace2, trace3])

    fig.update_layout(
        title={
            'text': 'Esfuerzo vs deformación',
            'x':0.5,  # Centrar horizontalmente
            'y':0.9,  # Ajustar la posición vertical si es necesario
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='Deformación horizontal (mm)',
        yaxis_title='Esfuerzo cortante (kg/cm2)'
    )

    return fig 


if __name__ == '__main__':
    app.run_server(debug=True)
        


app = dash.Dash(__name__external_stylesheets=[dbc.themes.BOOTSTRAP])

