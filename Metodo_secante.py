import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
import math
import random
from tabulate import tabulate

def validate_float(new_value):
    try:
        float(new_value)
        return True
    except ValueError:
        return False

def evaluar_funcion():
    global funcion_ingresada, valor_x0,valor_x1,tolerancia, iteraciones_maximas
    try:
        funcion = entrada_funcion.get()
        x0 = float(entrada_x0.get())
        x1 = float(entrada_x1.get())
        tol = float(entrada_tol.get())
        max_iter = int(entrada_max_iter.get())
        funcion_ingresada = funcion
        valor_x0=x0
        valor_x1=x1
        tolerancia=tol
        iteraciones_maximas=max_iter
        etiqueta_resultado.config(text=f"Función ingresada: {funcion_ingresada}, x0={x0}, x1={x1}, tol={tol}, max_iter={max_iter}")
        boton_evaluar.config(state=tk.DISABLED)
        ventana.after(2000, ventana.destroy)
        
    except:
        etiqueta_resultado.config(text="Error: entrada no válida")
    
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ingresar función f(x)")

# Crear los widgets de la interfaz
etiqueta_funcion = tk.Label(ventana, text="Ingrese la función f(x):")
entrada_funcion = tk.Entry(ventana)
etiqueta_x0 = tk.Label(ventana, text="Ingrese el valor de x0:")
entrada_x0 = tk.Entry(ventana, validate='key', validatecommand=(ventana.register(validate_float), '%P'))
etiqueta_x1 = tk.Label(ventana, text="Ingrese el valor de x1:")
entrada_x1 = tk.Entry(ventana, validate='key', validatecommand=(ventana.register(validate_float), '%P'))
etiqueta_tol = tk.Label(ventana, text="Ingrese la tolerancia:")
entrada_tol = tk.Entry(ventana, validate='key', validatecommand=(ventana.register(validate_float), '%P'))
etiqueta_max_iter = tk.Label(ventana, text="Ingrese el número máximo de iteraciones:")
entrada_max_iter = tk.Entry(ventana, validate='key', validatecommand=(ventana.register(validate_float), '%P'))
boton_evaluar = tk.Button(ventana, text="Evaluar", command=evaluar_funcion)
etiqueta_resultado = tk.Label(ventana, text="Resultado:")

# Colocar los widgets en la ventana
etiqueta_funcion.grid(row=0, column=0, padx=10, pady=10)
entrada_funcion.grid(row=0, column=1, padx=10, pady=10)
etiqueta_x0.grid(row=1, column=0, padx=10, pady=10)
entrada_x0.grid(row=1, column=1, padx=10, pady=10)
etiqueta_x1.grid(row=2, column=0, padx=10, pady=10)
entrada_x1.grid(row=2, column=1, padx=10, pady=10)
etiqueta_tol.grid(row=3, column=0, padx=10, pady=10)
entrada_tol.grid(row=3, column=1, padx=10, pady=10)
etiqueta_max_iter.grid(row=4, column=0, padx=10, pady=10)
entrada_max_iter.grid(row=4, column=1, padx=10, pady=10)
boton_evaluar.grid(row=5, column=0, padx=10, pady=10)

# Iniciar el bucle de eventos de la interfaz
ventana.mainloop()

def secant_method():
    iteraciones=[]
    """Método de la secante para encontrar las raíces de una función f(x)"""
    # Pedir los datos al usuario
    f_str = funcion_ingresada
    print(f_str)
    f = lambda x: eval(f_str)
    x0=valor_x0
    x1=valor_x1
    tol=tolerancia
    max_iter=iteraciones_maximas

    # Inicializar variables
    i = 0
    fx0 = f(x0)
    fx1 = f(x1)
    error_porcentual=0

    # Crear la figura y los ejes
    fig, ax = plt.subplots()
    x = np.linspace(x0 - 1, x1 + 1, 1000)
    y = f(x)
    ax.plot(x, y, label='f(x)')

    # Iterar hasta que se alcance la tolerancia o el número máximo de iteraciones
    while i < max_iter:
        # Calcular la siguiente aproximación
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        # Calcular el error porcentual y compararlo con la tolerancia
        if i > 0:
            error_porcentual = abs((x2 - x1) / x2) * 100
            if error_porcentual < tol:
                break

        # Actualizar las variables
        x0 = x1
        x1 = x2
        fx0 = fx1
        fx1 = f(x1)


        
        # Graficar la línea que conecta los puntos (x0, f(x0)) y (x1, f(x1))
        ax.plot([x0, x1], [fx0, fx1], (selec), label=f"Iteración {i}")

        # Imprimir la iteración actual en la lista iteraciones
        iteraciones.append([i, x1, fx1,error_porcentual])

        # Incrementar el contador de iteraciones
        i += 1

    color=['b','r','y','k','m','g']
    num=random.choice(color)
    color_actual=random.choice([c for c in color if c !=num ])
    selec=color_actual+'o-'
    # Imprimir la tabla con los datos de las iteraciones
    print(tabulate(iteraciones, headers=["Iteración", "x", "f(x)","Ea"]))

    # Devolver el resultado
    if i >= max_iter:
        print("Se alcanzó el número máximo de iteraciones sin encontrar una raíz.")
    else:
        print(f"La raíz es: {x1}")

    # Agregar la leyenda y el título de la gráfica
    ax.legend()
    ax.set_title("Método de la secante")

    # Mostrar la gráfica
    plt.show()

secant_method()