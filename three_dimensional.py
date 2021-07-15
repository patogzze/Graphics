from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

fig ,ax = plt.subplots(subplot_kw={"projection": "3d"})

res = 100
X = np.linspace(-4, 4, res)
Y = np.linspace(-4, 4, res)

X, Y = np.meshgrid(X,Y)

Z = np.sin(X) + 2*np.sin(Y)

surf = ax.plot_surface(X, Y, Z, cmap=cm.cool, linewidth=0, antialiased=False)

fig.colorbar(surf)
plt.show()
