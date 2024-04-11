import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sin, cos, tan, pi
from sympy import lambdify
from sympy import sympify
from sympy import *
import tkinter as tk
import math

#Inicializar valores
def validate_float(new_value):
    try:
        float(new_value)
        return True
    except ValueError:
        return False

def evaluar_funcion():
    global funcion_ingresada, valor_x1,valor_x2,tolerancia
    try:
        funcion = entrada_funcion.get()
        x1 = entrada_x1.get()
        x2 = entrada_x2.get()
        tol = float(entrada_tol.get())
        funcion_ingresada = funcion
        valor_x1=x1
        valor_x2=x2
        tolerancia=tol
        etiqueta_resultado.config(text=f"Función ingresada: {funcion_ingresada}, x1={x1}, x2={x2}, tol={tol}")
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
etiqueta_x1 = tk.Label(ventana, text="Ingrese el valor de x1:")
entrada_x1 = tk.Entry(ventana,validate='key', validatecommand=(ventana.register(validate_float), '%P'))
etiqueta_x2 = tk.Label(ventana, text="Ingrese el valor de 2:")
entrada_x2 = tk.Entry(ventana,validate='key', validatecommand=(ventana.register(validate_float), '%P'))
etiqueta_tol = tk.Label(ventana, text="Ingrese la tolerancia:")
entrada_tol = tk.Entry(ventana, validate='key', validatecommand=(ventana.register(validate_float), '%P'))
boton_evaluar = tk.Button(ventana, text="Evaluar", command=evaluar_funcion)
etiqueta_resultado = tk.Label(ventana, text="Resultado:")

# Colocar los widgets en la ventana
etiqueta_funcion.grid(row=0, column=0, padx=10, pady=10)
entrada_funcion.grid(row=0, column=1, padx=10, pady=10)
etiqueta_x1.grid(row=1, column=0, padx=10, pady=10)
entrada_x1.grid(row=1, column=1, padx=10, pady=10)
etiqueta_x2.grid(row=2, column=0, padx=10, pady=10)
entrada_x2.grid(row=2, column=1, padx=10, pady=10)
etiqueta_tol.grid(row=3, column=0, padx=10, pady=10)
entrada_tol.grid(row=3, column=1, padx=10, pady=10)
boton_evaluar.grid(row=5, column=0, padx=10, pady=10)

# Iniciar el bucle de eventos de la interfaz
ventana.mainloop()

#Método bisección
x=symbols('x')
fn =sympify(funcion_ingresada)
f= lambdify(x, fn)

#Variables
x1=float(valor_x1)
x2=float(valor_x2)
tol=tolerancia
i=0 #iniciar contador
ea=1 #iniciar variable de error
x_anterior=0 #iniciar la variable de x anterior

#Criterio inicial para verificar si la solución esta en el intervalo
if f(x1)*f(x2)<0:
    #Encabezados
    print("{:^60}".format("MÉTODO DE BISECCIÓN"))
    print("{:^10}{:^10}{:^10}{:^10}{:^10}".format("i","x1","x2","xr","ea%"))

    while ea>tol:
        xr=(x1+x2)/2
        ea=(abs((xr-x_anterior)/xr))*100

        if f(xr)*f(x1)<0:
            x2=xr
        else: 
            x1=xr

        x_anterior=xr
        
        #Valores en tabla
        print("{:^10}{:^10f}{:^10f}{:^10f}{:^10}".format(i,x1,x2,xr,round(ea,9)))
        i=i+1
    
    print("")
    print("El valor de x es",round(xr,9),"con un error de",round(ea,9),"%")

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

else:
    #si no hay raíz o bien se seleccionan 2 raíces en un intervalo
    print("")
    print("La función no tiene una raíz en el intervalo de ","x=",str(x1),"a x=",str(x2))
    print("Ingresar otros valores iniciales")

    #Graficar la función
    xpts=np.linspace(-10, 10)
    plt.plot(xpts,f(xpts))
    plt.title("Método de Bisección")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True,which='both')
    plt.ylim([-15,15])
    plt.show()