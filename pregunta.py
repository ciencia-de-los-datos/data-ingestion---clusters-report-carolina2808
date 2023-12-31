"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
from typing import List, Tuple

import pandas as pd


def ingest_data():
    column_limits = [(0, 9), (9, 25), (25, 41), (41, 118)]
    column_names = get_column_names(column_limits)

    return (pd.read_fwf('clusters_report.txt',
                        skiprows=4,
                        colspecs=column_limits,
                        header=None,
                        names=column_names,
                        converters={'porcentaje_de_palabras_clave': clean_percentage()})
            .fillna(method='ffill')
            .astype({"cluster": int, "cantidad_de_palabras_clave": int, 'porcentaje_de_palabras_clave': float})
            .groupby([c for c in column_names if c != "principales_palabras_clave"], as_index=False)[column_names[3]]
            .apply(clean_keywords()))


def get_column_names(limits: List[Tuple[int, int]]) -> List[str]:
    return (pd.read_fwf('clusters_report.txt', nrows=2, colspecs=limits, header=None)
            .fillna('')
            .apply(lambda x: ' '.join(x).strip().replace(' ', '_').lower())
            .values)


def clean_percentage():
    return lambda x: x.replace('%', '').replace(',', '.').strip()


def clean_keywords():
    return lambda x: ' '.join(x.apply(
        lambda y: ' '.join(y.replace('.', '').split())
    ))