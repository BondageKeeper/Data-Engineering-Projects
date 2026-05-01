import numpy as np
import matplotlib.pyplot as plt
def pressure_calculations():
    nx , ny = 400 , 200
    x = np.linspace(0,10,nx)
    y = np.linspace(0,5,ny)
    X,Y = np.meshgrid(x,y)
    wing_mask = ((X - 3) ** 2 / 4.0 + (Y - 2.5) ** 2 / (0.2 + 0.05 * X)) < 0.5
    p = np.zeros((ny,nx))
    p[:,0] = 200
    p[:,-1] = 0
    for multiplications in range(10000):
        p_mode = p.copy()
        p[1:-1,1:-1] = 0.25 * (p_mode[1:-1,2:] + p_mode[1:-1,:-2] + p_mode[:-2,1:-1] + p_mode[2:,1:-1])
        p[wing_mask] = 0
        #boundary_conditions:
        p[0,:] = p[1,:]
        p[-1,:] = p[-2,:]
    return X,Y,p,wing_mask
X,Y,P,mask_info = pressure_calculations()
plt.figure(figsize=(10,5))
plt.contourf(X,Y,P,999,cmap='jet')
plt.colorbar()
#plt.contourf(X,Y,mask_info,levels=[0.5,1],colors='#2abb8d')
plt.title('Pressure distribution over an airfoil(kPa)',color='#2abb8d')
plt.show()

