import tkinter
from tkinter import messagebox

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def minimos(x,y):
    def calculate(self):

        try:
            # Obtener las coordenadas ingresadas por el usuario
            x = []
            y = []

            for entry in self.coordinates_entries:
                data_str = entry.get()
                data_str = data_str.replace(' ', '')  # Eliminar espacios en blanco
                data = [float(val) for val in data_str.split(',')]
                x.append(data[0])
                y.append(data[1])

            x = np.array(x)
            y = np.array(y)

            # Realizar el ajuste lineal utilizando mínimos cuadrados
            a, b = self.minimos_cuadrados(x, y)

            # Mostrar resultados en una nueva ventana
            self.show_results(a, b, x, y)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def minimos_cuadrados(self, x, y):

        x = np.array(x)

    y = np.array(y)

    # Calcular los coeficientes de la línea recta utilizando mínimos cuadrados
    a = (len(x) * np.sum(x * y) - np.sum(x) * np.sum(y)) / (len(x) * np.sum(x ** 2) - (np.sum(x)) ** 2)
    b = (np.sum(y) - a * np.sum(x)) / len(x)

    return a, b

    def show_results(self, a, b, x, y):

        result_window = tkinter.Toplevel(self.root)

        result_window.title("Resultados")

        result_label = tkinter.Label(result_window, text=f"Coeficiente a (pendiente): {a:.4f}", font=("Helvetica", 12))
        result_label.pack()

        result_label = tkinter.Label(result_window, text=f"Coeficiente b (intercepto): {b:.4f}", font=("Helvetica", 12))
        result_label.pack()

        # Crear un gráfico de los datos y la línea ajustada
        plt.figure()
        plt.scatter(x, y, label='Datos')
        plt.plot(x, a * x + b, color='red', label='Ajuste lineal')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Ajuste lineal utilizando Mínimos Cuadrados')
        plt.legend()

    canvas = FigureCanvasTkAgg(plt.gcf(), master=result_window)
    canvas.get_tk_widget().pack()
