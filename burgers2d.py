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
nt = int(runtime/dt)

u = np.ones((ny, nx)) 
v = np.ones((ny, nx))
un = np.ones((ny, nx)) 
vn = np.ones((ny, nx))
comb = np.ones((ny, nx))


# Condiciones iniciales, hat function, todo 1 excepto 0.5<x,y<1, que vale 2
u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2 
v[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2

for n in range(nt+1):
    un = u.copy()
    vn = v.copy()

    u[1:-1,1:-1] = un[1:-1,1:-1] - dt/dx * un[1:-1,1:-1] * (un[1:-1,1:-1] - un[0:-2,1:-1]) 
    - dt/dy * vn[1:-1,1:-1] * (un[1:-1,1:-1] - un[1:-1,0:-2])
    + nu * dt/(dx**2)*(un[2:,1:-1] - 2*un[1:-1,1:-1] + un[0:-2,1:-1])
    + nu * dt/(dy**2)*(un[1:-1,2:] - 2*un[1:-1,1:-1] + un[1:-1,0:-2])

    v[1:-1,1:-1] = vn[1:-1,1:-1] - dt/dx * un[1:-1,1:-1] * (vn[1:-1,1:-1] - vn[0:-2,1:-1]) 
    - dt/dy * vn[1:-1,1:-1] * (vn[1:-1,1:-1] - vn[1:-1,0:-2])
    + nu * dt/(dx**2)*(vn[2:,1:-1] - 2*vn[1:-1,1:-1] + vn[0:-2,1:-1])
    + nu * dt/(dy**2)*(vn[1:-1,2:] - 2*vn[1:-1,1:-1] + vn[1:-1,0:-2])

    # Condiciones de contorno
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1
    
    v[0, :] = 1
    v[-1, :] = 1
    v[:, 0] = 1
    v[:, -1] = 1


x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=1, cstride=1)
ax.plot_surface(X, Y, v, cmap=cm.viridis, rstride=1, cstride=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig.show()