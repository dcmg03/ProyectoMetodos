import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(0)
x = np.linspace(0, 10, 20)
y = 2 * x + 1 + np.random.normal(0, 1, 20)  # y = 2x + 1 + ruido

# Función para ajustar una línea recta utilizando el método de los mínimos cuadrados
def ajustar_linea(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x ** 2)

    # Calcular los coeficientes de la línea recta (a y b)
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - a * sum_x) / n

    return a, b

# Obtener los coeficientes de la línea ajustada
a, b = ajustar_linea(x, y)

# Calcular los valores ajustados de y
y_ajustado = a * x + b

# Graficar los datos y la línea ajustada
plt.scatter(x, y, label='Datos')
plt.plot(x, y_ajustado, color='red', label='Ajuste lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste lineal utilizando mínimos cuadrados')
plt.grid(True)

# Mostrar el gráfico
plt.show()

print(f"Coeficiente a (pendiente): {a}")
print(f"Coeficiente b (intercepto): {b}")
