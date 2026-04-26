import pandas as pd

def cargar_csv(ruta, sep=",", encoding="utf-8"):
    try:
        df = pd.read_csv(ruta, sep=sep, encoding=encoding)
        print(f"Archivo '{ruta}' cargado correctamente. Filas: {len(df)}")
        return df
    except FileNotFoundError:
        print(f"Error: el archivo '{ruta}' no existe.")
        return None
    except Exception as e:
        print(f"Error al cargar '{ruta}': {e}")
        return None