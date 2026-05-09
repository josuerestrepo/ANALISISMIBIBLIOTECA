import matplotlib.pyplot as plt
import pandas as pd

def grafico_ventas(ventas_df):

    resumen = ventas_df.groupby("libro_id")["cantidad"].sum()

    resumen.plot(kind="bar")

    plt.title("Ventas por libro")
    plt.xlabel("Libro ID")
    plt.ylabel("Cantidad vendida")

    plt.tight_layout()

    plt.show()

ventas_df = pd.read_csv("data/ventas.csv")

grafico_ventas(ventas_df)
