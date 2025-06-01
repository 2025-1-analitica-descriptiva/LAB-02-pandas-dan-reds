"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    import pandas as pd

    ruta = r"C:/Users/danie/Documents/GitHub/LAB-02-pandas-dan-reds/files/input/tbl0.tsv"
    db = pd.read_csv(ruta, sep="\t")
    filas = db.shape[0]
    return filas

print(pregunta_01())
