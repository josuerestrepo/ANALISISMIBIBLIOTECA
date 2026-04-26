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

def registrar_venta(df_ventas, cliente_id, libro_id, libros, cantidad=1, precio=None):
    """Agrega una nueva venta al DataFrame de ventas."""
    if precio is None:
        # Buscar el precio del libro en el catálogo
        precio_libro = libros.loc[libros['libro_id'] == libro_id, 'precio']
        if not precio_libro.empty:
            precio = float(precio_libro.values[0])
        else:
            precio = 0.0  # valor por defecto si no se encuentra

    nueva_venta = {
        "id_venta": len(df_ventas) + 1,
        "cliente_id": cliente_id,
        "libro_id": libro_id,
        "cantidad": cantidad,
        "precio": precio
    }

    return pd.concat([df_ventas, pd.DataFrame([nueva_venta])], ignore_index=True)
    
    
