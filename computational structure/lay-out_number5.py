import numpy as np
import matplotlib.pyplot as plt
nx , ny = 200 , 200
x = np.linspace(-4,4,nx)
y = np.linspace(-4,4,ny)
X,Y = np.meshgrid(x,y)
u_inf = 1.0
kappa = 5.0 #k
gamma = 4.0 #Г
x_c , y_c = 0.0 , 0.0
X_rel = X - x_c
Y_rel = Y - y_c
R2 = X_rel**2 + Y_rel**2 + 1e-8
u_stream = u_inf
v_stream = 0.0
u_doublet = -(kappa/(2*np.pi)) * (X_rel**2 - Y_rel**2) / (R2**2)
v_doublet = -(kappa/(2*np.pi)) * (2 * X_rel * Y_rel) / (R2**2)
u_vortex = (gamma / (2 * np.pi)) * Y_rel / R2
v_vortex = -(gamma / (2 * np.pi)) * X_rel / R2
U = u_stream + u_doublet + u_vortex
V = v_stream + v_doublet + v_vortex
fig , axis = plt.subplots(figsize=(10,8))
magnitude = np.sqrt(U**2+V**2)
axis.imshow(magnitude,cmap='coolwarm',origin='lower',alpha=0.6)
axis.streamplot(X,Y,U,V,color='black',density=1.8,linewidth=1,arrowsize=1)
R_cylinder = np.sqrt(kappa/(2*np.pi*u_inf))
cylinder = plt.Circle((x_c,y_c),R_cylinder,color='gray',zorder=5)
axis.add_patch(cylinder)
axis.set_xlim([-4, 4])
axis.set_ylim([-4, 4])
axis.set_title(f"Potential Flow: Doublet + Vortex (Gamma = {gamma})")
plt.show()
