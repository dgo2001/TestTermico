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
dx = 2 * numpy.pi / (nx - 1) # Step size
nu = .07 # Termino de difusion
dt = dx * nu # Definir dt como funcion de dx asegura estabilidad de la solucion

x = numpy.linspace(0, 2 * numpy.pi, nx)
un = numpy.empty(nx)
t = 0

u = numpy.asarray([ufunc(t, x0, nu) for x0 in x]) # Condiciones iniciales de velocidad, funcion sawtooth