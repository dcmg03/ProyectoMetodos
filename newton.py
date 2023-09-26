import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def newton_raphson_method(func, derivative_func, x0, tol=1e-6, max_iter=100):
    x = x0
    num_iterations = 0
    while abs(func(x)) > tol and num_iterations < max_iter:
        x = x - func(x) / derivative_func(x)
        num_iterations += 1
    return x, num_iterations

# Solicitar entrada al usuario para la función
expression = input("Ingrese la función (por ejemplo, 'x**3 - 5*x + 27'): ")
x_symbol = sp.symbols('x')
func = sp.sympify(expression)
func_numeric = sp.lambdify(x_symbol, func, 'numpy')

# Solicitar entrada al usuario para la derivada
derivative_expression = input("Ingrese la derivada de la función (por ejemplo, '3*x**2 - 5'): ")
derivative_func = sp.sympify(derivative_expression)
derivative_func_numeric = sp.lambdify(x_symbol, derivative_func, 'numpy')

# Solicitar entrada al usuario para x0
x0 = float(input("Ingrese la aproximación inicial (x0): "))

# Solicitar entrada al usuario para la tolerancia
tolerancia = float(input("Ingrese la tolerancia (por ejemplo, 1e-6): "))

# Solicitar entrada al usuario para el máximo de iteraciones
max_iteraciones = int(input("Ingrese el número máximo de iteraciones: "))

root, num_iterations = newton_raphson_method(func_numeric, derivative_func_numeric, x0, tol=tolerancia, max_iter=max_iteraciones)

# Utilizar lambdify para obtener una función numérica que pueda ser evaluada
func_numeric = sp.lambdify(x_symbol, func, 'numpy')

# Calcular el valor de la función en la raíz
func_value_at_root = func_numeric(root)

# Calcular el error porcentual
error_porcentual = abs(func_value_at_root) * 100

print(f"Aproximación de la raíz: {root}")
print(f"Valor de la función en la raíz: {func_value_at_root}")
print(f"Número de iteraciones: {num_iterations}")
print(f"Error porcentual: {error_porcentual:.6f}%")

x_vals = np.linspace(root - 2, root + 2, 100)
y_vals = func_numeric(x_vals)

plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='red')
plt.axvline(root, color='green')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.title('Gráfica de la función y aproximación de la raíz')
plt.show()
