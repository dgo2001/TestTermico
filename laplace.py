import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D

def plot2D(x, y, p):
    fig = pyplot.figure(figsize=(11, 7), dpi=100)
    ax = fig.gca(projection='3d')
    X, Y = numpy.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, p[:], rstride=1, cstride=1, cmap=cm.viridis,
            linewidth=0, antialiased=False)
    ax.view_init(30, 225)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')

def laplace2d(p, y, dx, dy, l1norm_target):
    l1norm = 1

    for it in range(nt):
        #while l1norm > l1norm_target:
            pd = p.copy()
            p[1:-1, 1:-1] = ((dy**2 * (pd[1:-1, 2:] + pd[1:-1, 0:-2]) +
                            dx**2 * (pd[2:, 1:-1] + pd[0:-2, 1:-1]) - b[1:-1, 1:-1] * dx**2 * dy**2) /
                            (2 * (dx**2 + dy**2)))
                
            p[0, :] = 0
            p[ny-1, :] = 0
            p[:, 0] = 0
            p[:, nx-1] = 0
            #l1norm = (numpy.sum(numpy.abs(p[:]) - numpy.abs(pd[:])) / numpy.sum(numpy.abs(pd[:])))
     
    return p

##variable declarations
nx = 31
ny = 31
nt = 300
c = 1

xmin = 0
xmax = 2
ymin = 0
ymax = 1

dx = (xmax - xmin) / (nx - 1)
dy = (ymax - ymin) / (ny - 1)


##initial conditions
p = numpy.zeros((ny, nx))  # create a XxY vector of 0's
pd = numpy.zeros((nx,ny))
b = numpy.zeros((nx,ny))

b[int(ny / 4), int(nx / 4)]  = 100
b[int(3 * ny / 4), int(3 * nx / 4)] = -100

##plotting aids
x  = numpy.linspace(xmin, xmax, nx)
y  = numpy.linspace(xmin, xmax, ny)

##boundary conditions
p[0, :] = 0
p[ny-1, :] = 0
p[:, 0] = 0
p[:, nx-1] = 0

plot2D(x, y, p)

pyplot.show()