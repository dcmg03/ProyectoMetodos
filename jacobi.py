
import numpy as np

try:
    # Pedir al usuario la matriz
    print("Ingrese la matriz (separando los elementos por espacios y filas por saltos de línea):")
    rows = int(input("Número de filas: "))
    cols = int(input("Número de columnas: "))

    Matriz = np.zeros((rows, cols))

    for i in range(rows):
        row_data = input(f"Ingrese la fila {i + 1} ({cols} elementos separados por espacios): ").split()
        if len(row_data) != cols:
            raise ValueError("La cantidad de elementos en la fila no coincide con el número de columnas.")
        Matriz[i, :] = [float(x) for x in row_data]

    # Pedir al usuario el vector
    print("Ingrese el vector (separando los elementos por espacios):")
    Vector = np.array([float(x) for x in input().split()])

    # Pedir al usuario la tolerancia
    NormaDada = float(input("Ingrese la tolerancia: "))

    T0 = np.array([0] * cols)
    Iteracion = 0
    Norma = 1

    DigonalMatriz = np.diag(np.diag(Matriz))
    NoDiagonal = Matriz - DigonalMatriz
    MatrizIteracion = -np.linalg.inv(DigonalMatriz) @ NoDiagonal
    ValoresMatriz = np.linalg.eigvals(MatrizIteracion)
    RadioEspectral = max(abs(ValoresMatriz))

    if RadioEspectral > 1:
        print('El método no converge para el sistema de ecuaciones lineales dado')
    else:
        while Norma > NormaDada:
            Iteracion = Iteracion + 1
            print('ITERACION ', Iteracion)
            print('  X1      X2        X3        X4          ERROR')
            VectorAuxiliar = np.zeros(cols)
            for i in range(len(VectorAuxiliar)):
                Suma = 0
                for j in range(len(VectorAuxiliar)):
                    if i != j:
                        Suma += Matriz[i, j] * T0[j]
                VectorAuxiliar[i] = (Vector[i] - Suma) / Matriz[i, i]
                print(f'{VectorAuxiliar[i]:10.6f}', end='')
            Norma = np.linalg.norm(T0 - VectorAuxiliar)
            print(f'{Norma:10.6f}')
            print('----------------------')
            print('T', (Iteracion - 1), T0)
            print('----------------------')
            print('---------------------------------------------------------')
            T0 = VectorAuxiliar

except ValueError as error:
    print(f'Error en la entrada de datos: {error}')
except np.linalg.LinAlgError as error:
    print('POR FAVOR ORGANICE LA MATRIZ!!')