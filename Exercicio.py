casos = [85, 100, 120]
media = 100
desvio = 10

for valor in casos:
    z = (valor - media) / desvio
    print(f"Valor: {valor}, Z-Score: {z}")
    
for valor in casos:
    z = (valor - media) / desvio
    
    if z <0:
        posicao = "abaixo da média"
    elif z > 0:
        posicao = "acima da média"
    else:
        posicao = "na média"
    print(f"Valor: {valor}, Z-Score: {z}, {posicao}")
    
print("\nResumo dos valores:")

print("\nUm Z-Score negativo indica que o valor está abaixo da média.")
print("Um Z-Score positivo indica que o valor está acima da média.")
print("Um Z-Score igual a zero indica que o valor é igual à média.")