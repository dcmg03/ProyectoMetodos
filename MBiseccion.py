import numpy as np
import matplotlib.pyplot as plt

#Ingreso
def biseccion(f,a,b):
    input=f
    fx =lambda x:eval(input)
    # fx = lambda x: -0.5*(x**2) + 2.5*x + 4.5
    x = np.linspace(-10, 10, 1000)

    xi = float(a)
    xu = float(b)
    ant = 1
    error = 0.5
    tabla = []

    while error > 0.001:
        xr = (xi+xu)/2
        fxi = fx(xi)
        fxr = fx(xr)
        f = fxi*fxr
        if f > 0:
            xi = xr
        if f < 0:
            xu = xr
        error = abs((xr-ant)/xr)*100
        tabla.append([xi, xu, xr, fxi, fxr, f])
        ant = xr

    tabla = np.array(tabla)

    #print('[xi, xu, xr, fxi, fxr, f]')
    #print(tabla)
    #print('Error: ', error)
    #print('Raiz en: ', xr)
    fi = fx(x)
    plt.axvline(0, color='k')
    plt.axhline(0, 0, color='k')
    plt.title('Bisección')
    plt.plot(x,fi,'c')
    if xi != np.nan:
        plt.axvline(xi)
    plt.plot(xi, 0, 'ro')
    return [plt.gcf(), tabla, error, xr]