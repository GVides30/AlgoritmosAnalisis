import math
import cmath
from matplotlib import pyplot as plt
import numpy as np
import sys
import sympy as sp

def cuadratica(r,s): #hallar 2 raices en grados mayores a 2
    discrim = math.pow(r,2)+(4*s)
    raices = []
    if discrim > 0: #raiz real
        raices.append((r+math.sqrt(discrim))/(2))
        raices.append((r-math.sqrt(discrim))/(2))
    else: #raiz compleja
        raices.append((r-cmath.sqrt(discrim))/2)
        raices.append((r+cmath.sqrt(discrim))/2)
    return raices

def cuadratica2(a,b,c): #hallar últimas 2 raices
    discrim = math.pow(b,2)-(4*a*c)
    raices = []
    if discrim > 0: #raiz real
        raices.append((-b+math.sqrt(discrim))/(2*a))
        raices.append((-b-math.sqrt(discrim))/(2*a))
    else: #raiz compleja
        raices.append((-b-cmath.sqrt(discrim))/(2*a))
        raices.append((-b+cmath.sqrt(discrim))/(2*a))
    return raices

def generateb(a, r, s): #implementacion de relación de concurrencia para hallar residuos de división sintética
    b = []
    b.append(a[0])
    b.append(a[1]+(r*b[-1]))
    for i in a[2:]:
        b.append(i+(r*b[-1])+(s*b[-2]))
    return b

def generatec(b, r, s): #implementacion de relación de concurrencia para hallar derivadas parciales
    c = []
    c.append(b[0])
    c.append(b[1]+(r*c[-1]))
    for i in b[2:-1]:
        c.append(i+(r*c[-1])+(s*c[-2]))
    return c

def bairstow(r,s,a,errorA):
    grado = len(a)-1
    noIter = 1
    listaRaices = []
    b = []
    while grado > 0:
        noIter=0
        rerror = 100
        serror = 100
        if grado == 1:
            print('**********************************************')
            print('Hallando última raíz')
            print('**********************************************')
            if len(b) != 0:
                listaRaices.append(-b[1]/b[0])
            else:
                listaRaices.extend(cuadratica2(a[0],a[1],a[2]))
            grado -= 1
        elif grado == 2:
            print('**********************************************')
            print('Hallando las dos últimas raíces')
            print('**********************************************')
            if len(b) != 0:
                listaRaices.extend(cuadratica2(b[0],b[1],b[2]))
            else:
                listaRaices.extend(cuadratica2(a[0],a[1],a[2]))
            grado -= 2
        else:
            print('**********************************************')
            print('Hallando 2 raices')
            while rerror>errorA or serror>errorA:
                b = generateb(a,r,s) #b4, b3, b2, b1, b0 ...
                c = generatec(b,r,s) #c4, c3, c2, c1
                eq1 = np.array([[c[-2],c[-3]],[c[-1],c[-2]]])
                eq2 = np.array([-b[-2],-b[-1]])
                solEq = np.linalg.solve(eq1,eq2) #resolver sistema de ecuaciones usando matrices
                rdelta = solEq[0]
                sdelta = solEq[1]
                r += rdelta
                s += sdelta
                rerror = abs(rdelta/r)*100 #calcula errores relativos de r y s
                serror = abs(sdelta/s)*100
                noIter+=1
                print('-----------------')
                print(f'Iteración número: {noIter}')
                print(f'Raíces encontradas: {listaRaices}')
                print(f'Error de r: {rerror}')
                print(f'Error de s: {serror}')
            print('Error de r:',str(rerror))
            print('Error de s:',str(serror))
            print('No. iter realizadas:',str(noIter))
            print('**********************************************')
            listaRaices.extend(cuadratica(r,s))
            a = b[:-2]
            grado -= 2
    return listaRaices

def main(argv):
    print('----------------------------------------------')
    print('Método de Bairstow')
    print('----------------------------------------------')
    r = float(input('A continuación ingrese un valor para R: '))
    s = float(input('Ingrese un valor para S: '))
    errorA = float(input('Ingrese el número de dígitos de precisión: '))
    grado = int(input('Ingrese el grado del polinomio al cual desea calcularle las raices: '))
    a = []
    print('A continuación por favor ingrese los coeficientes de los términos del polinomio de mayor a menor grado:')
    coef = range(0,grado+1)
    coef = list(coef)[::-1]
    for i in coef:
        a.append(float(input('Coeficiente x'+str(i)+': ')))
    polinomio=0
    
    x = sp.Symbol('x')
    coef_sympy = [sp.Float(c) for c in a[::-1]]
    poli = 0
    for i, c in enumerate(coef_sympy):
        poli += c * x**i
    
    print("\n\n----------------------------------------------")
    print('---------------Calculando---------------------')
    print("----------------------------------------------\n")
    cont = 1
    raices = bairstow(r,s,a,math.pow(10,-errorA))
    print("\n")
    print("\n----------------------------------------------")
    print('---------------Resultados---------------------')
    print("----------------------------------------------\n")
    for i in raices:
        print('Raíz no.'+str(cont)+' : '+str(i))
        cont += 1
    print("Polinomio factorizado:")
    pol = ""
    for i in raices:
        if 'j' in str(i): #raíz compleja
            pol+="(x+"+str(-i)+")"
        else:
            pol+="(x+("+str(-i)+"))"
            
            
    print(pol)
    print(polinomio)
    
    f = sp.lambdify(x, poli, 'numpy')


    raices = np.roots(a)
    
    xpts = np.linspace(-10,10)
    ypts = f(xpts)
    raices_reales = [r for r in raices if abs(r.imag) < 1e-9]
    for r in raices_reales:
        plt.plot(r.real, 0, 'ro')
    plt.plot(xpts, ypts)
    plt.title("Polinomio")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-10,10])
    plt.show()

        
if __name__ == "__main__":
    main(sys.argv)