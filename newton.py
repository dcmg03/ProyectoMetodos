import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

import matplotlib.pyplot as plt
import numpy as np
#from tabulate import tabulate


print("\nMÉTODO DE NEWTON RAPHSON\n")

# INGRESO
#Funcion Original
def funcionNormal(x):
    fx= x**3+2*x**2+10*x-20
    return fx
#Primera derivada de la función
def primeraDeriv(x):
    dfx = 3*x**2+4*x+10
    return dfx
#Segunda derivada de la función
def segundaDeriv(x):
    ddfx = 6*x+4
    return ddfx

def gPrima(fdx,dfx,ddfx):
    gPrima = abs(1-((dfx*dfx)-(fdx*ddfx))/dfx**2)
    return gPrima

def newton_raphson_method(funcion, derivfun, x0, err, iter):
    plt.plot(xn, yn)
    plt.grid(True)
    plt.axhline(0, color="#ff0000") 
    plt.axvline(0, color="#ff0000")  
    plt.title("Metodo Newton Raphson")
    plt.ylabel("Eje Y")
    plt.xlabel("Eje X")
    plt.plot(xi,0, 'ro')
    a = -2  
    b = 5  
    xn = np.linspace(a, b, n)  
    n = iter
    x = np.linspace(-6,4,100);
    x0 = 1
    yn = funcion
    error = 0.00010
    # PROCEDIMIENTO
    tramo = abs(2*error)
    xi = x0
    tabla=[]
    iteracion=-1
    while (tramo>=error):
        iteracion=iteracion+1
        xnuevo = xi - (funcionNormal(xi)/primeraDeriv(xi))
        tramo  = abs(xnuevo-xi)
        gPrimaValor = gPrima(funcionNormal(xi),primeraDeriv(xi),segundaDeriv(xi))
        xi = xnuevo
        tabla.append([iteracion,xi,tramo,gPrimaValor])
    # SALIDA
    #print(tabulate(tabla, headers=['Iteración','Xi','Xi+1 - Xi','g(x)´']))
    print("\nLa raíz exacta es: ", xi,"\n\n")
    # GRÁFICA




plt.show()