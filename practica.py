import sympy as sp
import tkinter as tk
from sympy.parsing.sympy_parser import parse_expr
from sympy import poly


x = sp.Symbol('x')
f=x**5+3*x**4-2*x**3+6*x**2-1*x+2
d=complex(2,3)

def horner(F,r):
    a=sp.poly(F,x)
    h=a.all_coeffs()
    j=a.degree()
    L=[]
    c2=0
    for i in range(j+1):
        c1=h[i]+c2*r
        L.append(c1)
        c2=c1
    return L

def poli(L):
    P=0
    L=L[::-1]
    for i in range(1,len(L)):
        P=P+L[i]*x**(i-1)
    return P

def eval(j,h):
    return j.subs(x,h)

def newti (f,p):
    for i in range(40):
        v1=horner(f,p)
        v2=poli(v1)
        v3=horner(v2,p)
        x=p-(v1[-1])/v3[-1]
        p=x.evalf()
    return (v2,p)

G=sp.Poly(f).degree()
a=newti(f,d)
L=[]
L.append(a[1])

for i in range(G-1):
    a=newti(a[0],a[1])
    L.append(a[1])
n=[]
for i in L:
    if type(i)==sp.Float:
        n.append(i)
        continue
    bb=complex(0,0.00000000000000001).imag
    cc=complex(i).imag
    if abs(cc)<abs(bb):
        n.append(complex(i).real)
    else:
        n.append(complex(i))

print("las raices son:")
print(n)