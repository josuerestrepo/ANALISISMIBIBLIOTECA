import pandas as pd
import random

# Generar 100 clientes ficticios
clientes = []
for i in range(1, 101):
    cliente = {
        "cliente_id": i,
        "nombre": f"Cliente{i}",
        "email": f"cliente{i}@correo.com",
        "telefono": f"+57{random.randint(3000000000, 3999999999)}"
    }
    clientes.append(cliente)

df_clientes = pd.DataFrame(clientes)
df_clientes.to_csv("data/clientes.csv", index=False)

