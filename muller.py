import sympy as sym
from tabulate import tabulate
import cmath
from sympy import *
from matplotlib import pyplot as plt
import numpy as np

def muller(f, x0, x1, x2, tol, maxiter):
    

    iteraciones_tabla=[]
    # Convertir la función f a una expresión simbólica de SymPy
    x = sym.Symbol('x')
    f_expr = sym.sympify(f)
    f= lambdify(x, f_expr)
    raices = []
    for i in range(maxiter):
        # Calcular los coeficientes del polinomio cuadrático interpolante
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f_expr.subs(x, x1) - f_expr.subs(x, x0)) / h0
        d1 = (f_expr.subs(x, x2) - f_expr.subs(x, x1)) / h1
        a = (d1 - d0) / (h1 + h0)
        b = a*h1 + d1
        c = f_expr.subs(x, x2)
        
        # Resolver el polinomio cuadrático para encontrar la siguiente aproximación
        disc = b**2 - 4*a*c
        if sym.re(disc) < 0:
            disc = sym.sqrt(-disc) * sym.I
        else:
            disc = sym.sqrt(disc)
        if abs(b - disc) > abs(b + disc):
           den = b - disc
        else:
            den = b + disc
        try:
            dx = -2*c / den
        except TypeError:
            dx = sym.Float(-2*c, chop=True) / den


        # Actualizar las aproximaciones
        x3 = x2 + dx


        ea=(abs((x3-x2)/x3))*100
        iteraciones_tabla.append([i+1,sym.simplify(x0),sym.simplify(x1),sym.simplify(x2),sym.simplify(h0),sym.simplify(h1),sym.simplify(d0),sym.simplify(d1),sym.simplify(a),sym.simplify(b),sym.simplify(c),sym.simplify(x3),sym.simplify(ea)])
        if abs(ea.evalf()) < tol:
            print("{:^150}".format("MÉTODO DE MüLLER"))
            #print(tabulate(iteraciones_tabla, headers=["Iteración", "x0", "x1","x2","h0","h1","δ0","δ1","a","b","c","xr","ea"], tablefmt="presto", numalign="center", stralign="center"))
            print(tabulate(iteraciones_tabla, headers=["Iteración", "x0", "x1","x2","h0","h1","δ0","δ1","a","b","c","xr","ea"], tablefmt="presto", numalign="center", stralign="center"))
            if isinstance(x3, complex):
                pass
            else:
                expr = sym.simplify(x3)
                return expr
           
            return x3
        x0 = x1
        x1 = x2
        x2 = x3
        # Graficar la función
        xpts=np.linspace(-10,10,1000)
        plt.plot(xpts,np.real(f(xpts)))
        plt.title("MÉTODO DE MULLER")
        plt.axhline(color="black")
        plt.axvline(color="black")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True,which='both') 
        plt.ylim([-15,15])
        
    
    


    # Si no se alcanzó la convergencia en el número máximo de iteraciones
    raise ValueError("No se pudo encontrar una raíz con el método de Muller en el intervalo dado.")



x = sym.Symbol('x')
f =input("INGRESE LA FUNCIÓN F(X):")
x0=float(input("INGRESE x0:"))
x1=float(input("INGRESE x1:"))
x2 = float(input("INGRESE x2:"))
tol=float(input("INGRESE LA TOLERANCIA:"))
iteraciones_max=int(input("INGRESE EL MÁXIMO DE ITERACIONES:"))
print("")

# Llamar a la función muller para encontrar una raíz de f en el intervalo (x0, x2)
raiz = muller(f, x0, x1, x2,tol,iteraciones_max)
# Imprimir el resultado
print("")
print('Una raíz de la f(x):',f,'en el intervalo (', x0, ',', x2, ') es:', (raiz))
plt.show()



