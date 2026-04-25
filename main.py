
from carga import cargar_csv
from limpieza import manejar_nulos, estandarizar_texto, limpiar_moneda
from analisis import analisis_frecuencia, analisis_agregacion, analisis_filtrado
import pandas as pd
from analisis import registrar_venta

clientes = cargar_csv("data/clientes.csv")
libros = cargar_csv("data/libros.csv")
ventas = cargar_csv("data/ventas.csv")

ventas = registrar_venta(ventas, clientes_id =1, libro_id=3)
ventas.to_csv("data/ventas.csv", index=False)
print(ventas)

clientes = manejar_nulos(clientes)
ventas = limpiar_moneda(ventas, "precio")

clientes = estandarizar_texto(clientes, "nombre")


print("Producto más vendido:", analisis_frecuencia(ventas, "producto"))
print("Promedio de precio por categoría:", analisis_agregacion(ventas, "categoria", "precio"))
print("Libros de Gabriel García Márquez prestados:", analisis_filtrado(ventas, "autor", "Gabriel García Márquez"))

