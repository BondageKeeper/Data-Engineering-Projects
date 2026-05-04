import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
nx , ny = 100 , 100
dx , dy = 0.01 , 0.01
c_x , c_y = 0 , 20
nu = 00.1
wall_mask = np.zeros((ny,nx),dtype=bool)
wall_mask[40:60,40:60] = True
dt = 0.0001
nt = 10
u = np.zeros((ny,nx))
u[5:15,45:55] = 50
u[10:25, 42:58] = 50
figure , axis = plt.subplots()
axis.contour(wall_mask,levels=[0.5],colors='white',linewidths=2)
img = axis.imshow(u,cmap='magma',origin='lower')
v = np.zeros((ny,nx)) #vertical speed
p = np.zeros((ny,nx)) #pressure
b = np.zeros((ny,nx)) #divergence(it is a source of the pressure)
def update_motion(frames):
    global u
    u_photo = u.copy()
    v_photo = v.copy()
    u[1:-1,1:-1] = u_photo[1:-1,1:-1] - \
               c_x*dt/dx * (u_photo[1:-1,1:-1] - u_photo[1:-1,:-2]) - \
               c_y*dt/dy * (u_photo[1:-1,1:-1] - u_photo[:-2,1:-1]) + \
               nu*dt/dx**2 * (u_photo[1:-1,2:] - 2*u_photo[1:-1,1:-1] + u_photo[1:-1,:-2]) + \
               nu*dt/dy**2 * (u_photo[2:,1:-1] - 2*u_photo[1:-1,1:-1] + u_photo[:-2,1:-1])
    v[1:-1, 1:-1] = v_photo[1:-1, 1:-1] - \
                    c_x * dt / dx * (v_photo[1:-1, 1:-1] - v_photo[1:-1, :-2]) - \
                    c_y * dt / dy * (v_photo[1:-1, 1:-1] - v_photo[:-2, 1:-1]) + \
                    nu * dt / dx ** 2 * (v_photo[1:-1, 2:] - 2 * v_photo[1:-1, 1:-1] + v_photo[1:-1, :-2]) + \
                    nu * dt / dy ** 2 * (v_photo[2:, 1:-1] - 2 * v_photo[1:-1, 1:-1] + v_photo[:-2, 1:-1])
    #and here we are going to calculate our divergence:
    b[1:-1,1:-1] = (1/dt) * ((u[1:-1,2:] - u[1:-1,:-2]) / (2*dx) + (v[2:,1:-1] - v[:-2,1:-1]) / (2*dy))
    for _ in range(75):
        p_photo = p.copy()
        p[1:-1,1:-1] = ((p_photo[1:-1,2:] + p_photo[1:-1,:-2]) * dy**2 +
                       (p_photo[2:,1:-1] + p_photo[:-2,1:-1]) * dx**2 -
                       (b[1:-1,1:-1] * dx**2 * dy**2)) / (2 * (dx**2 + dy**2))
        p[:,-1] = p[:,-2]
        p[0,:] = p[1,:]
        p[:,0] = p[:1]
        p[-1,:] = 0
    u[1:-1,1:-1] -= dt / (2 * dx) * (p[1:-1,2:] - p[1:-1,:-2])
    v[1:-1,1:-1] -= dt / (2 * dy) * (p[2:,1:-1] - p[:-2,1:-1])
    u[wall_mask] = 0
    v[wall_mask] = 0
    img.set_array(u)
    return [img] #here we return our image in order to update this image
ani = FuncAnimation(figure,update_motion,frames=200,interval=20,blit=False)
plt.show()
