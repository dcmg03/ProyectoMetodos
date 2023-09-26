

def coeficientes_indepentiendes(n):
    out = []
    print('-----Ingreso de los coeficientes independientes-----')
    for i in range(0,n):
        out.append(float(input('Ingrese valor [' + str(i) + ']: ')))
    return out


def valores_inicial(n):
    out = []
    print('-----Ingreso de los coeficientes independientes-----')
    for i in range(0,n):
        out.append(float(input('Ingrese valor [' + str(i) + ']: ')))
    return out

def gaussMethod(n, m, matriz, vectorI):
    # [[4,-1,0,0],[-1,4,-1,0],[0,-1,4,-1],[0,0,-1,4]]
    # [1,1,1,1]
    A = matriz [m][n]
    b = coeficientes_indepentiendes(n)
    x0=valores_inicial(n)
    k=0
    norma = 1
    error=0.001
    max_iteraciones=100
    cont = 0
    infinity = float('inf')

    while norma > error:
        k += 1
        x = []
        for i in range(0,3):
            suma = 0
            for j in range(0,3):
                if i != j:
                    suma += A[i][j]*x0[j]
            x.append((b[i]-suma)/(A[i][i]))
            b[i]=x[i]
            if x[i] == float('inf'):
                cont = 1

        norma = abs(x0[0]-x[0])

        print("\nEl vector en la iteracion "+str(k)+" es igual: \n" +str(x))

        x0 = x
        if k > max_iteraciones:
            print('\nNo se alcanzo la convergencia')
            break
