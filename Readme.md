# AnalisisMiBiblioteca

Proyecto en **Python** para la gestión y análisis de datos de una biblioteca.  
Permite cargar clientes, libros y ventas desde archivos CSV, limpiar y estandarizar datos, registrar nuevas ventas y realizar análisis de frecuencia y agregación.

---

## Características principales
- **Carga de datos** desde archivos CSV con manejo de errores.
- **Limpieza de datos**: eliminación de nulos, estandarización de texto y conversión de precios.
- **Registro de ventas** con asignación automática de precios desde el catálogo.
- **Análisis de datos**:
  - Libro más vendido.
  - Producto más vendido.
  - Promedio de precios por categoría.

---

## Estructura del proyecto


---

## Módulos

### `carga.py`
Funciones para cargar archivos CSV:
- `cargar_csv(ruta)`: lee un archivo CSV y devuelve un DataFrame.

### `limpieza.py`
Funciones de limpieza:
- `manejar_nulos(df)`: elimina filas con valores nulos.
- `estandarizar_texto(df, columna)`: convierte texto a minúsculas y elimina espacios.
- `limpiar_moneda(df, columna)`: limpia símbolos de moneda y convierte a `float`.

### `analisis.py`
Funciones de análisis:
- `analisis_frecuencia(df, columna)`: devuelve el elemento más frecuente.
- `analisis_agregacion(df, columna_categoria, columna_valor)`: calcula promedios por categoría.
- `analisis_filtrado(df, columna, condicion)`: filtra y cuenta elementos.
- `registrar_venta(df_ventas, cliente_id, libro_id, libros, cantidad=1, precio=None)`: agrega una nueva venta al DataFrame.

### `main.py`
Orquesta el flujo completo:
1. Carga clientes, libros y ventas.
2. Registra nuevas ventas.
3. Limpia y estandariza datos.
4. Une ventas con títulos de libros.
5. Ejecuta análisis y muestra resultados.

---

## ▶️ Ejecución

1. Clona el repositorio o descarga el proyecto.
2. Instala dependencias:
   ```bash
   pip install pandas

   python main.py