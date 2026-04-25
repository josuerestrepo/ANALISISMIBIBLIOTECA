import pandas as pd 


def manejar_nulos(df):
    return df.dropna()

def estandarizar_texto(df, columna):
    df[columna] = df[columna].str.lower().str.strip()
    return df

def limpiar_moneda(df, columna):
    df[columna] = df[columna].replace('[\$,]', '', regex=True).astype(float)
  
    return df
