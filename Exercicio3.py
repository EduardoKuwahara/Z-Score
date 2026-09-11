temperaturas = [21, 23, 25, 27, 29]
media = 25
desvio = 2

resultados = []

for t in temperaturas:
    z = (t - media) / desvio
    resultados.append((t, z))
    print(f"Temperatura {t} -> Z = {z}")


mais_incomum = max(resultados, key=lambda x: abs(x[1]))

print(f"\nA leitura mais incomum é {mais_incomum[0]}°C, com Z = {mais_incomum[1]}")