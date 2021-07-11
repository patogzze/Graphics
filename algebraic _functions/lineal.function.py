import numpy as np
import matplotlib.pyplot as plt

def f(m,x,b):
  return m*x + b
N = 1000

m = (7-6)/(3-2)

x = np.linspace(-10.0, 10.0, num=N)

b = 10

y = f(m,x,b)


fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()