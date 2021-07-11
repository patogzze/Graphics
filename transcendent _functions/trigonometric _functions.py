import numpy as np
import matplotlib.pyplot as plt
from math import pi

def f(x):
  return np.sin(x)

N = 1000

x = np.linspace(-2*pi, 2*pi, num=N)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()