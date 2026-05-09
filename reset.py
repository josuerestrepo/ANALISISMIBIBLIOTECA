import pandas as pd

# Definir las columnas que debe tener la tabla de ventas
columnas = ["id_venta,cliente_id,libro_id,precio,categoria_id,cantidad"]

# Crear un DataFrame vacío con esas columnas
ventas = pd.DataFrame(columns=columnas)

# Guardar el archivo sobrescribiendo el existente
ventas.to_csv("data/ventas.csv", index=False)

print("La tabla de ventas ha sido borrada. Solo quedan los encabezados.")