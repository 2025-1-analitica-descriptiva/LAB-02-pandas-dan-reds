"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """
    import pandas as pd

    ruta = r"C:/Users/danie/Documents/GitHub/LAB-02-pandas-dan-reds/files/input/tbl0.tsv"
    data = pd.read_csv(ruta, sep="\t")
    suma = data.groupby("c1")["c2"].sum()
    return suma
