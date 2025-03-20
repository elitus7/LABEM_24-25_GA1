import numpy as np
import matplotlib.pyplot as plt

# Definim el camp elèctric d'una càrrega puntual
def E(q, r0, x, y):
    rx, ry = x - r0[0], y - r0[1]
    dist = (rx**2 + ry**2)**1.5
    return q * rx / dist, q * ry / dist

# Definim el potencial elèctric
def V(q, r0, x, y):
    return q / np.hypot(x - r0[0], y - r0[1])

# Malla
x = np.linspace(-6, 6, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

q1, q2 = 1, -1
d = 4
charges = [(q1, (d/2, 0)), (q2, (-d/2, 0))]

Ex, Ey = np.zeros(X.shape), np.zeros(Y.shape)
Vt = np.zeros(X.shape)
for q, pos in charges:
    ex, ey = E(q, pos, X, Y)
    Ex += ex
    Ey += ey
    Vt += V(q, pos, X, Y)

fig, ax = plt.subplots()
ax.streamplot(X, Y, Ex, Ey, color=np.log(np.hypot(Ex, Ey)), linewidth=0.7, cmap=plt.cm.plasma, density=1)
ax.contour(X, Y, Vt, levels=np.linspace(-2, 2, 20), colors='black', linestyles='solid', linewidths=0.5)

for q, pos in charges:
    color = 'red' if q < 0 else 'blue'
    ax.scatter(*pos, color=color, s=100)

ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
plt.show()
