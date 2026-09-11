import numpy as np

latencias = [98, 102, 101, 99, 100, 103, 97, 180]

media = np.mean(latencias)
desvio = np.std(latencias)

print(f"Média: {media:.2f} ms")
print(f"Desvio-padrão: {desvio:.2f} ms")

valor = 180
z = (valor - media) / desvio
print(f"\nZ-Score da latência {valor} ms: {z:.2f}")

if abs(z) > 3:
    print("Esse valor merece investigação (|Z| > 3).")
else:
    print("Esse valor está dentro do esperado.")

print("Lembrete: investigar não significa apagar o dado automaticamente.")