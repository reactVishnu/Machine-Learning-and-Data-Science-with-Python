import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 11)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, x, label='X v X')
ax.plot(x, x**2, label='X v X**2')
ax.legend(loc=(0.5,0.5))
plt.show()
