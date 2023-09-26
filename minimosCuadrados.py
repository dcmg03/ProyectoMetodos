import numpy as np

# Solicitar al usuario el número de puntos de datos
n = int(input("Ingrese el número de puntos de datos: "))

# Solicitar al usuario ingresar los puntos de datos (x, y)
x = np.zeros(n)
y = np.zeros(n)

for i in range(n):
    x[i] = float(input(f"Ingrese el valor de x{i + 1}: "))
    y[i] = float(input(f"Ingrese el valor de y{i + 1}: "))

# Ajuste de mínimos cuadrados lineal (y = mx + b)
A = np.vstack([x, np.ones(n)]).T
m, b = np.linalg.lstsq(A, y, rcond=None)[0]

# Imprimir los coeficientes del ajuste
print(f"Pendiente (m): {m}")
print(f"Ordenada al origen (b): {b}")

# Predicción de valores ajustados
y_pred = m * x + b

# Imprimir valores ajustados
print("Valores ajustados:")
for i in range(n):
    print(f"x = {x[i]}, y = {y_pred[i]}")
