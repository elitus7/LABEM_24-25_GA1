import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
import sympy as sp
import latexify

q = 1
d= 4.603
nx, ny = 128, 128
L = (10.019+10.610)/2

#cosas de los graficos
x = np.linspace(-2.5, 13, 1500) #-1.5 / 4.2 / 50
y = np.linspace(-7, 7, 1500) #-2.5 / 2.5 / 50
X, Y = np.meshgrid(x, y)



#func potencaial
def V(x,y):
    return -q*(1/np.sqrt((x-d)**2+(y)**2) - 1/np.sqrt((x-d/2)**2+(y-d*np.sqrt(3)/2)**2) +1/np.sqrt((x+d/2)**2+(y-d*np.sqrt(3)/2)**2) -1/np.sqrt((x+d)**2+(y)**2) +1/np.sqrt((x+d/2)**2+(y+d*np.sqrt(3)/2)**2) -1/np.sqrt((x-d/2)**2+(y+d*np.sqrt(3)/2)**2))

Z = V(X, Y)

def E_x(x,y):
    return -(q*((x-d)/(np.sqrt((x-d)**2+(y)**2))**(3/2) - (x-d/2)/(np.sqrt((x-d/2)**2+(y-d*np.sqrt(3)/2)**2))**(3/2) +(x+d/2)/(np.sqrt((x+d/2)**2+(y-d*np.sqrt(3)/2)**2))**(3/2) -(x+d)/(np.sqrt((x+d)**2+(y)**2))**(3/2) +(x+d/2)/(np.sqrt((x+d/2)**2+(y+d*np.sqrt(3)/2)**2))**(3/2) -(x-d/2)/(np.sqrt((x-d/2)**2+(y+d*np.sqrt(3)/2)**2))**(3/2)))

def E_y(x,y):
    return -(q*((y)/(np.sqrt((x-d)**2+(y)**2))**(3/2) - (y-d*np.sqrt(3)/2)/(np.sqrt((x-d/2)**2+(y-d*np.sqrt(3)/2)**2))**(3/2) +(y-d*np.sqrt(3)/2)/(np.sqrt((x+d/2)**2+(y-d*np.sqrt(3)/2)**2))**(3/2) -(y)/(np.sqrt((x+d)**2+(y)**2))**(3/2) +(y+d*np.sqrt(3)/2)/(np.sqrt((x+d/2)**2+(y+d*np.sqrt(3)/2)**2))**(3/2) -(y+d*np.sqrt(3)/2)/(np.sqrt((x-d/2)**2+(y+d*np.sqrt(3)/2)**2))**(3/2)))

E_xx = E_x(X,Y)
E_yy = E_y(X,Y)

#a por el plot
fig =plt.figure(figsize=(10.714, 9.286), label= 'Línies de camp') 
ax = fig.add_subplot(111)

ax.contour(X,Y,Z, levels =np.linspace(-3, 3, 30), colors='black',linewidths=0.5, linestyles='solid')
ax.streamplot(X,Y,E_xx,E_yy, density=2.5, color=np.log(np.hypot(E_xx, E_yy)), cmap='plasma', linewidth=0.5)
#plt.contourf(X, Y, normP, cmap="rainbow", levels=60)
#plt.contourf(X, Y, normPM, cmap="rainbow", levels=60)


#puntos de las cargas
#pa = np.linspace(0,L*np.sqrt(3)/2, 2000)

ax.plot([d],[0], 'bo', markersize=14)
ax.plot([d/2],[d*np.sqrt(3)/2], 'ro', markersize=14)
ax.plot([-d/2],[d*np.sqrt(3)/2], 'bo', markersize=14)
ax.plot([-d/2],[-d*np.sqrt(3)/2], 'bo', markersize=14)
ax.plot([d/2],[-d*np.sqrt(3)/2], 'ro', markersize=14)

#ax.plot([pa],[np.sqrt(3)/3*pa],'ro', markersize=3)
#configs del grafico
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
plt.show()


