import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from scipy.optimize import minimize_scalar

def trapecio(fun, ai, bi, ntrap):
    plt.clf()
    # ENTRADAS

    x = sym.Symbol('x')
    fx = sym.lambdify(x, fun, 'numpy')
    a = float(ai)
    b = float(bi)
    dfx = sym.diff(fx(x), x, 2)
    medio = (b - a) / 2

    mInterval = dfx.subs(x, medio)
    n_trapecios = int(ntrap)
    # VALOR DE h
    h = (b - a) / n_trapecios

    # Numero de puntos
    puntos = n_trapecios + 1
    area_bajo = 0
    x = a
    trapecios_x = []
    trapecios_y = []

    if n_trapecios == 1:
        area_bajo = h * (fx(a) + fx(b)) / 2

    elif n_trapecios > 1:
        for i in range(0, n_trapecios, 1):
            trapecio_x = [x, x + h, x + h, x, x]
            trapecio_y = [0, 0, fx(x + h), fx(x), 0]

            trapecios_x.extend(trapecio_x)
            trapecios_y.extend(trapecio_y)

            area = h * (fx(x) + fx(x + h)) / 2
            area_bajo = area_bajo + area
            x = x + h
    else:
        print("Ingrese un numero válido de trapecios")

    error = ((b - a) ** 3 / (12 * n_trapecios ** 2)) * abs(mInterval)

    x_vals = np.linspace(a, b, 400)
    fx_vals = fx(x_vals)

    #print("\nCantidad de trapecios:", n_trapecios)
    #print("El area bajo la curva corresponde a:", area_bajo)
    #print("Error:", error)

    # Gráfica de f(x) y trapecios
    plt.plot(x_vals, fx_vals, label="f(x)")
    plt.fill_between(x_vals, 0, fx_vals, color='yellow', alpha=0.3)
    plt.plot(trapecios_x, trapecios_y, color='green', label='Trapecios')
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(a, color='red', linestyle='dashed', linewidth=1.5, label='a')
    plt.axvline(b, color='blue', linestyle='dashed', linewidth=1.5, label='b')
    plt.title("Área bajo la Curva y Trapecios")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    #plt.show()

    return [plt.gcf(), n_trapecios, area_bajo, error]
