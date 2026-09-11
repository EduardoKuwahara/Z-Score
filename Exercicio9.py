import numpy as np

dados = [10, 11, 12, 12, 13, 13, 14, 15, 30]

# IQR
q1 = np.percentile(dados, 25)
q3 = np.percentile(dados, 75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")

# Z-Score
media = np.mean(dados)
desvio = np.std(dados)
z_30 = (30 - media) / desvio

print(f"\nMédia: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")
print(f"Z-Score de 30: {z_30:.2f}")

# Comparação
print("\nComparação:")
if 30 < limite_inferior or 30 > limite_superior:
    print(f"Pelo IQR, 30 É considerado outlier (fora do intervalo [{limite_inferior:.2f}, {limite_superior:.2f}]).")
else:
    print(f"Pelo IQR, 30 NÃO é considerado outlier.")

if abs(z_30) > 3:
    print(f"Pelo Z-Score, 30 É considerado outlier (|Z| = {abs(z_30):.2f} > 3).")
else:
    print(f"Pelo Z-Score, 30 NÃO é considerado outlier (|Z| = {abs(z_30):.2f}, abaixo de 3).")

print("\nConclusão:")
print("O IQR e o Z-Score podem discordar sobre o mesmo dado. O IQR se baseia na")
print("posição dos quartis e é menos sensível a valores extremos, enquanto o Z-Score")
print("usa a média e o desvio-padrão, que são diretamente afetados pelo próprio outlier.")
print("Por isso, técnicas diferentes podem chegar a conclusões diferentes sobre o mesmo dado.")