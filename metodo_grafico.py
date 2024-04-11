import tkinter
from tkinter import messagebox
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import tkinter as tk
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)


def is_valid_expression(expr):
    """Función para validar la expresión ingresada por el usuario"""
    try:
        x = sp.Symbol('x')
        expr = str(expr)  # convertir la entrada a una cadena de caracteres
        sp.sympify(expr)
        p = sp.Poly(expr, x)
        return True
    except (sp.SympifyError, TypeError):
        return False
    
def grafica(poli):
    # Definir el polinomio
    x = sp.symbols('x')
    p = sp.Poly(poli, x)
   
    # Encontrar las raíces del polinomio
    raices = sp.solve(poli)

    # Crear la gráfica
    f = sp.lambdify(x, poli, 'numpy')

    xpts = np.linspace(-10,10)
    ypts = f(xpts)
    
    plt.plot(xpts, ypts)
    plt.title("Polinomio")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-10,10])
    
    # Verificar si hay raíces complejas
    for raiz in raices:
        if isinstance(raiz, (int, float)):
            plt.scatter(raiz, 0, color="red")
            plt.annotate(round(raiz,9), xy=(raiz,0.5))
        else:
            plt.scatter(raiz.as_real_imag()[0], raiz.as_real_imag()[1], color="red")
    # Mostrar la gráfica
    plt.show()
    print(raices)

def create_window():
    # Crear la ventana
    window = tk.Tk()
    window.title("Ingresar polinomio")

    # Crear un cuadro de entrada de texto
    entry = tk.Entry(window, width=50)
    entry.pack()

    def on_button_click():
        # Obtener la entrada del usuario
        poli = entry.get()

        # Validar la expresión
        if not is_valid_expression(poli):
            messagebox.showerror("Error", "La expresión ingresada no es válida")
            return

        # Llamar a la función para graficar el polinomio
        grafica(poli)

    # Crear un botón para iniciar la gráfica
    button = tk.Button(window, text="Graficar", command=on_button_click)
    button.pack()

    window.mainloop()

create_window()