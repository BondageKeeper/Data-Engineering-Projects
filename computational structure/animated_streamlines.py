import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
nx , ny = 100 , 100
dx , dy = 1.0 , 1.0
dt = 0.00001
viscosity = 0.0005
u_inlet = 40
u = np.full((ny,nx),u_inlet,dtype=float)
v = np.zeros((ny,nx),dtype=float)
p = np.zeros((ny,nx),dtype=float)
div = np.zeros((ny,nx))
x = np.linspace(0,nx-1,nx)
y = np.linspace(0,ny-1,ny)
X,Y = np.meshgrid(x,y)
wall_mask = np.zeros((ny,nx),dtype=bool)
#for i in range(30,60):
#    j = int(0.4 * i + 40)
#    wall_mask[j:j+3,i] = True
wall_mask[45:55,40:50] = True
def solve_cfd():
    global u,v,div,p
    u_photo = u.copy()
    v_photo = v.copy()
    u[1:-1,1:-1] = (u_photo[1:-1,1:-1] - u_photo[1:-1,1:-1] * dt / dx * (u_photo[1:-1,1:-1] - u_photo[1:-1,:-2]) -
                   v_photo[1:-1,1:-1] * dt / dy * (u_photo[1:-1,1:-1] - u_photo[:-2,1:-1]) +
                   viscosity * dt / dx**2 * (u_photo[1:-1,2:] - 2 * u_photo[1:-1,1:-1] + u_photo[1:-1,:-2]) +
                   viscosity * dt / dy**2 * (u_photo[2:,1:-1] - 2 * u_photo[1:-1,1:-1] + u_photo[:-2,1:-1]))
    v[1:-1,1:-1] = (v_photo[1:-1,1:-1] - u_photo[1:-1,1:-1] * dt / dx * (v_photo[1:-1,1:-1] - v_photo[1:-1,:-2]) -
                   v_photo[1:-1,1:-1] * dt / dy * (v_photo[1:-1,1:-1] - v_photo[:-2,1:-1]) +
                   viscosity * dt / dx ** 2 * (v_photo[1:-1, 2:] - 2 * v_photo[1:-1, 1:-1] + v_photo[1:-1, :-2]) +
                   viscosity * dt / dy ** 2 * (v_photo[2:, 1:-1] - 2 * v_photo[1:-1, 1:-1] + v_photo[:-2, 1:-1]))
    u[wall_mask] = 0
    v[wall_mask] = 0
    u[:,0] = u_inlet
    u[:,-1] = u[:,-2]
    v[:,0] = 0
    v[:,-1] = 0

    div[1:-1,1:-1] = ((1.0/dt) * ((u[1:-1,2:] - u[1:-1,:-2]) / (2*dx) + (v[2:,1:-1] - v[:-2,1:-1]) / (2*dy)))
    for _ in range(100):
        p_photo = p.copy()
        p[1:-1,1:-1] = (((p_photo[1:-1,2:] + p_photo[1:-1,:-2])*dy**2) + ((p_photo[2:,1:-1] + p_photo[:-2,1:-1])*dx**2) -
                        (div[1:-1,1:-1]*dx**2*dy**2)) / (2*(dx**2+dy**2))
        p[:,-1] = 0
        p[:,0] = p[:,1]
        p[0,:] = p[1,:]
        p[-1,:] = p[-2,:]
    u[1:-1,1:-1] -= (dt * (p[1:-1,2:] - p[1:-1,:-2])) / (2*dx)
    v[1:-1,1:-1] -= (dt * (p[2:,1:-1] - p[:-2,1:-1])) / (2*dy)

figure , axis = plt.subplots(figsize=(8,7))

def update_picture(frame):
    for _ in range(10):
        solve_cfd()
    axis.clear()
    u_plot = u.copy()
    v_plot = v.copy()
    u_plot[wall_mask] = None
    v_plot[wall_mask] = None
    vel_mag = np.sqrt(u**2+v**2)
    axis.imshow(vel_mag,origin='lower',cmap='magma' ,vmin=0, vmax=u_inlet*1.5)
    axis.streamplot(X,Y,u,v,color='blue',linewidth=0.8,density=0.7)
    axis.contour(wall_mask,levels=[0.5],colors='cyan')
    axis.set_title(f'2D Airfoil Flow - Step {frame}')
ani = FuncAnimation(figure,update_picture,frames=200,interval=20)
plt.show()

