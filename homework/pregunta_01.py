"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import os
import pandas as pd
import re

def limpiar_texto(serie: pd.Series) -> pd.Series:
    """
    Limpieza general de texto:
    - convierte a string
    - minúsculas
    - reemplaza _ y - por espacios
    - elimina puntos
    - elimina espacios extra
    """
    return (
        serie.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[_\-]", " ", regex=True)
        .str.replace(r"\.", "", regex=True)
        .str.replace(r"\s+", " ", regex=True)
    )

def limpiar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia nombres de columnas con la misma lógica.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"\.", "", regex=True)
        .str.replace(r"\s+", " ", regex=True)
    )
    return df

def pregunta_01():
    input_path = "files/input/solicitudes_de_credito.csv"
    output_path = "files/output/solicitudes_de_credito.csv"

    os.makedirs("files/output", exist_ok=True)

    # Leer datos
    df = pd.read_csv(input_path, sep=";")

    # Limpiar columnas
    df = limpiar_columnas(df)

    # Eliminar columnas basura tipo Excel
    df = df.loc[:, ~df.columns.str.contains("^unnamed")]

    # Limpiar texto en todas las columnas object
    for col in df.select_dtypes(include="object").columns:
        df[col] = limpiar_texto(df[col])

    # Eliminar duplicados y nulos
    df = df.drop_duplicates()
    df = df.dropna()
    return df

    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """