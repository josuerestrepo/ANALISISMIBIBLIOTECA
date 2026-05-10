import requests
import pandas as pd


url = "http://localhost:8080/api/libro"
response = requests.get(url)

if response.status_code == 200:
    
    datos = response.json()
    print("peticion exitosa")
    print("tipo de datos:", type(datos))
    
    df = pd.DataFrame(datos)
    print("DataFrame creado:")
    print(df)
else:
    print(f"Error en la petición: {response.status_code}")