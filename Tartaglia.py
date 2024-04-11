import cmath
import math
import sympy 
import sympy as sp
import numpy as np

def raices_tartaglia_cardano(polinomio):
    # Verifica que el polinomio sea de grado 3 o menos
    if polinomio.degree() > 3:
        raise ValueError("El polinomio debe ser de grado 3 o menos")

    # Obtener los coeficientes del polinomio
    a, b, c, d = polinomio.coeffs()

    # Calcula las constantes de Tartaglia-Cardano
    p = -b / (3*a)
    q = (3*a*c - b**2) / (9*a**2)
    r = (9*a*b*c - 27*a**2*d - 2*b**3) / (54*a**3)
    discriminante = q**3 + r**2

    # Calcula las raíces
    if discriminante > 0:
        u = sympy.cbrt(-r + sympy.sqrt(discriminante))
        v = sympy.cbrt(-r - sympy.sqrt(discriminante))
        real1 = u + v - p
        real2 = -(u + v) / 2 - p
        real3 = -(u + v) / 2 - p
        return (real1, ), (real2, ), (real3, )
    elif discriminante == 0:
        u = sympy.cbrt(-r)
        real1 = 2*u - p
        real2 = -u - p
        real3 = -u - p
        return (real1, ), (real2, ), (real3, )
    else:
        theta = sympy.acos(-r / sympy.sqrt(-q**3))
        real1 = 2*sympy.sqrt(-q)*sympy.cos(theta/3) - p
        real2 = 2*sympy.sqrt(-q)*sympy.cos((theta + 2*sympy.pi)/3) - p
        real3 = 2*sympy.sqrt(-q)*sympy.cos((theta + 4*sympy.pi)/3) - p
        imag = sympy.sqrt(3)*sympy.sqrt(-q)*sympy.sin(theta/3)
        return (real1, imag), (real2, -imag), (real3, imag)

def raices_cuadraticas(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    elif discriminante == 0:
        x = -b / (2*a)
        return x,
    else:
        # El polinomio tiene raíces complejas
        real = -b / (2*a)
        imag = math.sqrt(-discriminante) / (2*a)
        return (real, imag), (real, -imag)

def raices_tartaglia(a, b, c, d):
 # Calcula las constantes de Tartaglia-Cardano
    p = -b / (3*a)
    q = (3*a*c - b**2) / (9*a**2)
    r = (9*a*b*c - 27*a**2*d - 2*b**3) / (54*a**3)
    discriminante = q**3 + r**2
    
    # Calcula las raíces
    if discriminante > 0:
        s = math.sqrt(discriminante)
        t1 = -r + s
        t2 = -r - s
        u1 = math.pow(abs(t1), 1/3) * (1 if t1 >= 0 else -1)
        u2 = math.pow(abs(t2), 1/3) * (1 if t2 >= 0 else -1)
        real1 = -1*(u1 + u2 - p)
        imag1 = 0
        real2 = -1*(-0.5*(u1 + u2) - p)
        imag2 = 0.5*math.sqrt(3)*(u1 - u2)
        real3 = -1*(-0.5*(u1 + u2) - p)
        imag3 = -0.5*math.sqrt(3)*(u1 - u2)
        return (real1, imag1), (real2, imag2), (real3, imag3)
    elif discriminante == 0:
        u = -r**(1/3) if r < 0 else r**(1/3)
        real1 = 2*u - p
        imag1 = 0
        real2 = -u - p
        imag2 = 0
        real3 = -u - p
        imag3 = 0
        return (real1, imag1), (real2, imag2), (real3, imag3)
    else:
        s = math.sqrt(-q**3)
        argumento = math.atan2(s, -r)
        modulo = math.pow(q**2 + s**2, 1/6)
        real1 = 2*modulo*math.cos(argumento/3) - p
        imag1 = 0
        real2 = 2*modulo*math.cos((argumento + 2*math.pi)/3) - p
        imag2 = 0
        real3 = 2*modulo*math.cos((argumento + 4*math.pi)/3) - p
        imag3 = 0
        return (real1, imag1), (real2, imag2), (real3, imag3)

def raices_ferrari(a, b, c, d, e):
    # Dividimos por a para obtener la forma simplificada del polinomio
    p = b/a
    q = c/a
    r = d/a
    s = e/a

    # Definimos la variable y
    y = -p/2.0
    w = y**2 - q/3.0

    # Definimos los coeficientes de la ecuación cúbica
    A = (r - y*q + 2*y**3)/3.0
    B = (2*y*2*y - y*r + y*q*2 - s)/2.0

    # Resolvemos la ecuación cúbica
    p = -A**2/3.0 + B
    q = A**3/27.0 - A*B/3.0 + pow(B, 2)/2.0
    t = q + pow(q**2 + p**3, 1/2)
    u = pow(t, 1/3) - pow(-t, 1/3)

    # Calculamos las soluciones para y
    y1 = u - A/3.0
    y2 = -u/2.0 - A/3.0
    y3 = y2
    y4 = y1

    # Calculamos las soluciones para x
    x1 = pow(y1 - y, 1/2) - pow(w, 1/2)
    x2 = -pow(y1 - y, 1/2) - pow(w, 1/2)
    x3 = pow(y2 - y, 1/2) + pow(w, 1/2)
    x4 = -pow(y2 - y, 1/2) + pow(w, 1/2)

    # Ajustamos las soluciones de x para considerar el caso en que w = 0
    if w == 0:
        x3 = -y1 - y2 - y/3.0
        x4 = x3

    # Devolvemos las cuatro soluciones para x
    return [x1 - y/4.0, x2 - y/4.0, x3 - y/4.0, x4 - y/4.0]

grado = int(input('Ingrese el grado del polinomio al cual desea calcularle las raices: '))
poli = []
print('A continuación por favor ingrese los coeficientes de los términos del polinomio de mayor a menor grado:')
coef = range(0,grado+1)
coef = list(coef)[::-1]
for i in coef:
    poli.append(float(input('Coeficiente x'+str(i)+': ')))
    
if len(poli) == 3:
    print("Las raices son:")
    raices = raices_cuadraticas(*poli)
    print(raices)
elif len(poli) == 4:
    print("Las raices son:")
    raices = raices_tartaglia(*poli)
    print(raices)
else:
    print("Las raices son:")
    # Construir el polinomio
    polinomio = np.poly1d(poli)
    # Encontrar las raíces del polinomio
    raices = np.roots(polinomio)
    print(raices)