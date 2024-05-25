import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Grid parameters
nx, ny = 50, 50
dx = dy = 1.0

# Time parameters
dt = 0.01
nt = 500

# Thermal diffusivities
alpha1 = 0.1  # diffusivity for air
alpha2 = 0.01  # diffusivity for steel

# Initialize the diffusivity grid
alpha = np.full((ny, nx), alpha1)

# Steel ball parameters
center_x, center_y = nx // 2, ny // 2
radius = 5
velocity_y = 1  # speed of the falling ball


# Initial temperature distribution
u = np.zeros((ny, nx)) + 20

# Function to initialize the diffusivity grid with a circular region for the steel ball
def update_diffusivity(alpha, center_x, center_y, radius, alpha1, alpha2):
    alpha.fill(alpha1)  # set all to air diffusivity
    for i in range(ny):
        for j in range(nx):
            if (i - center_y)**2 + (j - center_x)**2 < radius**2:
                u[i,j] = 100
                alpha[i, j] = alpha2  # set to steel diffusivity

    return alpha

# Initial diffusivity grid
alpha = update_diffusivity(alpha, center_x, center_y, radius, alpha1, alpha2)



# Update function
def update(u, alpha, dx, dy, dt, velocity_y):
    u_new = u.copy()
    for i in range(1, ny-1):
        for j in range(1, nx-1):
            convective_term = velocity_y * (u[i, j] - u[i-1, j]) / dy
            u_new[i, j] = u[i, j] + dt * (
                alpha[i, j] * ((u[i+1, j] - 2*u[i, j] + u[i-1, j]) / dx**2 + (u[i, j+1] - 2*u[i, j] + u[i, j-1]) / dy**2)
                - convective_term
            )
    return u_new

# Simulation loop
for t in range(nt):
    u = update(u, alpha, dx, dy, dt, velocity_y)

# Visualization
fig, ax = plt.subplots()
cax = ax.imshow(u, cmap='jet', interpolation='nearest')
fig.colorbar(cax)

def animate(i):
    global u
    u = update(u, alpha, dx, dy, dt, velocity_y)
    cax.set_array(u)
    return cax,

ani = FuncAnimation(fig, animate, frames=nt, interval=50, blit=True)
plt.show()
