media = 100
desvio = 5
valor = 115

distancia = valor - media
print("Distância do valor em relação à média:", distancia)

quantos_desvios = distancia / desvio
print("Número de desvios padrão que o valor está da média:", quantos_desvios)

z = quantos_desvios
print("O Z-Score do valor é:", z)

print(f"O valor {valor} está a {z} desvios padrão da média de {media}.")
