import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
plt.title('Trigonometry display')
x_sino = np.arange(-2*np.pi,2*np.pi,0.1)
x_cosino = np.arange(-2*np.pi,2*np.pi,0.1)
y_sino = np.sin(x_sino)
y_cosino = np.cos(x_cosino)
plt.plot(x_sino,y_sino,'r--',linewidth = 3 , label='Sino Function')
plt.plot(x_cosino,y_cosino,'b--',linewidth = 3 , label = 'Cosino Function')
plt.fill_between(x_sino,y_sino,where=(y_sino>0),color='orange')
plt.fill_between(x_cosino,y_cosino,where=(y_cosino<0),color='pink')
plt.xlabel('Axis X (Radian value)')
plt.ylabel('Axis Y (Trigonometry value)')
plt.legend(shadow=True,fancybox=True) #it will show the indication of each function
plt.grid()
plt.show()
