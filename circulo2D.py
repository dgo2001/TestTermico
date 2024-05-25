import numpy as np
import matplotlib.pyplot as plt

### Data ###

length = 50 #Side length of simulation enviroment, square by default [mm]
time = 4 #Runtime for the simulation [s]
nodes = 50 #Nodes per side of the enclosure
vel = 1

# Thermal diffusivities [mm^2/s]
a1 = 19  # Diffusivity for medium 1 (Air, placeholder, insert eqn for ideal gas)
a2 = 3.438  # Diffusivity for medium 2 (Inconel 600)

# Nusselt number

#Nu = 2 + 0.6*np.sqrt(Re)*(Pr)^(1/3)
Nu = 2
h = 0.1

# Starting conditions
T0_1 = 20 # Initial temp for medium 1 [ºC]
T0_2 = 50 # Initial temp for medium 2 [ºC]

### Init ###

# Initialize the diffusivity grid
amap = np.full((nodes, nodes), a1)

# Initalize the temperature grid

dx = length / nodes
dy = length / nodes

dt = min(dx**2/(4*a1), dy**2/(4*a1)) # Taking the max alpha value assures the most stable dt
t_nodes = int(time/dt)

u = np.zeros((nodes, nodes)) + T0_1 # Sets medium 1 temp to T0_1

# Define the circular region for the second medium
center_x, center_y = nodes // 2, nodes // 2
radius = 10 #[mm]
r = radius/dx #[nodes]

for i in range(nodes):
    for j in range(nodes):
        if (i - center_y)**2 + (j - center_x)**2 < r**2:
            u[i,j] = 50 # Sets medium 2 temp to T0_2
            amap[i, j] = a2 # Sets medium 2 diffusivity to a2


# Boundary Conditions (WIP)


### Run ###

# Visualizing with a plot

fig, axis = plt.subplots()

pcm = axis.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)

# Simulating

counter = 0

while counter < time :

    w = u.copy()

    for i in range(1, nodes - 1):
        for j in range(1, nodes - 1):

            dd_ux = (w[i-1, j] - 2*w[i, j] + w[i+1, j])/dx**2
            dd_uy = (w[i, j-1] - 2*w[i, j] + w[i, j+1])/dy**2

            u[i, j] = dt * amap[i,j] * (dd_ux + dd_uy) + w[i, j]

    counter += dt

    # Updating the plot

    pcm.set_array(u)
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.01)

plt.show()













