import pandas as pd

dados = {
    "Evento": ["A", "B", "C", "D", "E", "F", "G"],
    "Tentativas_Login": [3, 4, 2, 5, 3, 4, 40]
}
df = pd.DataFrame(dados)

media = df["Tentativas_Login"].mean()
desvio = df["Tentativas_Login"].std()

print(f"Média: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}\n")

df["Z_Score"] = (df["Tentativas_Login"] - media) / desvio

print(df, "\n")

eventos_criticos = df[df["Z_Score"].abs() > 3]

print("Eventos com |Z| > 3 (merecem investigação):")
print(eventos_criticos, "\n")

print("Mensagem final:")
print("Em segurança da informação, um evento raro não deve ser descartado como ruído.")
print("Diferente de outras áreas, onde um outlier pode ser só uma variação natural,")
print("um valor incomum de tentativas de login pode indicar um ataque de força bruta")
print("em andamento. Por isso, o dado mais 'estranho' estatisticamente é, muitas vezes,")
print("o dado mais importante para a análise de segurança.")