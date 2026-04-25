import pandas as pd

def analisis_frecuencia(df, columna):
    """Elemento con mayor frecuencia."""
    return df[columna].value_counts().idxmax()

def analisis_agregacion(df, columna_categoria, columna_valor):
    """Agrupación y suma/promedio."""
    return df.groupby(columna_categoria)[columna_valor].mean()

def analisis_filtrado(df, columna, condicion):
    """Filtrar y contar elementos."""
    return df[df[columna] == condicion].shape[0]

