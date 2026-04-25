import pandas as pd
def cargar_csv(ruta):
    
    try:
        df = pd.read_csv(ruta)
        print(f"archivo cargado corretamente")
        return df 
    except Exception as e :
        print(f"Error al cargar")
        return None