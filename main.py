from carga import cargar_csv
from limpieza import manejar_nulos, estandarizar_texto, limpiar_moneda
from analisis import analisis_frecuencia, analisis_agregacion, analisis_filtrado, registrar_venta
import pandas as pd

# Cargar datos
clientes = cargar_csv("data/clientes.csv")
libros = cargar_csv("data/libros.csv")
ventas = cargar_csv("data/ventas.csv")

# Registrar ventas con precios automáticos desde el catálogo
ventas = registrar_venta(ventas, cliente_id=1, libro_id=3, libros=libros)
ventas = registrar_venta(ventas, cliente_id=3, libro_id=4, libros=libros)
ventas = registrar_venta(ventas, cliente_id=1, libro_id=5, libros=libros)
ventas = registrar_venta(ventas, cliente_id=2, libro_id=5, libros=libros)
ventas = registrar_venta(ventas, cliente_id=6, libro_id=6, libros=libros)

# Guardar ventas actualizadas
ventas.to_csv("data/ventas.csv", index=False)

# Limpieza de datos
clientes = manejar_nulos(clientes)
clientes = estandarizar_texto(clientes, "nombre")
ventas = limpiar_moneda(ventas, "precio")

# Merge con títulos de libros
ventas = ventas.merge(libros[['libro_id', 'titulo']], on='libro_id', how='left')


# Análisis
print("Libro más vendido:", analisis_frecuencia(ventas, "titulo"))
print("Producto más vendido:", analisis_frecuencia(ventas, "libro_id"))
print("Promedio de precio por categoría:", analisis_agregacion(ventas, "libro_id", "precio"))