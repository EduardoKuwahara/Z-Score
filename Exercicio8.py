import pandas as pd
import numpy as np

dados = {
    "Usuario": ["ana", "bruno", "carla", "diego", "eva", "fabio"],
    "Requisicoes": [120, 135, 128, 122, 130, 400]
}
df = pd.DataFrame(dados)

media = df["Requisicoes"].mean()
desvio = df["Requisicoes"].std()

print(f"Média: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}\n")

df["Z_Score"] = (df["Requisicoes"] - media) / desvio
df["Status"] = df["Z_Score"].apply(lambda z: "Investigar" if abs(z) > 3 else "Comum")

print(df, "\n")

investigar = df[df["Status"] == "Investigar"]
print("Linhas marcadas para investigação:")
print(investigar)