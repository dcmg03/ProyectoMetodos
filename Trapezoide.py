
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

from scipy.optimize import minimize_scalar

#ENTRADAS

e=np.exp(1)
def trapecio(fun,ai,bi,ntrap):

    f= lambda x: eval(fun)
    a=float(ai)
    b=float(bi)
    n_trapecios=int(ntrap)
    medio=(b+a)/2
    #VALOR DE h
    h=(b-a)/n_trapecios

    #Segunda derivada
    der2=abs((f(a)-2*f(medio)+f(b))/(h)**2)

    #Numero de puntos
    puntos=n_trapecios+1
    area_bajo=0.0
    x=a
    if n_trapecios == 1 :
        area_bajo= h *(f(a) + f(b)) / 2

    elif n_trapecios >1:
        for i in range (0,n_trapecios,1):
            area= h * (f(x) + f(x + h)) / 2
            area_bajo+=area
            x=x+h
    else:
        print("Ingrese un numero válido de trapecios")

    error = ((b - a)**3 / (12 * n_trapecios**2)) * der2


    x=np.linspace(a,b,puntos)
    fi=f(x)
    print("\nCantidad de trapecios: "+str(n_trapecios))
    print("El area bajo la curva corresponde a :"+ str(area_bajo))
    print("Error: "+str(error))
    plt.plot(x,fi,'bo')

    for i in range(0,puntos,1):
        plt.axvline(x[i],color="w")
    plt.fill_between(x,0,fi,color='yellow')
    plt.title('Trapezoide')

    return[plt.gcf(),n_trapecios,area_bajo,error]




