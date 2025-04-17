import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
import sympy as sp
import latexify



L = (10.019+10.610)/2
q =1
d = 4.603
u = (q/L)*np.sqrt(3)/2

def f(x, y):
    a = 4/np.sqrt(3)
    b = a*np.sqrt(x**2+y**2)-(2/3)*(3*x-np.sqrt(3)*y)
    p = 1/np.sqrt((x-d)**2+y**2)
    return u*np.log(((a*np.sqrt((x**2+y**2)+L*(-np.sqrt(3)*x-y+L))+2/3*(-3*x-np.sqrt(3)*y+2*np.sqrt(3)*L)))/(a*np.sqrt(x**2+y**2)-(2/3)*(3*x+np.sqrt(3)*y)))+u*np.log((a*np.sqrt((x**2+y**2)+L*(-np.sqrt(3)*x+y+L))+2/3*(-3*x+np.sqrt(3)*y+2*np.sqrt(3)*L))/b)-q*p
    
x = np.linspace(-2.5, 13, 1500) #-1.5 / 4.2 / 50
y = np.linspace(-7, 7, 1500) #-2.5 / 2.5 / 50
X, Y = np.meshgrid(x, y)
Z = f(X, Y)


#ojo esto esta de extra para probar, el streamplot creo que va bien con linspace, pero el quiver hay que darle aranges que sino....
#x = np.arange(-1.5,4.2,.5)
#y = np.arange(-2.5,2.5,.5) 
  
# Meshgrid 
X,Y = np.meshgrid(x,y)
#se acabo lo extra

def F(x,y):
    return 4/np.sqrt(3)*np.sqrt(x**2+y**2+L*(y-np.sqrt(3)*x+L))+2/3*(np.sqrt(3)*y-3*x+2*np.sqrt(3)*L)

def F_x(x,y):
    return 2/np.sqrt(3)*(2*x-np.sqrt(3)*L)/(np.sqrt(x**2+y**2+L*(y-np.sqrt(3)*x+L)))-2

def F_y(x,y):
    return 2/np.sqrt(3)*(2*y+L)/(np.sqrt(x**2+y**2+L*(y-np.sqrt(3)*x+L)))+2/np.sqrt(3)


def V(x,y):
    return 4/np.sqrt(3)*np.sqrt(x**2+y**2)+2/3*(np.sqrt(3)*y-3*x)

def V_x(x,y):
    return 4/np.sqrt(3)*x/(np.sqrt(x**2+y**2))-2

def V_y(x,y):
    return 4/np.sqrt(3)*y/np.sqrt(x**2+y**2)+2/np.sqrt(3)


Ex = -u*(F_x(X,Y)/F(X,Y) + F_x(X,-Y)/F(X,-Y) -V_x(X,Y)/V(X,Y)-V_x(X,-Y)/V(X,-Y)) -q*(X-d)/(((X-d)**2+Y**2)**(3/2))
Ey = -u*(F_y(X,Y)/F(X,Y) - F_y(X,-Y)/F(X,-Y) -V_y(X,Y)/V(X,Y)+V_y(X,-Y)/V(X,-Y)) -q*Y/(((X-d)**2+Y**2)**(3/2))

normE = np.log(np.sqrt(Ex**2+Ey**2))
normP = np.log(-Z)
normPM = np.log(Z)

fig =plt.figure(figsize=(10.714, 9.286), label= 'Línies de camp') 
ax = fig.add_subplot(111)

ax.contour(X,Y,Z, levels =np.linspace(-3, 3, 30), colors='black',linewidths=0.5, linestyles='solid')
ax.streamplot(X,Y,Ex,Ey, density=2.5, color=np.log(np.hypot(Ex, Ey)),cmap='plasma', linewidth=0.5)
#colorin = ax.contourf(X, Y, normE, cmap="rainbow", levels=60)
#plt.contourf(X, Y, normP, cmap="rainbow", levels=60)
#plt.contourf(X, Y, normPM, cmap="rainbow", levels=60)
ax.set_xticks([])
ax.set_yticks([])

ax.plot([d],[0], 'bo', markersize=14)
pa = np.linspace(0,L*np.sqrt(3)/2-.01, 2000)
ax.plot([pa],[np.sqrt(3)/3*pa],'ro', markersize=3)
ax.plot([pa],[-np.sqrt(3)/3*pa],'ro', markersize=3)

plt.show()
