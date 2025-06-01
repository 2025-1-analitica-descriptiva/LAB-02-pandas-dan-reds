"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    import pandas as pd

    ruta = r"C:/Users/danie/Documents/GitHub/LAB-02-pandas-dan-reds/files/input/tbl1.tsv"
    data = pd.read_csv(ruta, sep="\t")
    lista = sorted(data["c4"].astype(str).str.upper().unique())
    return lista
