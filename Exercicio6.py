media_a = 100
desvio_a = 2
media_b = 100
desvio_b = 20
valor = 110

z_a = (valor - media_a) / desvio_a
z_b = (valor - media_b) / desvio_b

print(f"Grupo A -> Z-Score = {z_a:.2f}")
print(f"Grupo B -> Z-Score = {z_b:.2f}")

print("\nComparação:")
print(f"A distância absoluta é a mesma nos dois grupos: {valor - media_a} unidades.")
print(f"No Grupo A, o Z-Score é {z_a:.2f}, um valor bem alto, indicando algo muito incomum.")
print(f"No Grupo B, o Z-Score é {z_b:.2f}, um valor baixo, indicando algo dentro do esperado.")

print("\nConclusão:")
print("A mesma distância absoluta (10 unidades) pode ser rara ou comum dependendo")
print("da dispersão dos dados. Quando o desvio-padrão é pequeno (Grupo A), os valores")
print("estão muito concentrados perto da média, então um desvio de 10 é extremo.")
print("Quando o desvio-padrão é grande (Grupo B), os dados já variam bastante por")
print("natureza, então o mesmo desvio de 10 é considerado normal.")