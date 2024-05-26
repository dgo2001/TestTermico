import numpy as np
import sympy as sp 

from sympy import init_printing
init_printing(use_latex=True)

x, nu, t = sympy.symbols('x nu t')
phi=(sympy.exp(-(x-4*t)**2/(4*nu*(t+1)))+
       sympy.exp(-(x-4*t-2*sympy.pi)**2/(4*nu*(t+1))))
phi

