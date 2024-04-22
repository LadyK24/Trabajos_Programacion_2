import pandas as pd

Muestra=[
    1,
    2,
    3
]

Normal=[
    1,
    2,
    3
]

Cortante=[
    1,
    2,
    3
]

Residual=[
    1,
    2,
    3
]
esfuerzos= pd.DataFrame({ 
    "Muestra": Muestra,
    "Normal": Normal, 
    "Cortante": Cortante,
    "Residual": Residual, 
})
