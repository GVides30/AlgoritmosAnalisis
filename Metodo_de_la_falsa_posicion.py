import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy import *

def falsa_posicion(funcion, a, b, tolerancia):
    iteraciones = 0
    x = sp.Symbol('x')
    f = sp.sympify(funcion)
    f=sp.lambdify(x,f)
    x1 = a
    x2 = b
    xr = (x1*f(x2) - x2*f(x1)) / (f(x2) - f(x1))
    f_xr_f_x1 = f(xr) * f(x1)
    f_x1 = f(x1)
    f_x2 = f(x2)
    error = 100
    condicion = ""

    while abs(error) > tolerancia and f_xr_f_x1 != 0:
        if f_xr_f_x1 > 0:
            x1 = xr
        else:
            x2 = xr

        xr_ant = xr
        xr = (x1*f(x2) - x2*f(x1)) / (f(x2) - f(x1))
        f_xr_f_x1 = f(xr) * f(x1)
        iteraciones += 1
        error = (xr - xr_ant) / xr * 100
        condicion = "<" if f_xr_f_x1 < 0 else ">"
        
        # Se muestra cada iteración en la consola.
        print(f"Iteración {iteraciones}:")
        print(f"x1: {x1}")
        print(f"x2: {x2}")
        print(f"xr: {xr}")
        print(f"f(x1): {f_x1}")
        print(f"f(x2): {f_x2}")
        print(f"f(xr): {f(xr)}")
        print(f"f(xr)*f(x1): {f_xr_f_x1}")
        print(f"Condición: {condicion}")
        print(f"Error: {error}%")
        print("-----------------------")
    
    print("La raiz es:",xr)
    # Añadimos un punto a la gráfica para marcar la posición de la raíz
    plt.plot(xr, f(xr), 'ro', label='Raíz')

    plt.plot(xr, f(xr), 'ro', label='Raíz')
    #Graficar la función 
    xpts=np.linspace(-10,10)
    plt.plot(xpts,f(xpts))
    plt.title("Método de Bisección")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(xr, 0,c="#FF00FF")
    plt.annotate(round(xr,9), xy=(xr,0.5))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True,which='both') 
    plt.ylim([-15,15])
    plt.show()

    # Mostramos la gráfica
    plt.show()

    return

    
def calcular_raiz():
    # Se obtienen los valores ingresados por el usuario.
    funcion = funcion_entry.get()
    a = float(a_entry.get())
    b = float(b_entry.get())
    tolerancia = float(tolerancia_entry.get())
    
    # Se llama a la función falsa_posicion con los argumentos ingresados.
    falsa_posicion(funcion, a, b, tolerancia)
    
# Se crea la ventana.
ventana = tk.Tk()

# Se crean los widgets para ingresar los argumentos.
tk.Label(ventana, text="Función:").grid(row=0, column=0)
funcion_entry = tk.Entry(ventana)
funcion_entry.grid(row=0, column=1)


tk.Label(ventana, text="a:").grid(row=1, column=0)
a_entry = tk.Entry(ventana)
a_entry.grid(row=1, column=1)

tk.Label(ventana, text="b:").grid(row=2, column=0)
b_entry = tk.Entry(ventana)
b_entry.grid(row=2, column=1)

tk.Label(ventana, text="Tolerancia:").grid(row=3, column=0)
tolerancia_entry = tk.Entry(ventana)
tolerancia_entry.grid(row=3, column=1)

# Se crea el botón para calcular la raíz.
tk.Button(ventana, text="Calcular", command=calcular_raiz).grid(row=4, column=0, columnspan=2)

# Se crean los widgets para mostrar los resultados.
iteraciones_label = tk.Label(ventana)
iteraciones_label.grid(row=5, column=0)

x1_label = tk.Label(ventana)
x1_label.grid(row=6, column=0)

x2_label = tk.Label(ventana)
x2_label.grid(row=7, column=0)

xr_label = tk.Label(ventana)
xr_label.grid(row=8, column=0)

fxr_f1_label = tk.Label(ventana)
fxr_f1_label.grid(row=9, column=0)

condicion_label = tk.Label(ventana)
condicion_label.grid(row=10, column=0)

error_label = tk.Label(ventana)
error_label.grid(row=11, column=0)

# Se inicia el bucle principal de la ventana.
ventana.mainloop()