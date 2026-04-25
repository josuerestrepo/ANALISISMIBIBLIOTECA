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

def registrar_venta(df_ventas, cliente_id, libro_id, cantidad=1):
    """Agrega una nueva venta al DataFrame de ventas."""
    nueva_venta = {
        "cliente_id": cliente_id,
        "libro_id": libro_id,
        "cantidad": cantidad
    }
    return pd.concat([df_ventas, pd.DataFrame([nueva_venta])], ignore_index=True)
