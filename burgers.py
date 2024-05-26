### Resolucion de la ecuacion de Burgers en 1D con condiciones de contorno periodicas

import numpy as np
import sympy as sp 

from sympy import init_printing # Prettyprint para las expresiones simbolicas
init_printing(use_latex=True)

from sympy.utilities.lambdify import lambdify # Permite llamar a las funciones simbolicas

x, nu, t = sp.symbols('x nu t')
phi=(sp.exp(-(x-4*t)**2/(4*nu*(t+1)))+
       sp.exp(-(x-4*t-2*sp.pi)**2/(4*nu*(t+1))))
phiprime = phi.diff(x)

u = -2 * nu * (phiprime / phi) + 4
ufunc = lambdify((t, x, nu), u) # Crea una funcion "u" llamable (numericamente) a partir de la def. simbolica

nx = 101 # Numero de steps en el espacio
nt = 100 # Numero de steps en tiempo
dx = 2 * np.pi / (nx - 1) # Step size
nu = .07 # Termino de difusion
dt = dx * nu # Definir dt como funcion de dx asegura estabilidad de la solucion

x = np.linspace(0, 2*np.pi, nx)
un = np.empty(nx)
t = 0

u = np.asarray([ufunc(t, x0, nu) for x0 in x]) # Condiciones iniciales de velocidad, funcion sawtooth

for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] - un[i] * dt / dx *(un[i] - un[i-1]) + nu * dt / dx**2 *\
                (un[i+1] - 2 * un[i] + un[i-1])
        
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx**2 *\
                (un[1] - 2 * un[0] + un[-2])
    u[-1] = u[0]