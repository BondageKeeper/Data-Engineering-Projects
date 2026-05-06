#an example with diffusion:
import numpy as np
from numba import njit,prange
@njit(parallel=True)
def diffusion_calculation(visc,d_t,d_x,d_y,vel):
    rows,cols = vel.shape
    next_vel = vel.copy()
    for i in prange(1,rows-1):
        for j in range(1,cols-1):
            diffusion = ((visc * d_t) / (d_x**2) * (vel[i,j+1] - 2*vel[i,j] + vel[i,j-1]) +
                       (visc * d_t) / (d_y**2) * (vel[i+1,j] - 2*vel[i,j] + vel[i-1,j]))
            next_vel[i,j] = vel[i,j] + diffusion
    return next_vel
viscosity = 0.05
dt = 0.0001
dx , dy = 1.0 , 1.0
nx , ny = 100 , 100
v = np.zeros((ny,nx),dtype=float)
v[0:10,0:10] = 50
calculation_result = diffusion_calculation(viscosity,dt,dx,dy,v)
print(calculation_result)
