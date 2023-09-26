import tkinter
from tkinter import ttk, messagebox
from numpy import character as np
from Simpson import simpson
from Secante import secante
from Punto_Fijo import punto
from Trapezoide import trapecio
from MBiseccion import biseccion
from gauss import gaussMethod
from Simpson import simpson

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MainWindow:
    def __init__(self):

        self.window = tkinter.Tk()
        self.window.title("Proyecto metodos")
        self.window.geometry("550x480")
        self.window.update()
        self.open_windows = []
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = int((screen_width / 2) - (self.window.winfo_width() / 2))
        y = int((screen_height / 2) - (self.window.winfo_height() / 2))

        self.window.geometry("+{}+{}".format(x, y))
        self.window.configure(background="darkgray")
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)
        self.title = tkinter.Label(self.window, text="Metodos Numericos", bg="gold", font="Helvetica 20",
                                   background="#2196F3")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.button1 = tkinter.Button(self.window, text="PUNTO FIJO", font="Helvetica 13", width=10, height=5,
                                      command=self.punto_fijo)
        self.button2 = tkinter.Button(self.window, text="BISECCIÓN", font="Helvetica 13", width=10, height=5,
                                      command=self.biseccion)
        self.button3 = tkinter.Button(self.window, text="SECANTE", font="Helvetica 13", width=10, height=5,
                                      command=self.secante)
        self.button4 = tkinter.Button(self.window, text="TRAPECIO", font="Helvetica 13", width=10, height=5,
                                      command=self.trapecio)
        self.button5 = tkinter.Button(self.window, text="SIMPSON", font="Helvetica 13", width=10, height=5,
                                      command=self.simpson)
        self.button6 = tkinter.Button(self.window, text="GAUSS-SEIDEL", font="Helvetica 13", width=10, height=5,
                                      command=self.gauss)
        self.button7 = tkinter.Button(self.window, text="MINIMOS CUADRADOS", font="Helvetica 13", width=10, height=5,
                                      command=self.minimos)
        self.button8 = tkinter.Button(self.window, text="JACOBI", font="Helvetica 13", width=10, height=5,
                                      command=self.jacobi)
        self.button9 = tkinter.Button(self.window, text="NEWTON RAPHSON", font="Helvetica 13", width=10, height=5,
                                      command=self.newton)
        self.button1.grid(row=1, column=0, padx=5, pady=5, sticky="NSEW")
        self.button2.grid(row=1, column=1, padx=5, pady=5, sticky="NSEW")
        self.button3.grid(row=1, column=2, padx=5, pady=5, sticky="NSEW")
        self.button4.grid(row=2, column=0, padx=5, pady=5, sticky="NSEW")
        self.button5.grid(row=2, column=1, padx=5, pady=5, sticky="NSEW")
        self.button6.grid(row=2, column=2, padx=5, pady=5, sticky="NSEW")
        self.button7.grid(row=3, column=0, padx=5, pady=5, sticky="NSEW")
        self.button8.grid(row=3, column=1, padx=5, pady=5, sticky="NSEW")
        self.button9.grid(row=3, column=2, padx=5, pady=5, sticky="NSEW")

        for btn in (self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8,self.button9):
            btn.configure(height=5, width=10)
        self.window.protocol("WM_DELETE_WINDOW", self.on_cerrar_ventana_principal)

    def on_cerrar_ventana_principal(self):
        self.window.destroy()

    def jacobi(self):
        self.window.withdraw()
        self.windowjacobi = tkinter.Toplevel(self.window)
        self.windowjacobi.title("Jacobi ")
        self.windowjacobi.geometry("490x330")
        self.windowjacobi.configure(background="darkgray")
        # CENTRAR LA VENTANA EN LA PANTALLA
        self.windowjacobi.update()
        screen_width = self.windowjacobi.winfo_screenwidth()
        screen_height = self.windowjacobi.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowjacobi.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowjacobi.winfo_height() / 2))
        self.windowjacobi.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowjacobi, text="Jacobi", bg="lightblue", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.open_windows.append(self.windowjacobi)
        #self.lbl_matrix= tkinter.Label(self.windowjacobi, text="Ingrese tamaño de la matriz")
        #self.lbl_matrix.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.matrix_entries = []
        self.vector_entries = []

        self.etiqueta_tamano = tkinter.Label(self.windowjacobi, text="Ingrese el tamaño de la matriz:")
        self.etiqueta_tamano.grid(row=1, column=0)
        self.caja_tamano = tkinter.Entry(self.windowjacobi, validate="key")
        self.caja_tamano.config(validatecommand=(self.windowjacobi.register(self.validate), "%S"))
        self.caja_tamano.grid(row=1, column=1)

        #self.entry_tamano=tkinter.Entry(self.windowjacobi, font="Helvetica 14")
        #self.entry_tamano.grid(row=2, column=1, padx=3, pady=3)
        self.tamano = self.caja_tamano.get()
        self.botonC=tkinter.Button(self.windowjacobi, text="Crear matriz", font="Helvetica 13", width=10, height=2,
                                      command=self.crearMatrixJ)
        self.botonC.grid(row=4, column=0, columnspan=2, )

        # boton regresar
        back_main = tkinter.Button(self.windowjacobi, text="Regresar", width=10, height=2,
                                   command=lambda: self.back(self.windowjacobi))
        back_main.grid(row=10, column=1)


    def crearMatrixJ(self):
        numFilas = int(self.caja_tamano.get())

        self.matriz = []
        for i in range(numFilas):
            self.fila = []
            for j in range(numFilas):
                self.caja = tkinter.Entry(self.windowjacobi, width=6, validate="key")
                self.caja.config(validatecommand=(self.windowjacobi.register(self.validate), "%S"))
                self.caja.grid(row=i, column=j)
                self.fila.append(self.caja)
            self.matriz.append(self.fila)




    def newton(self):
        self.window.withdraw()
        self.windownewton = tkinter.Toplevel(self.window)
        self.windownewton.title("Newthon raphson")
        self.windownewton.geometry("490x330")
        self.windownewton.configure(background="darkgray")
        # CENTRAR LA VENTANA EN LA PANTALLA
        self.windownewton.update()
        screen_width = self.windownewton.winfo_screenwidth()
        screen_height = self.windownewton.winfo_screenheight()
        x = int((screen_width / 2) - (self.windownewton.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windownewton.winfo_height() / 2))
        self.windownewton.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windownewton, text="Newton Raphson", bg="lightblue", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")

        # MENSAJE INFORMATIVO
        self.text = tkinter.Text(self.windownewton, width=68, height=4, font="Helvetica 10", state="disabled",
                                 bg="lightgreen")
        self.text.config(state="normal")
        texto_ejemplo = "Para el ingreso de funciones tener en cuenta:\n *Raices cuadradas: np.sqrt() o x**(1/2), cubicas np.cbsqrt o  x**(1/3)\n *Funciones trigonométricas antepuestas con np.cos, np.sen \n *El término variable se expresa con x "
        self.text.insert("1.0", texto_ejemplo)
        self.text.config(state="disabled")
        self.text.tag_configure("center", justify="center")
        self.text.tag_add("center", "1.0", "end")
        self.text.grid(row=1, column=0, columnspan=3, padx=3, pady=3)





         # FUNCION SIN DESPEJAR
        self.label_function = tkinter.Label(self.windownewton, text="Función sin despejar f(x):", font="Helvetica 13",
                                            background="darkgray")
        self.label_function.grid(row=2, column=0, padx=3, pady=3)
        self.entry_functionpt = tkinter.Entry(self.windownewton, font="Helvetica 14")
        self.entry_functionpt.grid(row=2, column=1, padx=3, pady=3)

        #FUNCION DERIVADA
        self.label_gfunction = tkinter.Label(self.windownewton, text="Función derivada g(x):", font="Helvetica 13",
                                             background="darkgray")
        self.label_gfunction.grid(row=3, column=0, columnspan=1, padx=3, pady=3)
        self.entry_gfunction = tkinter.Entry(self.windownewton, font="Helvetica 14")
        self.entry_gfunction.grid(row=3, column=1, padx=3, pady=3)

        # VALOR INICIAL
        self.label_it = tkinter.Label(self.windownewton, text="Ingrese el valor inicial", font="Helvetica 13",
                                      background="darkgray")
        self.label_it.grid(row=6, column=0, padx=3, pady=3)
        self.entry_it = tkinter.Entry(self.windownewton, font="Helvetica 14")
        self.entry_it.config(validate="key")
        self.entry_it.config(validatecommand=(self.entry_it.register(self.validate), '%S'))
        self.entry_it.grid(row=6, column=1, padx=3, pady=3)

        # PORCENTAJE DE ERROR
        self.label_err = tkinter.Label(self.windownewton, text="Ingrese el valor del error:", font="Helvetica 13",
                                       background="darkgray")
        self.label_err.grid(row=5, column=0, padx=3, pady=3)
        self.entry_errapt = tkinter.Entry(self.windownewton, font="Helvetica 14")
        self.entry_errapt.config(validate="key")
        self.entry_errapt.config(validatecommand=(self.entry_errapt.register(self.validate), '%S'))
        self.entry_errapt.grid(row=5, column=1, padx=3, pady=3)

        # NUMERO MAXIMO DE ITERACIONES
        self.label_it = tkinter.Label(self.windownewton, text="Ingrese el maximo de iteraciones:", font="Helvetica 13",
                                      background="darkgray")
        self.label_it.grid(row=6, column=0, padx=3, pady=3)
        self.entry_it = tkinter.Entry(self.windownewton, font="Helvetica 14")
        self.entry_it.config(validate="key")
        self.entry_it.config(validatecommand=(self.entry_it.register(self.validate), '%S'))
        self.entry_it.grid(row=6, column=1, padx=3, pady=3)



        # boton regresar
        back_main = tkinter.Button(self.windownewton, text="Regresar", width=10, height=2,
                                   command=lambda: self.back(self.windownewton))
        back_main.grid(row=10, column=1)

    def punto_fijo(self):
        self.window.withdraw()
        self.windowpt = tkinter.Toplevel(self.window)
        self.windowpt.title("Punto Fijo")
        self.windowpt.geometry("490x330")
        self.windowpt.configure(background="darkgray")
        # CENTRAR LA VENTANA EN LA PANTALLA
        self.windowpt.update()
        screen_width = self.windowpt.winfo_screenwidth()
        screen_height = self.windowpt.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowpt.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowpt.winfo_height() / 2))
        self.windowpt.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowpt, text="Metodo Punto Fijo", bg="lightblue", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
        # MENSAJE INFORMATIVO
        self.text = tkinter.Text(self.windowpt, width=68, height=4, font="Helvetica 10", state="disabled",
                                 bg="lightgreen")
        self.text.config(state="normal")
        texto_ejemplo = "Para el ingreso de funciones tener en cuenta:\n *Raices cuadradas: np.sqrt() o x**(1/2), cubicas np.cbsqrt o  x**(1/3)\n *Funciones trigonométricas antepuestas con np.cos, np.sen \n *El término variable se expresa con x "
        self.text.insert("1.0", texto_ejemplo)
        self.text.config(state="disabled")
        self.text.tag_configure("center", justify="center")
        self.text.tag_add("center", "1.0", "end")
        self.text.grid(row=1, column=0, columnspan=3, padx=3, pady=3)
        # FUNCION SIN DESPEJAR
        self.label_function = tkinter.Label(self.windowpt, text="Función sin despejar f(x):", font="Helvetica 13",
                                            background="darkgray")
        self.label_function.grid(row=2, column=0, padx=3, pady=3)
        self.entry_functionpt = tkinter.Entry(self.windowpt, font="Helvetica 14")
        self.entry_functionpt.grid(row=2, column=1, padx=3, pady=3)
        # FUNCION DESPEJADA
        self.label_gfunction = tkinter.Label(self.windowpt, text="Función despejada g(x):", font="Helvetica 13",
                                             background="darkgray")
        self.label_gfunction.grid(row=3, column=0, columnspan=1, padx=3, pady=3)
        self.entry_gfunction = tkinter.Entry(self.windowpt, font="Helvetica 14")
        self.entry_gfunction.grid(row=3, column=1, padx=3, pady=3)
        # INGRESO INTERVALO a
        self.label_x0 = tkinter.Label(self.windowpt, text="Valor inicial X0:", font="Helvetica 13",
                                      background="darkgray")
        self.label_x0.grid(row=4, column=0, padx=3, pady=3)
        self.entry_apt = tkinter.Entry(self.windowpt, font="Helvetica 14")
        self.entry_apt.config(validate="key")
        self.entry_apt.config(validatecommand=(self.entry_apt.register(self.validate), '%S'))
        self.entry_apt.grid(row=4, column=1, padx=3, pady=3)
        # PORCENTAJE DE ERROR
        self.label_err = tkinter.Label(self.windowpt, text="Ingrese el valor del error:", font="Helvetica 13",
                                       background="darkgray")
        self.label_err.grid(row=5, column=0, padx=3, pady=3)
        self.entry_errapt = tkinter.Entry(self.windowpt, font="Helvetica 14")
        self.entry_errapt.config(validate="key")
        self.entry_errapt.config(validatecommand=(self.entry_errapt.register(self.validate), '%S'))
        self.entry_errapt.grid(row=5, column=1, padx=3, pady=3)
        # NUMERO MAXIMO DE ITERACIONES
        self.label_it = tkinter.Label(self.windowpt, text="Ingrese el maximo de iteraciones:", font="Helvetica 13",
                                      background="darkgray")
        self.label_it.grid(row=6, column=0, padx=3, pady=3)
        self.entry_it = tkinter.Entry(self.windowpt, font="Helvetica 14")
        self.entry_it.config(validate="key")
        self.entry_it.config(validatecommand=(self.entry_it.register(self.validate), '%S'))
        self.entry_it.grid(row=6, column=1, padx=3, pady=3)
        # REGRESAR AL INICIO
        back_main = tkinter.Button(self.windowpt, text="Regresar", width=10, height=2,
                                   command=lambda: self.back(self.windowpt))
        back_main.grid(row=8, column=0, padx=10, pady=10)
        # CALCULAR
        calculate = tkinter.Button(self.windowpt, text="Calcular", width=10, height=2, command=self.startPuntoFijo)
        calculate.grid(row=8, column=1, padx=10, pady=10)
        self.open_windows.append(self.windowpt)

    def startPuntoFijo(self):
        if '/x' in self.entry_functionpt.get() and self.entry_apt.get() == '0' and '/x' in self.entry_gfunction.get():
            self.windowsalert = tkinter.Toplevel(self.windowpt)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="No se puede dividir entre cero",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif self.entry_functionpt.get() == '' or self.entry_gfunction.get() == '' or self.entry_apt.get() == '' or self.entry_errapt.get() == '' or self.entry_it.get() == '':
            self.windowsalert = tkinter.Toplevel(self.windowpt)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="Por favor ingrese todos los datos",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        else:
            self.windowpt.withdraw()
            self.windowrespt = tkinter.Toplevel(self.windowpt)
            self.windowrespt.title("Resultados Punto Fijo")
            self.windowrespt.geometry("408x475")
            self.windowrespt.configure(background="darkgray")
            self.windowrespt.update()
            screen_width = self.windowrespt.winfo_screenwidth()
            screen_height = self.windowrespt.winfo_screenheight()
            x = int((screen_width / 2) - (self.windowrespt.winfo_width() / 2))
            y = int((screen_height / 2) - (self.windowrespt.winfo_height() / 2))
            self.windowrespt.geometry("+{}+{}".format(x, y))
            self.title = tkinter.Label(self.windowrespt, text="Resultados Punto Fijo", bg="gold", font="Helvetica 20")
            self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
            self.label_respt = tkinter.Label(self.windowrespt, text="La raíz se encuentra en:", font="Helvetica 13",
                                             background="darkgray")
            self.label_respt.grid(row=1, column=0, padx=3, pady=3)
            resultpt = punto(self.entry_functionpt.get(), self.entry_gfunction.get(), self.entry_apt.get(),
                             self.entry_errapt.get(), self.entry_it.get())
            self.label_respt = tkinter.Label(self.windowrespt, text=str(resultpt[1]), font="Helvetica 13",
                                             background="darkgray")
            self.label_respt.grid(row=1, column=1, padx=3, pady=3)
            self.label_errpt = tkinter.Label(self.windowrespt, text="El error es :", font="Helvetica 13",
                                             background="darkgray")
            self.label_errpt.grid(row=2, column=0, padx=3, pady=3)
            self.label_errbpt = tkinter.Label(self.windowrespt, text=str(resultpt[2]), font="Helvetica 13",
                                              background="darkgray")
            self.label_errbpt.grid(row=2, column=1, padx=3, pady=3)
            figpt = resultpt[0]
            figpt.set_size_inches(4, 3)
            canvas = FigureCanvasTkAgg(figpt, master=self.windowrespt)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=3, pady=3)
            back_mainpt = tkinter.Button(self.windowrespt, text="Regresar", width=10, height=2,
                                         command=lambda: self.back(self.windowrespt))
            back_mainpt.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
            self.open_windows.append(self.windowrespt)

    def biseccion(self):
        self.window.withdraw()
        self.windowbis = tkinter.Toplevel(self.window)
        self.windowbis.title("Biseccion")
        self.windowbis.geometry("405x265")
        self.windowbis.configure(background="darkgray")
        self.windowbis.update()
        screen_width = self.windowbis.winfo_screenwidth()
        screen_height = self.windowbis.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowbis.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowbis.winfo_height() / 2))
        self.windowbis.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowbis, text="Metodo Biseccion", bg="lightblue", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
        # Espacio de texto recomendaciones
        self.text = tkinter.Text(self.windowbis, width=56, height=4, font="Helvetica 10", state="disabled",
                                 bg="lightgreen")
        self.text.config(state="normal")
        texto_ejemplo = "Para el ingreso de funciones tener en cuenta:\n *Raices cuadradas: np.sqrt() o x**(1/2), cubicas np.cbsqrt o  x**(1/3)\n *Funciones trigonométricas antepuestas con np.cos, np.sen \n *El término variable se expresa con x "
        self.text.insert("1.0", texto_ejemplo)
        self.text.config(state="disabled")
        self.text.tag_configure("center", justify="center")
        self.text.tag_add("center", "1.0", "end")
        self.text.grid(row=1, column=0, columnspan=3, padx=3, pady=3)
        # FUNCION FX
        self.label_function = tkinter.Label(self.windowbis, text="Función  f(x):", font="Helvetica 13",
                                            background="darkgray")
        self.label_function.grid(row=2, column=0, columnspan=1, padx=3, pady=3)
        self.entry_functionbis = tkinter.Entry(self.windowbis, font="Helvetica 14")
        self.entry_functionbis.grid(row=2, column=1, padx=3, pady=3)
        # INGRESO INTERVALO a
        self.label_x0 = tkinter.Label(self.windowbis, text="Valor a intervalo [a,b]:", font="Helvetica 13",
                                      background="darkgray")
        self.label_x0.grid(row=3, column=0, padx=3, pady=3)
        self.entry_x0bis = tkinter.Entry(self.windowbis, font="Helvetica 14")
        self.entry_x0bis.config(validate="key")
        self.entry_x0bis.config(validatecommand=(self.entry_x0bis.register(self.validate), '%S'))
        self.entry_x0bis.grid(row=3, column=1, padx=3, pady=3)
        # INGRESO INTERVALO b
        self.label_intervalBbis = tkinter.Label(self.windowbis, text="Valor b intervalo [a,b]:", font="Helvetica 13",
                                                background="darkgray")
        self.label_intervalBbis.grid(row=4, column=0, padx=3, pady=3)
        self.entry_intervalBbis = tkinter.Entry(self.windowbis, font="Helvetica 14")
        self.entry_intervalBbis.config(validate="key")
        self.entry_intervalBbis.config(validatecommand=(self.entry_intervalBbis.register(self.validate), '%S'))
        self.entry_intervalBbis.grid(row=4, column=1, padx=3, pady=3)
        # REGRESAR
        back_main = tkinter.Button(self.windowbis, text="Regresar", width=10, height=2,
                                   command=lambda: self.back(self.windowbis))
        back_main.grid(row=5, column=0, padx=10, pady=10)
        # CALCULAR
        calculate = tkinter.Button(self.windowbis, text="Calcular", width=10, height=2, command=self.startBiseccion)
        calculate.grid(row=5, column=1, padx=10, pady=10)
        self.open_windows.append(self.windowbis)

    def startBiseccion(self):
        if '/x' in self.entry_functionbis.get() and float(self.entry_x0bis.get()) <= 0 and float(
                self.entry_intervalBbis.get()) >= 0:
            self.windowsalert = tkinter.Toplevel(self.windowbis)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert,
                                            text="La funcion no es continua o\n existe una division entre cero, por favor elija otro intervalo para evaluar la funcion",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif self.entry_functionbis.get() == '' or self.entry_x0bis.get() == '' or self.entry_intervalBbis.get() == '':
            self.windowsalert = tkinter.Toplevel(self.windowbis)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="Por favor ingrese todos los datos",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif '/x' in self.entry_functionbis.get() and float(self.entry_intervalBbis.get()) == 0:
            self.windowsalert = tkinter.Toplevel(self.windowbis)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert,
                                            text="La funcion no es continua o\n existe una division entre cero",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif float(self.entry_x0bis.get()) > float(self.entry_intervalBbis.get()):
            self.windowsalert = tkinter.Toplevel(self.windowbis)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="El intervalo [a,b] es incorrecto",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif float(self.entry_x0bis.get()) == float(self.entry_intervalBbis.get()):
            self.windowsalert = tkinter.Toplevel(self.windowbis)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="El intervalo [a,b] es incorrecto",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        else:
            self.windowbis.withdraw()
            self.windowresbis = tkinter.Toplevel(self.windowbis)
            self.windowresbis.title("Resultados Biseccion")
            self.windowresbis.geometry("408x480")
            self.windowresbis.configure(background="darkgray")
            self.windowresbis.update()
            screen_width = self.windowresbis.winfo_screenwidth()
            screen_height = self.windowresbis.winfo_screenheight()
            x = int((screen_width / 2) - (self.windowresbis.winfo_width() / 2))
            y = int((screen_height / 2) - (self.windowresbis.winfo_height() / 2))
            self.windowresbis.geometry("+{}+{}".format(x, y))
            self.title = tkinter.Label(self.windowresbis, text="Resultados Biseccion", bg="lightblue",
                                       font="Helvetica 20")
            self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
            self.label_res = tkinter.Label(self.windowresbis, text="La raíz se encuentra en:", font="Helvetica 13",
                                           background="darkgray")
            self.label_res.grid(row=1, column=0, padx=3, pady=3)
            result = biseccion(self.entry_functionbis.get(), self.entry_x0bis.get(), self.entry_intervalBbis.get())
            self.label_resb = tkinter.Label(self.windowresbis, text=str(result[3]), font="Helvetica 13",
                                            background="darkgray")
            self.label_resb.grid(row=1, column=1, padx=3, pady=3)
            self.label_err = tkinter.Label(self.windowresbis, text="El error es :", font="Helvetica 13",
                                           background="darkgray")
            self.label_err.grid(row=2, column=0, padx=3, pady=3)
            self.label_errb = tkinter.Label(self.windowresbis, text=str(result[2]), font="Helvetica 13",
                                            background="darkgray")
            self.label_errb.grid(row=2, column=1, padx=3, pady=3)
            fig = result[0]
            fig.set_size_inches(4, 3)
            canvas = FigureCanvasTkAgg(fig, master=self.windowresbis)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=3, pady=3)
            back_main = tkinter.Button(self.windowresbis, text="Regresar", width=10, height=2,
                                       command=lambda: self.back(self.windowresbis))
            back_main.grid(row=5, column=0, padx=10, pady=10)
            show_table = tkinter.Button(self.windowresbis, text="Mostrar tabla", width=10, height=2,
                                        command=self.showtablebis)
            show_table.grid(row=5, column=1, padx=10, pady=10)
            self.open_windows.append(self.windowresbis)

    def showtablebis(self):
        self.windowshowt = tkinter.Toplevel(self.windowresbis)
        self.windowshowt.title("Tabla resultados")
        self.windowshowt.geometry("607x220")
        self.windowshowt.configure(background="darkgray")
        self.windowshowt.update()
        screen_width = self.windowshowt.winfo_screenwidth()
        screen_height = self.windowshowt.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowshowt.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowshowt.winfo_height() / 2))
        self.windowshowt.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowshowt, text="Tabla Resultados", bg="lightblue", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
        table = ttk.Treeview(self.windowshowt, columns=("col1", "col2", "col3", "col4", "col5", "col6"),
                             show="headings")
        table.heading("col1", text="xi", anchor=tkinter.CENTER)
        table.heading("col2", text="xu")
        table.heading("col3", text="xr")
        table.heading("col4", text="fxi")
        table.heading("col5", text="fxr")
        table.heading("col6", text="f")
        table.column("col1", width=100)
        table.column("col2", width=100)
        table.column("col3", width=100)
        table.column("col4", width=100)
        table.column("col5", width=100)
        table.column("col6", width=100)
        tabla = biseccion(self.entry_functionbis.get(), self.entry_x0bis.get(), self.entry_intervalBbis.get())[1]
        files = tabla.tolist()
        for i, fila in enumerate(files):
            table.insert("", "end", text=i, values=(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]))
        table.grid(row=1, column=0, padx=3, pady=3)

    def secante(self):
        self.window.withdraw()
        self.windowsec = tkinter.Toplevel(self.window)
        self.windowsec.title("Secante")
        self.windowsec.geometry("429x305")
        self.windowsec.configure(background="darkgray")
        self.windowsec.update()
        screen_width = self.windowsec.winfo_screenwidth()
        screen_height = self.windowsec.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowsec.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowsec.winfo_height() / 2))
        self.windowsec.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowsec, text="Metodo Secante", bg="lightblue", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
        # Area de texto informativa
        self.text = tkinter.Text(self.windowsec, width=60, height=4, font="Helvetica 10", state="disabled",
                                 bg="lightgreen")
        self.text.config(state="normal")
        texto_ejemplo = "Para el ingreso de funciones tener en cuenta:\n *Raices cuadradas: np.sqrt() o x**(1/2), cubicas np.cbsqrt o  x**(1/3)\n *Funciones trigonométricas antepuestas con np.cos, np.sen \n *El término variable se expresa con x "
        self.text.insert("1.0", texto_ejemplo)
        self.text.config(state="disabled")
        self.text.tag_configure("center", justify="center")
        self.text.tag_add("center", "1.0", "end")
        self.text.grid(row=1, column=0, columnspan=3, padx=3, pady=3)
        # INGRESO FUNCION
        self.label_function = tkinter.Label(self.windowsec, text="Función f(x):", font="Helvetica 13",
                                            background="darkgray")
        self.label_function.grid(row=2, column=0, padx=3, pady=3)
        self.entry_functionsec = tkinter.Entry(self.windowsec, font="Helvetica 14")
        self.entry_functionsec.grid(row=2, column=1, padx=3, pady=3)
        # INGRESOX0
        self.label_x0 = tkinter.Label(self.windowsec, text="Valor X0:", font="Helvetica 13", background="darkgray")
        self.label_x0.grid(row=3, column=0, padx=3, pady=3)
        self.entry_x0sec = tkinter.Entry(self.windowsec, font="Helvetica 14")
        self.entry_x0sec.config(validate="key")
        self.entry_x0sec.config(validatecommand=(self.entry_x0sec.register(self.validate), '%S'))
        self.entry_x0sec.grid(row=3, column=1, padx=3, pady=3)
        # INGRESOX1
        self.label_x1 = tkinter.Label(self.windowsec, text="Valor X1:", font="Helvetica 13", background="darkgray")
        self.label_x1.grid(row=4, column=0, padx=3, pady=3)
        self.entry_x1sec = tkinter.Entry(self.windowsec, font="Helvetica 14")
        self.entry_x1sec.config(validate="key")
        self.entry_x1sec.config(validatecommand=(self.entry_x1sec.register(self.validate), '%S'))
        self.entry_x1sec.grid(row=4, column=1, padx=3, pady=3)
        # PORCENTAJE DE ERROR
        self.label_err = tkinter.Label(self.windowsec, text="Ingrese el valor del error:", font="Helvetica 13",
                                       background="darkgray")
        self.label_err.grid(row=5, column=0, padx=3, pady=3)
        self.entry_errsec = tkinter.Entry(self.windowsec, font="Helvetica 14")
        self.entry_errsec.config(validate="key")
        self.entry_errsec.config(validatecommand=(self.entry_errsec.register(self.validate), '%S'))
        self.entry_errsec.grid(row=5, column=1, padx=3, pady=3)
        # REGRESAR AL INICIO
        back_main = tkinter.Button(self.windowsec, text="Regresar", width=10, height=2,
                                   command=lambda: self.back(self.windowsec))
        back_main.grid(row=6, column=0, padx=10, pady=10)
        # CALCULAR
        calculate = tkinter.Button(self.windowsec, text="Calcular", width=10, height=2, command=self.startSecante)
        calculate.grid(row=6, column=1, padx=10, pady=10)
        self.open_windows.append(self.windowsec)

    def startSecante(self):
        if '/x' in self.entry_functionsec.get() and float(self.entry_x0sec.get()) <= 0 and float(
                self.entry_x1sec.get()) >= 0:
            self.windowsalert = tkinter.Toplevel(self.windowsec)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert,
                                            text="La funcion no es continua o\n existe una division entre cero",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif self.entry_functionsec.get() == '' or self.entry_x1sec.get() == '' or self.entry_errsec.get() == '' or self.entry_x0sec.get() == '':
            self.windowsalert = tkinter.Toplevel(self.windowsec)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="Por favor ingrese todos los datos",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif '/x' in self.entry_functionsec.get() and float(self.entry_x1sec.get()) == 0:
            self.windowsalert = tkinter.Toplevel(self.windowsec)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert,
                                            text="La funcion no es continua o\n existe una division entre cero",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif float(self.entry_x0sec.get()) > float(self.entry_x1sec.get()):
            self.windowsalert = tkinter.Toplevel(self.windowsec)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="X0 debe ser menor que X1", font="Helvetica 13",
                                            background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif float(self.entry_x0sec.get()) == float(self.entry_x1sec.get()):
            self.windowsalert = tkinter.Toplevel(self.windowsec)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="X0 debe ser diferente que X1", font="Helvetica 13",
                                            background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        else:
            self.windowsec.withdraw()
            self.windowressec = tkinter.Toplevel(self.windowsec)
            self.windowressec.title("Resultados Secante")
            self.windowressec.geometry("408x480")
            self.windowressec.configure(background="darkgray")
            self.windowressec.update()
            screen_width = self.windowressec.winfo_screenwidth()
            screen_height = self.windowressec.winfo_screenheight()
            x = int((screen_width / 2) - (self.windowressec.winfo_width() / 2))
            y = int((screen_height / 2) - (self.windowressec.winfo_height() / 2))
            self.windowressec.geometry("+{}+{}".format(x, y))
            self.title = tkinter.Label(self.windowressec, text="Resultados Secante", bg="lightblue",
                                       font="Helvetica 20")
            self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
            self.label_res = tkinter.Label(self.windowressec, text="La raíz se encuentra en:", font="Helvetica 13",
                                           background="darkgray")
            self.label_res.grid(row=1, column=0, padx=3, pady=3)
            resultsec = secante(self.entry_functionsec.get(), self.entry_x0sec.get(), self.entry_x1sec.get(),
                                self.entry_errsec.get())
            self.label_resb = tkinter.Label(self.windowressec, text=str(resultsec[1]), font="Helvetica 13",
                                            background="darkgray")
            self.label_resb.grid(row=1, column=1, padx=3, pady=3)
            self.label_err = tkinter.Label(self.windowressec, text="El error es :", font="Helvetica 13",
                                           background="darkgray")
            self.label_err.grid(row=2, column=0, padx=3, pady=3)
            self.label_errsec = tkinter.Label(self.windowressec, text=str(resultsec[2]), font="Helvetica 13",
                                              background="darkgray")
            self.label_errsec.grid(row=2, column=1, padx=3, pady=3)
            fig = resultsec[0]
            fig.set_size_inches(4, 3)
            canvas = FigureCanvasTkAgg(fig, master=self.windowressec)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=3, pady=3)
            back_mainsec = tkinter.Button(self.windowressec, text="Regresar", width=10, height=2,
                                          command=lambda: self.back(self.windowressec))
            back_mainsec.grid(row=5, column=0, padx=10, pady=10)
            show_table = tkinter.Button(self.windowressec, text="Mostrar tabla", width=10, height=2,
                                        command=self.showtablesec)
            show_table.grid(row=5, column=1, padx=10, pady=10)
            self.open_windows.append(self.windowressec)

    def showtablesec(self):
        self.windowshowtsec = tkinter.Toplevel(self.windowressec)
        self.windowshowtsec.title("Tabla resultados")
        self.windowshowtsec.geometry("310x220")
        self.windowshowtsec.configure(background="darkgray")
        self.windowshowtsec.update()
        screen_width = self.windowshowtsec.winfo_screenwidth()
        screen_height = self.windowshowtsec.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowshowtsec.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowshowtsec.winfo_height() / 2))
        self.windowshowtsec.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowshowtsec, text="Tabla Resultados", bg="lightblue", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
        table = ttk.Treeview(self.windowshowtsec, columns=("col1", "col2", "col3"), show="headings")
        table.heading("col1", text="xi", anchor=tkinter.CENTER)
        table.heading("col2", text="xnuevo")
        table.heading("col3", text="deltax")
        table.column("col1", width=100)
        table.column("col2", width=100)
        table.column("col3", width=100)
        tabla = \
        secante(self.entry_functionsec.get(), self.entry_x0sec.get(), self.entry_x1sec.get(), self.entry_errsec.get())[
            3]
        files = tabla.tolist()
        for i, fila in enumerate(files):
            table.insert("", "end", text=i, values=(fila[0], fila[1], fila[2]))
        table.grid(row=1, column=0, padx=3, pady=3)

    def trapecio(self):
        self.window.withdraw()
        self.windowtrap = tkinter.Toplevel(self.window)
        self.windowtrap.title("Trapecio")
        self.windowtrap.geometry("476x300")
        self.windowtrap.configure(background="darkgray")
        self.windowtrap.update()
        screen_width = self.windowtrap.winfo_screenwidth()
        screen_height = self.windowtrap.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowtrap.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowtrap.winfo_height() / 2))
        self.windowtrap.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowtrap, text="Metodo Trapecio", bg="lightblue", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
        # Area de texto informativa
        self.text = tkinter.Text(self.windowtrap, width=66, height=4, font="Helvetica 10", state="disabled",
                                 bg="lightgreen")
        self.text.config(state="normal")
        texto_ejemplo = "Para el ingreso de funciones tener en cuenta:\n *Raices cuadradas: np.sqrt() o x**(1/2), cubicas np.cbsqrt o  x**(1/3)\n *Funciones trigonométricas antepuestas con np.cos, np.sen \n *El término variable se expresa con x "
        self.text.insert("1.0", texto_ejemplo)
        self.text.config(state="disabled")
        self.text.tag_configure("center", justify="center")
        self.text.tag_add("center", "1.0", "end")
        self.text.grid(row=1, column=0, columnspan=3, padx=3, pady=3)
        # INGRESO FUNCION
        self.label_function = tkinter.Label(self.windowtrap, text="Función f(x):", font="Helvetica 13",
                                            background="darkgray")
        self.label_function.grid(row=2, column=0, padx=3, pady=3)
        self.entry_functiontrap = tkinter.Entry(self.windowtrap, font="Helvetica 14")
        self.entry_functiontrap.grid(row=2, column=1, padx=3, pady=3)
        # INGRESO INTERVALO a
        self.label_x0 = tkinter.Label(self.windowtrap, text="Valor a intervalo [a,b]:", font="Helvetica 13",
                                      background="darkgray")
        self.label_x0.grid(row=3, column=0, padx=3, pady=3)
        self.entry_x0trap = tkinter.Entry(self.windowtrap, font="Helvetica 14")
        self.entry_x0trap.config(validate="key")
        self.entry_x0trap.config(validatecommand=(self.entry_x0trap.register(self.validate), '%S'))
        self.entry_x0trap.grid(row=3, column=1, padx=3, pady=3)
        # INGRESO INTERVALO b
        self.label_intervalB = tkinter.Label(self.windowtrap, text="Valor b intervalo [a,b]:", font="Helvetica 13",
                                             background="darkgray")
        self.label_intervalB.grid(row=4, column=0, padx=3, pady=3)
        self.entry_intervalBtrap = tkinter.Entry(self.windowtrap, font="Helvetica 14")
        self.entry_intervalBtrap.config(validate="key")
        self.entry_intervalBtrap.config(validatecommand=(self.entry_intervalBtrap.register(self.validate), '%S'))
        self.entry_intervalBtrap.grid(row=4, column=1, padx=3, pady=3)
        # NUMERO DE TRAPECIOS
        self.label_ntrap = tkinter.Label(self.windowtrap, text="Ingrese el numero de trapecios:", font="Helvetica 13",
                                         background="darkgray")
        self.label_ntrap.grid(row=5, column=0, padx=3, pady=3)
        self.entry_ntrap = tkinter.Entry(self.windowtrap, font="Helvetica 14")
        self.entry_ntrap.config(validate="key")
        self.entry_ntrap.config(validatecommand=(self.entry_ntrap.register(self.validate), '%S'))
        self.entry_ntrap.grid(row=5, column=1, padx=3, pady=3)
        # REGRESAR AL INICIO
        back_main = tkinter.Button(self.windowtrap, text="Regresar", width=10, height=2,
                                   command=lambda: self.back(self.windowtrap))
        back_main.grid(row=6, column=0, padx=10, pady=10)
        # CALCULAR
        calculate = tkinter.Button(self.windowtrap, text="Calcular", width=10, height=2, command=self.startTrapecio)
        calculate.grid(row=6, column=1, padx=10, pady=10)
        self.open_windows.append(self.windowtrap)

    def startTrapecio(self):
        if '/x' in self.entry_functiontrap.get() and float(self.entry_x0trap.get()) <= 0 and float(
                self.entry_intervalBtrap.get()) >= 0:
            self.windowsalert = tkinter.Toplevel(self.windowtrap)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert,
                                            text="La funcion no es continua o \n existe una division entre cero",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif self.entry_functiontrap.get() == '' or self.entry_x0trap.get() == '' or self.entry_intervalBtrap.get() == '' or self.entry_ntrap.get() == '':
            self.windowsalert = tkinter.Toplevel(self.windowtrap)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="Por favor ingrese todos los datos",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif float(self.entry_x0trap.get()) > float(self.entry_intervalBtrap.get()):
            self.windowsalert = tkinter.Toplevel(self.windowtrap)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="El intervalo a debe ser menor que el intervalo b",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif '/x' in self.entry_functiontrap.get() and float(self.entry_ntrap.get()) <= 0:
            self.windowsalert = tkinter.Toplevel(self.windowtrap)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="El numero de trapecios debe ser \n mayor que 0",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif '/x' in self.entry_functiontrap.get() and float(self.entry_intervalBtrap.get()) == 0:
            self.windowsalert = tkinter.Toplevel(self.windowtrap)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert,
                                            text="La funcion no es continua o \n existe una division entre cero",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif float(self.entry_x0trap.get()) == float(self.entry_intervalBtrap.get()):
            self.windowsalert = tkinter.Toplevel(self.windowtrap)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert,
                                            text="El intervalo a debe ser diferente \n que el intervalo b",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        else:
            self.windowtrap.withdraw()
            self.windowrestrap = tkinter.Toplevel(self.windowtrap)
            self.windowrestrap.title("Resultados Trapecio")
            self.windowrestrap.geometry("408x480")
            self.windowrestrap.configure(background="darkgray")
            self.windowrestrap.update()
            screen_width = self.windowrestrap.winfo_screenwidth()
            screen_height = self.windowrestrap.winfo_screenheight()
            x = int((screen_width / 2) - (self.windowrestrap.winfo_width() / 2))
            y = int((screen_height / 2) - (self.windowrestrap.winfo_height() / 2))
            self.windowrestrap.geometry("+{}+{}".format(x, y))
            self.title = tkinter.Label(self.windowrestrap, text="Resultados Trapecio", bg="lightblue",
                                       font="Helvetica 20")
            self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
            self.label_res = tkinter.Label(self.windowrestrap, text="El area bajo la curva es:", font="Helvetica 13",
                                           background="darkgray")
            self.label_res.grid(row=1, column=0, padx=3, pady=3)
            resultstrap = trapecio(self.entry_functiontrap.get(), self.entry_x0trap.get(),
                                   self.entry_intervalBtrap.get(), self.entry_ntrap.get())
            self.label_resb = tkinter.Label(self.windowrestrap, text=str(resultstrap[2]), font="Helvetica 13",
                                            background="darkgray")
            self.label_resb.grid(row=1, column=1, padx=3, pady=3)
            self.label_err = tkinter.Label(self.windowrestrap, text="El error es :", font="Helvetica 13",
                                           background="darkgray")
            self.label_err.grid(row=2, column=0, padx=3, pady=3)
            self.label_errsec = tkinter.Label(self.windowrestrap, text=str(resultstrap[3]), font="Helvetica 13",
                                              background="darkgray")
            self.label_errsec.grid(row=2, column=1, padx=3, pady=3)
            fig = resultstrap[0]
            fig.set_size_inches(4, 3)
            canvas = FigureCanvasTkAgg(fig, master=self.windowrestrap)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=3, pady=3)
            back_maintrap = tkinter.Button(self.windowrestrap, text="Regresar", width=10, height=2,
                                           command=lambda: self.back(self.windowrestrap))
            back_maintrap.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
            self.open_windows.append(self.windowrestrap)

    def simpson(self):
        self.window.withdraw()
        self.windowsimp = tkinter.Toplevel(self.window)
        self.windowsimp.title("Simpson")
        self.windowsimp.geometry("480x304")
        self.windowsimp.configure(background="darkgray")
        self.windowsimp.update()
        screen_width = self.windowsimp.winfo_screenwidth()
        screen_height = self.windowsimp.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowsimp.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowsimp.winfo_height() / 2))
        self.windowsimp.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowsimp, text="Metodo Simpson", bg="lightblue", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.text = tkinter.Text(self.windowsimp, width=67, height=4, font="Helvetica 10", state="disabled",
                                 bg="lightgreen")
        self.text.config(state="normal")
        texto_ejemplo = "Para el ingreso de funciones tener en cuenta:\n *Raices cuadradas: np.sqrt() o x**(1/2), cubicas np.cbsqrt o  x**(1/3)\n *Funciones trigonométricas antepuestas con np.cos, np.sen \n *El término variable se expresa con x "
        self.text.insert("1.0", texto_ejemplo)
        self.text.config(state="disabled")
        self.text.tag_configure("center", justify="center")
        self.text.tag_add("center", "1.0", "end")
        self.text.grid(row=1, column=0, columnspan=3, padx=3, pady=3)
        # INGRESO FUNCION
        self.label_function = tkinter.Label(self.windowsimp, text="Función f(x):", font="Helvetica 13",
                                            background="darkgray")
        self.label_function.grid(row=2, column=0, padx=3, pady=3)
        self.entry_functionsim = tkinter.Entry(self.windowsimp, font="Helvetica 14")
        self.entry_functionsim.grid(row=2, column=1, padx=3, pady=3)
        # INGRESO INTERVALO a
        self.label_x0 = tkinter.Label(self.windowsimp, text="Valor a intervalo [a,b]:", font="Helvetica 13",
                                      background="darkgray")
        self.label_x0.grid(row=3, column=0, padx=3, pady=3)
        self.entry_x0sim = tkinter.Entry(self.windowsimp, font="Helvetica 14")
        self.entry_x0sim.config(validate="key")
        self.entry_x0sim.config(validatecommand=(self.entry_x0sim.register(self.validate), '%S'))
        self.entry_x0sim.grid(row=3, column=1, padx=3, pady=3)
        # INGRESO INTERVALO b
        self.label_intervalB = tkinter.Label(self.windowsimp, text="Valor b intervalo [a,b]:", font="Helvetica 13",
                                             background="darkgray")
        self.label_intervalB.grid(row=4, column=0, padx=3, pady=3)
        self.entry_intervalBsim = tkinter.Entry(self.windowsimp, font="Helvetica 14")
        self.entry_intervalBsim.config(validate="key")
        self.entry_intervalBsim.config(validatecommand=(self.entry_intervalBsim.register(self.validate), '%S'))
        self.entry_intervalBsim.grid(row=4, column=1, padx=3, pady=3)
        # NUMERO DE TRAPECIOS
        self.label_ntrap = tkinter.Label(self.windowsimp, text="Ingrese el numero de trapecios:", font="Helvetica 13",
                                         background="darkgray")
        self.label_ntrap.grid(row=5, column=0, padx=3, pady=3)
        self.entry_ntrapsim = tkinter.Entry(self.windowsimp, font="Helvetica 14")
        self.entry_ntrapsim.config(validate="key")
        self.entry_ntrapsim.config(validatecommand=(self.entry_ntrapsim.register(self.validate), '%S'))
        self.entry_ntrapsim.grid(row=5, column=1, padx=3, pady=3)
        # REGRESAR AL INICIO
        back_main = tkinter.Button(self.windowsimp, text="Regresar", width=10, height=2,
                                   command=lambda: self.back(self.windowsimp))
        back_main.grid(row=6, column=0, padx=10, pady=10)
        # CALCULAR
        calculate = tkinter.Button(self.windowsimp, text="Calcular", width=10, height=2, command=self.startSimpson)
        calculate.grid(row=6, column=1, padx=10, pady=10)
        self.open_windows.append(self.windowsimp)

    def startSimpson(self):
        if '/x' in self.entry_functionsim.get() and float(self.entry_x0sim.get()) <= 0 and float(
                self.entry_intervalBsim.get()) >= 0:
            self.windowsalert = tkinter.Toplevel(self.windowsimp)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert,
                                            text="La funcion no es continua o \n existe una division entre cero",
                                            font="Helvetica 13", background="darkgray", anchor="center")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif self.entry_functionsim.get() == '' or self.entry_intervalBsim.get() == '' or self.entry_x0sim.get() == '' or self.entry_ntrapsim.get() == '':
            self.windowsalert = tkinter.Toplevel(self.windowsimp)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="Por favor ingrese todos los datos",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif float(self.entry_ntrapsim.get()) % 2 != 0:
            self.windowsalert = tkinter.Toplevel(self.windowsimp)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="El numero de trapecios debe ser par",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif '/x' in self.entry_functionsim.get() and float(self.entry_intervalBsim.get()) == 0:
            self.windowsalert = tkinter.Toplevel(self.windowsimp)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert,
                                            text="La funcion no es continua o \n existe una division entre cero",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif float(self.entry_x0sim.get()) > float(self.entry_intervalBsim.get()):
            self.windowsalert = tkinter.Toplevel(self.windowsimp)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="El valor de a debe ser menor que b",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif float(self.entry_x0sim.get()) == float(self.entry_intervalBsim.get()):
            self.windowsalert = tkinter.Toplevel(self.windowsimp)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="El valor de a debe ser diferente que b",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        elif float(self.entry_ntrapsim.get()) <= 0:
            self.windowsalert = tkinter.Toplevel(self.windowsimp)
            self.windowsalert.title("Error")
            self.windowsalert.geometry("300x100")
            self.windowsalert.configure(background="darkgray")
            self.labelalert = tkinter.Label(self.windowsalert, text="El numero de trapecios debe ser mayor que 0",
                                            font="Helvetica 13", background="darkgray")
            self.labelalert.grid(row=0, column=0, columnspan=3, sticky="nsew")
        else:
            self.windowsimp.withdraw()
            self.windowressimp = tkinter.Toplevel(self.windowsimp)
            self.windowressimp.title("Resultados Simpson")
            self.windowressimp.geometry("408x480")
            self.windowressimp.configure(background="darkgray")
            self.windowressimp.update()
            screen_width = self.windowressimp.winfo_screenwidth()
            screen_height = self.windowressimp.winfo_screenheight()
            x = int((screen_width / 2) - (self.windowressimp.winfo_width() / 2))
            y = int((screen_height / 2) - (self.windowressimp.winfo_height() / 2))
            self.windowressimp.geometry("+{}+{}".format(x, y))
            self.title = tkinter.Label(self.windowressimp, text="Resultados Simpson", bg="lightgreen",
                                       font="Helvetica 20")
            self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
            resultsimp = simpson(self.entry_functionsim.get(), self.entry_x0sim.get(), self.entry_intervalBsim.get(),
                                 self.entry_ntrapsim.get())
            self.label_res = tkinter.Label(self.windowressimp, text="El area bajo la curva es:", font="Helvetica 13",
                                           background="darkgray")
            self.label_res.grid(row=1, column=0, padx=3, pady=3)
            self.label_resb = tkinter.Label(self.windowressimp, text=str(resultsimp[1]), font="Helvetica 13",
                                            background="darkgray")
            self.label_resb.grid(row=1, column=1, padx=3, pady=3)
            self.label_err = tkinter.Label(self.windowressimp, text="El error es :", font="Helvetica 13",
                                           background="darkgray")
            self.label_err.grid(row=2, column=0, padx=3, pady=3)
            self.label_errsec = tkinter.Label(self.windowressimp, text=str(resultsimp[2]), font="Helvetica 13",
                                              background="darkgray")
            self.label_errsec.grid(row=2, column=1, padx=3, pady=3)
            fig = resultsimp[0]
            fig.set_size_inches(4, 3)
            canvas = FigureCanvasTkAgg(fig, master=self.windowressimp)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=3, pady=3)
            back_maintrap = tkinter.Button(self.windowressimp, text="Regresar", width=10, height=2,
                                           command=lambda: self.back(self.windowressimp))
            back_maintrap.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
            self.open_windows.append(self.windowressimp)

    def minimos(self):
        self.window.withdraw()
        self.windowminimos = tkinter.Toplevel(self.window)
        self.windowminimos.title("Método de Mínimos Cuadrados")
        self.windowminimos.geometry("640x280")
        self.windowminimos.update()
        screen_width = self.windowminimos.winfo_screenwidth()
        screen_height = self.windowminimos.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowminimos.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowminimos.winfo_height() / 2))
        self.windowminimos.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowminimos, text="Metodo Minimos Cuadrados", bg="lightblue",
                                   font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.text = tkinter.Text(self.windowminimos, width=67, height=4, font="Helvetica 10", state="disabled",
                                 bg="lightblue")
        self.text.config(state="normal")

        # Etiqueta para el número de coordenadas
        self.label_num_coordinates = tkinter.Label(self.windowminimos, text="Número de coordenadas:",
                                                   font="Helvetica 13", background="darkgray")
        self.label_num_coordinates.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.entry_num_coordinates = tkinter.Entry(self.windowminimos)
        self.entry_num_coordinates.grid(row=2, column=0, columnspan=3, sticky="nsew")



        # Botón para ingresar las coordenadas
        self.enter_coordinates_button = tkinter.Button(self.windowminimos, text="Ingresar Coordenadas", width=10,
                                                       height=2, command=self.enter_coordinates)
        self.enter_coordinates_button.grid(row=3, column=1, padx=10, pady=10)
        # self.open_windows.append(self.windowsimp)

        self.coordinates_frame = tkinter.Frame(self.windowminimos)

        # Botón de calcular
        self.calculate_button = tkinter.Button(self.windowminimos, text="Calcular", command=self.calculate)
        self.calculate_button.grid(row=4, column=0, columnspan=3, sticky="nsew")
        # self.calculate_button.pack()
        back_maintrap = tkinter.Button(self.windowminimos, text="Regresar", width=10, height=2,
                                       command=lambda: self.back(self.windowminimos))
        back_maintrap.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.open_windows.append(self.windowminimos)


    def gauss(self):
        self.window.withdraw()
        self.windowgauss = tkinter.Toplevel(self.window)
        self.windowgauss.title("Gauss-Seidel")
        self.windowgauss.geometry("640x280")
        self.windowgauss.update()
        screen_width = self.windowgauss.winfo_screenwidth()
        screen_height = self.windowgauss.winfo_screenheight()
        x = int((screen_width / 2) - (self.windowgauss.winfo_width() / 2))
        y = int((screen_height / 2) - (self.windowgauss.winfo_height() / 2))
        self.windowgauss.geometry("+{}+{}".format(x, y))
        self.title = tkinter.Label(self.windowgauss, text="Metodo Gauss-seidel", bg="lightblue", font="Helvetica 20")
        self.title.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.etiqueta_filas = tkinter.Label(self.windowgauss, text=" Numero de Filas:")
        self.etiqueta_filas.grid(row=1, column=0)
        self.caja_filas = tkinter.Entry(self.windowgauss, validate="key")
        self.caja_filas.config(validatecommand=(self.windowgauss.register(self.validate), "%S"))
        self.caja_filas.grid(row=1, column=1)

        self.etiqueta_columnas = tkinter.Label(self.windowgauss, text="Numero de Columnas:")
        self.etiqueta_columnas.grid(row=2, column=0)
        self.caja_columnas = tkinter.Entry(self.windowgauss, validate="key")
        self.caja_columnas.config(validatecommand=(self.windowgauss.register(self.validate), "%S"))
        self.caja_columnas.grid(row=2, column=1)

        self.etiqueta_terminos = tkinter.Label(self.windowgauss, text="Numero de terminos independientes:")
        self.etiqueta_terminos.grid(row=3, column=0)
        self.caja_terminos = tkinter.Entry(self.windowgauss, validate="key")
        self.caja_terminos.config(validatecommand=(self.windowgauss.register(self.validate), "%S"))
        self.caja_terminos.grid(row=3, column=1)

        self.boton_crear = tkinter.Button(self.windowgauss, text="Crear matriz", command=self.crear_matriz)
        self.boton_crear.grid(row=5, columnspan=2)
        self.boton_crear = tkinter.Button(self.windowgauss, text="Crear vector de terminos Independientes",
                                          command=self.crear_vectorI)
        self.boton_crear.grid(row=6, columnspan=2)

        back_main = tkinter.Button(self.windowgauss, text="Regresar", width=10, height=2,
                                   command=lambda: self.back(self.windowgauss))
        back_main.grid(row=10, column=1)
        self.open_windows.append(self.windowgauss)

    def crear_matriz(self):
        frame_matriz = tkinter.Toplevel()
        # Obtener los valores ingresados
        numFilas = int(self.caja_filas.get())
        numColumnas = int(self.caja_columnas.get())

        # Crear la matriz
        self.matriz = []
        for i in range(numFilas):
            self.fila = []
            for j in range(numColumnas):
                self.caja = tkinter.Entry(frame_matriz, width=6, validate="key")
                self.caja.config(validatecommand=(self.windowgauss.register(self.validate), "%S"))
                self.caja.grid(row=i, column=j)
                self.fila.append(self.caja)
            self.matriz.append(self.fila)
        #Agregar el botón de resolver
        boton_resolver = tkinter.Button(frame_matriz, text="Resolver", command=self.resolver_matriz)
        boton_resolver.grid()

    def crear_vectorI(self):

        frame_matriz = tkinter.Toplevel()
        tkinter.Label(frame_matriz, text="---VECTOR DE TERMINOS INDEPENDIENTES---").grid(row=0, column=0)
        tamano = int(self.caja_terminos.get())
        self.b_entries = []

        for i in range(tamano):
            self.entry = tkinter.Entry(frame_matriz, width=6, validate="key")
            self.entry.config(validatecommand=(frame_matriz.register(self.validate), "%S"))
            self.entry.grid(row=i + 1, column=tamano)
            self.nums = int(self.entry[i].get())
            self.b_entries.append(self.nums)

        print(self.b_entries)
        tkinter.Button(frame_matriz, text="Siguiente", command=self.resolver_matriz).grid(row=(tamano + 1),
                                                                                          column=tamano)

    def enter_coordinates(self):
        try:
            num_coordinates = int(self.entry_num_coordinates.get())

            # Crear campos de entrada para las coordenadas
            self.coordinates_entries = []
            for i in range(num_coordinates):
                label = tkinter.Label(self.coordinates_frame, text=f"Coordenada {i + 1}:")
                label.grid(row=i, column=0)

                entry = tkinter.Entry(self.coordinates_frame)
                entry.grid(row=i, column=1)
                self.coordinates_entries.append(entry)

            self.coordinates_frame.pack()

            # Deshabilitar el botón para ingresar coordenadas después de haber ingresado las coordenadas
            self.enter_coordinates_button.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", str(e))

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
    def resolver_matriz(self):
        # Obtener los valores ingresados
        numFilas = int(self.caja_filas.get())
        numColumnas = int(self.caja_columnas.get())
        # matriz=[]
        for i in range(numFilas):
             #fila=[]
            for j in range(numColumnas):
                print(self.matriz[i][j].get())
                self.fila.append(self.matriz[i][j].get())
            self.matriz.append(self.fila)
        # gaussMethod(self.caja_filas, self.caja_columnas,self.matriz)



    def back(self, actual_window):
        actual_window.destroy()
        self.open_windows.pop()

        if self.open_windows:
            previous_window = self.open_windows[-1]
            previous_window.update()
            previous_window.deiconify()
            previous_window.focus_set()
        else:
            self.window.update()
            self.window.deiconify()
            self.window.focus_set()

    def validate(self, character):
        return all(c.isdigit() or c == '.' or (c == '-' and i == 0) for i, c in enumerate(character))


main_window = MainWindow()
main_window.window.mainloop()
