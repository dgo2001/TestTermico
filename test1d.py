import numpy
from matplotlib import pyplot

length = 10               # length of rod
k = .466                  # heat constant of steel
temp_at_left_end = 200    # temperature at left side of rod
temp_at_right_end = 200   # temperature at right side of rodtotal_time = 10           # time sim will run for

total_time = 4

dx = .1    # space in between points, the smaller the better# defines the x domain as being from 0 to length and                  # having int(length/dx) points separated by a value dx, will 
# return an array containing all of the points
x_vec = numpy.linspace(0, length, int(length/dx))    

dt = .0001    # space in between steps in time# defines the time domain as being from 0 to total_time and                  # having int(total_time/dt) points, separated by steps of 
# value dt, returns an array containing all time steps
t_vec = numpy.linspace(0, total_time, int(total_time/dt))# defines an empty 2D numpy array to store the values of u(t, x) as   # we solve for them
u = numpy.zeros([len(t_vec), len(x_vec)])

u[:, 0] = temp_at_left_end     # u(t, 0) = 200
u[:, -1] = temp_at_right_end   # u(t, length) = 200

for t in range(1, len(t_vec)-1):
    for x in range(1, len(x_vec)-1):
        u[t+1, x] = k * (dt / dx**2) * (u[t, x+1] - 2*u[t, x] + 
                    u[t, x-1]) + u[t, x]# Notice how this equation substitutes the dx and dt that appear
# within the functions themselves with +1 or -1, this is because
# while the theory states that the points will be spaced out by
# +/- dx or +/- dt, in practice an array can only ever be spaced
# out by +1 or -1, so we make due.

    pyplot.plot(x_vec, u[t], 'black')
    pyplot.pause(.001)
    pyplot.cla()


pyplot.plot(x_vec, u[0])
pyplot.ylabel("Temperature (C˚)")
pyplot.xlabel("Distance Along Rod (m)")
pyplot.show()