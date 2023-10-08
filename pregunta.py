"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
def ingest_data():
    # Lee el archivo 'clusters_report.txt'
    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()
    # Elimina líneas en blanco y líneas de separación
    lines = [line.strip() for line in lines if line.strip() and not line.startswith('-')]
    # Separa las primeras tres columnas y combina el resto en la última columna
    data = []
    for line in lines:
        parts = line.split()
        data.append(parts[:3] + [' '.join(parts[3:])])
    # Crea DF
    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    return df