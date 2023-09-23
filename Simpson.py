import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def simpson(f,ai,bi,trap):
    e = np.exp(1)
    y=sym.Symbol('y')
    x= sym.Symbol('x')
    input=f
    f =lambda x:eval(input)
    a=float(ai)
    b=float(bi)
    n_trapecios=int(trap)
    graficar=False
    medio=(b-a)/2
    h = (b - a) / n_trapecios
    dr4 = abs(f(a) - 4 * f(medio) + 6 * f((a + medio) / 2) + f(b)) / (h ** 4)
    aux = a


    if n_trapecios == 2:
        T = (h / 6 * n_trapecios) * (f(a) + 4 * f((b - a) / 2) + f(b))
        print('El area bajo la curva es: ', np.abs(T))
        x = np.linspace(a, b, n_trapecios + 1)
        y = f(x)
        error = ((b - a) ** 5 / (180 * n_trapecios ** 4)) * dr4
        graficar=True
    elif n_trapecios > 2 and n_trapecios % 2 == 0:
        try:
            sum = 0
            for i in range(1, n_trapecios + 1):
                pmedio = (aux + (h / 2))
                sum = sum + f(pmedio)
                aux = aux + h
            x = np.linspace(a, b, n_trapecios + 1)
            y = f(x)
            T = ((b - a) / (6 * n_trapecios)) * (f(a) + 4 * sum + 2 * np.sum(y[1:-1]) + f(b))
            #print('El area bajo la curva es: ', np.abs(T))
            error = ((b - a) ** 5 / (180 * n_trapecios ** 4)) * dr4
            #print("El valor del error es :" + str(error))
            graficar=True
        except ZeroDivisionError:
            print("La función no se puede evaluar en cero")

    else:
        print('No se puede aplicar el metodo de simpson')
        grafica=False

    if graficar==True:
        fig, ax = plt.subplots()
        ax.plot(x, y)
        for i in range(n_trapecios):
            xs = [x[i], x[i + 1], x[i + 1], x[i]]
            ys = [0, 0, f(x[i + 1]), f(x[i])]
            ax.plot(xs, ys, 'b', lw=1)
        xm = (x[:-1] + x[1:]) / 2
        ym = f(xm)
        for i in range(n_trapecios):
            ax.plot([xm[i], xm[i]], [0, ym[i]], 'r--', lw=1)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Método de Simpson')

    return[plt.gcf(),np.abs(T),error]