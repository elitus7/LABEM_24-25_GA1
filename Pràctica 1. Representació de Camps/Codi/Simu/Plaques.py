import numpy as np
import matplotlib.pyplot as plt

nx, ny = 128, 128
x = np.linspace(-6, 6, nx)
y = np.linspace(-5, 5, ny)
X, Y = np.meshgrid(x, y)
d = 3
H = 5  
nq = 200
q = 1  

# Funcions per al camp i potencial
def E(q, r0, x, y):
    rx, ry = x - r0[0], y - r0[1]
    dist3 = (rx**2 + ry**2)**1.5
    return q * rx / dist3, q * ry / dist3

def V(q, r0, x, y):
    return q / np.hypot(x - r0[0], y - r0[1])

# Definir càrregues
charges = [(q, (d/2, -H/2 + H * i / nq)) for i in range(nq)] + \
          [(-q, (-d/2, -H/2 + H * i / nq)) for i in range(nq)]

# Càlcul del camp elèctric i potencial
Ex, Ey, Vt = np.zeros((ny, nx)), np.zeros((ny, nx)), np.zeros((ny, nx))
for q, pos in charges:
    ex, ey = E(q, pos, X, Y)
    Ex += ex
    Ey += ey
    Vt += V(q, pos, X, Y)

fig, ax = plt.subplots(figsize=(6, 6))
ax.streamplot(x, y, Ex, Ey, color=np.log(np.hypot(Ex, Ey)), cmap='plasma', density=2, linewidth=0.5)
ax.contour(X, Y, Vt, levels=np.linspace(Vt.min(), Vt.max(), 20), colors='black', linewidths=0.5, linestyles='solid')
for q, pos in charges:
    ax.plot(*pos, 'ro' if q > 0 else 'bo', markersize=2)
ax.set_aspect('equal')
plt.xticks([])
plt.yticks([])
plt.show()
