import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import math


#importar el frontend
from frontend.frontend import layout


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = layout

# Definición de la tabla 

@app.callback(
    Output('tabla_cortedirecto', 'data'),
    Input('tabla_cortedirecto', 'data'),
    Input('tabla_cortedirecto', 'columns'),
    Input('Diametro','value'),
    Input('Altura','value'),
    
)

def update_cortedirecto_table(rows,columns,Diametro,Altura):
    calculoAarea = (math.pi * Diametro **2 )/4 
    
    cortedirecto=pd.DataFrame(rows)

    cortedirecto['Fuerza1'] = cortedirecto['Fuerza1'].astype("int")
    cortedirecto['Fuerza2'] = cortedirecto['Fuerza2'].astype("int")
    cortedirecto['Fuerza3'] = cortedirecto['Fuerza3'].astype("int")

    cortedirecto["Esfuerzo1"]=round((cortedirecto["Fuerza1"]/9.81)/(calculoAarea /(1-((cortedirecto["Deformacion"]/100)/(Altura*10)))),2)#AGREGUÉ EN LA ECUACIÓN
    cortedirecto["Esfuerzo2"]=round((cortedirecto["Fuerza2"]/9.81)/(calculoAarea /(1-((cortedirecto["Deformacion"]/100)/(Altura*10)))),2)#AGREGUÉ EN LA ECUACIÓN
    cortedirecto["Esfuerzo3"]=round((cortedirecto["Fuerza3"]/9.81)/(calculoAarea /(1-((cortedirecto["Deformacion"]/100)/(Altura*10)))),2)#AGREGUÉ EN LA ECUACIÓN
    
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





# Definición de la tabla 
@app.callback(
    Output('esfuerzos_tabla_dataframe', 'data'),    
    Input('Diametro','value'),
    Input('Sobrecarga','value'),
    Input('Relacioncarga1','value'),
    Input('Relacioncarga2','value'),
    Input('Relacioncarga3','value'),
    Input('tabla_cortedirecto', 'data'),
    Input('tabla_cortedirecto', 'columns'),
    Input('Altura','value'),#AGREGUÉ ALTURA
)

def update_esfuerzos_table(Diametro, Sobrecarga,  Relacioncarga1, Relacioncarga2, Relacioncarga3,rows,columns,Altura):
    
    cortedirecto = pd.DataFrame(rows)
    calculoAarea = (math.pi * Diametro **2 )/4 

    cortedirecto['Fuerza1'] = cortedirecto['Fuerza1'].astype("int")
    cortedirecto['Fuerza2'] = cortedirecto['Fuerza2'].astype("int")
    cortedirecto['Fuerza3'] = cortedirecto['Fuerza3'].astype("int")

    cortedirecto["Esfuerzo1"]=round((cortedirecto["Fuerza1"]/9.81)/(calculoAarea /(1-((cortedirecto["Deformacion"]/100)/(Altura*10)))),2)#AGREGUÉ EN LA ECUACIÓN
    cortedirecto["Esfuerzo2"]=round((cortedirecto["Fuerza2"]/9.81)/(calculoAarea /(1-((cortedirecto["Deformacion"]/100)/(Altura*10)))),2)#AGREGUÉ EN LA ECUACIÓN
    cortedirecto["Esfuerzo3"]=round((cortedirecto["Fuerza3"]/9.81)/(calculoAarea /(1-((cortedirecto["Deformacion"]/100)/(Altura*10)))),2)#AGREGUÉ EN LA ECUACIÓN
    
    
    #Calcular esfuerzo normal
    
    normal1 = round(((((math.pi * Diametro **2 )/4 )*Relacioncarga1)+ Sobrecarga/1000)/((math.pi * Diametro **2 )/4),2)
    normal2 = round(((((math.pi * Diametro **2 )/4 )*Relacioncarga2)+ Sobrecarga/1000)/((math.pi * Diametro **2 )/4),2)
    normal3 = round(((((math.pi * Diametro **2 )/4 )*Relacioncarga3)+ Sobrecarga/1000)/((math.pi * Diametro **2 )/4),2)

    # Calcular los máximos de los esfuerzos 1, 2 y 3
    max_esfuerzo_lab1 = cortedirecto["Esfuerzo1"].max()
    max_esfuerzo_lab2 = cortedirecto["Esfuerzo2"].max()
    max_esfuerzo_lab3 = cortedirecto["Esfuerzo3"].max()
    
    
    # Extraer la última fila de los esfuerzos 1, 2 y 3 del dataframe cortedirecto
    esfuerzo_residual_lab1 = cortedirecto["Esfuerzo1"].loc[30]
    esfuerzo_residual_lab2 = cortedirecto["Esfuerzo2"].loc[30]
    esfuerzo_residual_lab3 = cortedirecto["Esfuerzo3"].loc[30]
    
    # Añadir los máximos y el esfuerzo residual a las columnas "Cortante" y "Residual" de la tabla esfuerzos

    
    esfuerzos = pd.DataFrame()
    
    Muestra=[
        1,
        2,
        3
    ]


    esfuerzos= pd.DataFrame({ 
        "Muestra": Muestra,
        "Normal": [normal1, normal2, normal3],
        "Cortante": [max_esfuerzo_lab1, max_esfuerzo_lab2, max_esfuerzo_lab3],
        "Residual": [esfuerzo_residual_lab1, esfuerzo_residual_lab2, esfuerzo_residual_lab3]
    })

    

    return esfuerzos.to_dict('records')


# Definición de la grafica 

@app.callback(
    Output('Esfuerzos_plot','figure'),
    Input('esfuerzos_tabla_dataframe','data')
)


def update_esfuerzos_plot(rows):
    
    esfuerzos = pd.DataFrame(rows)

    trace = go.Scatter(
        x=esfuerzos["Normal"],
        y=esfuerzos["Cortante"],
        mode='lines',
        name='Esfuerzos_name',
        line=dict(color='blue'),
    )


    fig = go.Figure(data=[trace])

    fig.update_layout(
        title={
            'text': 'Esfuerzo Normal vs Esfuerzo Cortante',
            'x':0.5,  # Centrar horizontalmente
            'y':0.9,  # Ajustar la posición vertical si es necesario
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='Esfuerzo Normal (kg/cm2)',
        yaxis_title='Esfuerzo Cortante (kg/cm2)'
    )

    return fig 




if __name__ == '__main__':
    app.run_server(debug=True)
        


app = dash.Dash(__name__external_stylesheets=[dbc.themes.BOOTSTRAP])