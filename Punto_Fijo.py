import numpy as np
import matplotlib.pyplot as plt

#Funciones
def punto(f,g,a,e,it):
    error=[]
    def puntofijo(gx, a, tolera, iteramax=15):
        i = 1
        b = gx(a)
        tramo = abs(a - b)
        while (tramo >= tolera and i<=iteramax):
            a = b
            b = gx(a)
            tramo = abs(b - a)
            error.append(tramo)
            i = i + 1
        respuesta = b

        #Validar respuesta
        if (i >= iteramax):
            respuesta = np.nan
        return (respuesta)

    #Fin de la función

    #Entadas
    # fx = lambda x: 2*(x**2) - x - 5
    inputf=f
    fx = lambda x: eval(inputf)
    # gx = lambda x: np.sqrt((x+5)/2)
    inputg=g
    gx=lambda x:eval(g)
    a =float(a)
    b = 5
    tolera = float(e)
    iteramax = int(it)
    muestras = 100
    tramos = 50


    #Procedimiento

    respuesta = puntofijo(gx, a, tolera)
    err=error[-1]
    xi = np.linspace(a, b, muestras)
    fi = fx(xi)
    gi = gx(xi)
    yi = xi

    #Salidas

    plt.plot(xi, fi, label='f(x)')
    plt.plot(xi, gi, label='g(x)')
    plt.plot(xi, yi, label='(y=x)')


    if(respuesta != np.nan):
        plt.axvline(respuesta)#Linea vertical donde cruzan la funcion

    plt.axvline(0, color='gray')
    plt.axhline(0, 0, color='gray')
    plt.plot(respuesta, 0, 'ro', label='raiz')
    plt.title('Punto Fijo')
    plt.legend()
    return [plt.gcf(), respuesta,err]
    exit()