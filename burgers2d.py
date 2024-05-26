import numpy as np
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D

nx = 41
ny = 41
runtime = 4 # Definimos el tiempo de ejecucion en vez de el numero de timesteps [s]
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = .0009
nu = 0.01
dt = sigma * dx * dy / nu
nt = runtime/dt

u = numpy.ones((ny, nx)) 
v = numpy.ones((ny, nx))
un = numpy.ones((ny, nx)) 
vn = numpy.ones((ny, nx))
comb = numpy.ones((ny, nx))


# Condiciones iniciales, hat function, todo 1 excepto 0.5<x,y<1, que vale 2
u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2 
v[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2