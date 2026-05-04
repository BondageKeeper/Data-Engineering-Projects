#this is will be a wind which moves diagnolly
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
nx , ny = 100 , 100
dx , dy = 1 , 1
c_x , c_y = 1 , 1 #speed of motion in each direction
dt = 0.2
u = np.zeros((ny,nx))
u[10:30,10:30] = 2
fig , axis = plt.subplots()
img = axis.imshow(u,cmap='magma',origin='lower') #initially origin was upper left [0,0] / now it is upper right [0,0](keep in mind)
def update_motion(frame):
    global u
    un = u.copy()
    u[1:,1:] = (un[1:,1:] - c_x*dt/dx*(un[1:,1:] - un[1:,:-1]) - c_y*dt/dx*(un[1:,1:] - un[:-1,1:]))
    img.set_array(u)
    return [img]
ani = FuncAnimation(fig,update_motion,frames=200,interval=20,blit=True)
plt.show()
