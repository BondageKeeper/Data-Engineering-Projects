import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numba import njit , prange
nx , ny = 200 , 200
dx , dy = 1 , 1
dt = 0.000001
cx , cy = 5 , 0.01
viscosity = 2
vel_h = np.zeros((ny,nx))
vel_v = np.zeros((ny,nx))
divergence = np.zeros((ny,nx))
pressure = np.zeros((ny,nx))
wall_mask = np.zeros((ny,nx))
wall_mask[20:100,20:100] = True
figure , axis = plt.subplots(figsize=(10,10))
img = axis.imshow(vel_h,cmap='magma',origin='lower',vmin=0,vmax=25)

@njit(parallel=True)
def turbo_calculation(u,v,div,p,c_x,c_y,d_t,d_x,d_y,coeff):
    u[:,0] = 20
    v[:,0] = 0
    rows , cols = u.shape
    u_new = u.copy()
    v_new = v.copy()
    for i in prange(1,rows-1):
        for j in range(1,cols-1):
            if not wall_mask[i,j]:
                u_new[i,j] = u[i,j] - c_x * (d_t / d_x) * (u[i,j] - u[i,j-1]) - \
                                      c_y * (d_t / d_y) * (u[i,j] - u[i-1,j]) + \
                                      coeff * (d_t / dx**2) * (u[i,j-1] - 2 * u[i,j] + u[i,j+1]) + \
                                      coeff * (d_t / dy**2) * (u[i-1,j] - 2 * u[i,j] + u[i+1,j])
                v_new[i,j] = v[i,j] - c_x * (d_t / d_x) * (v[i,j] - v[i,j-1]) - \
                                      c_y * (d_t / d_y) * (v[i,j] - v[i-1,j]) + \
                                      coeff * (d_t / d_x ** 2) * (v[i,j-1] - 2 * v[i,j] + v[i,j+1]) + \
                                      coeff * (d_t / d_y ** 2) * (v[i-1,j] - 2 * v[i,j] + v[i+1,j])
    for i in prange(1,rows-1):
        for j in range(1,cols-1):
            div[i,j] = (1 / d_t) * ((u_new[i,j+1] - u_new[i,j-1]) / (2 * d_x) + (u_new[i+1,j] - u_new[i-1,j]) / (2 * d_y))
    for i in range(100):
        p_old = p.copy()
        for i in prange(1,rows-1):
            for j in range(1,cols-1):
                p[i,j] = ((p_old[i,j+1] + p_old[i,j-1]) * d_y ** 2 +
                         (p_old[i+1,j] + p_old[i-1,j]) * d_x ** 2 -
                         (div[i,j]*d_x**2*d_y**2)) / (2*(d_x**2 + d_y**2))
        p[:,-1] = 0
        p[0,:] = p[1,:]
        p[:,0] = p[:,1]
        p[-1,:] = p[-2,:]
    for i in prange(rows-1):
        for j in range(cols-1):
            if not wall_mask[i,j]:
                u_new[i,j] -= 0.1 * (d_t / (2 * d_x)) * (p[i,j+1] - p[i,j-1])
                v_new[i,j] -= 0.1 * (d_t / (2 * d_y)) * (p[i+1,j] - p[i-1,j])
            else:
                u_new[i,j] = 0
                v_new[i,j] = 0
    return u_new , v_new

def render_motion(frames):
    global vel_h , vel_v
    vel_h,vel_v = turbo_calculation(vel_h,vel_v,divergence,pressure,cx,cy,dt,dx,dy,viscosity)
    magnitude = np.sqrt(vel_v**2+vel_h**2)
    img.set_array(magnitude)
    return [img]

ani = FuncAnimation(figure,render_motion,frames=200,interval=20,blit=False)
plt.show()

