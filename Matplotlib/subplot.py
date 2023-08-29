import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,10,11)
b = a**4
x = np.arange(0,5)
y = 2*x

fig, axes = plt.subplots(nrows=2,ncols=2)
print(axes)
axes[0][0].plot(a, b)
axes[0][0].set_title('[0][0]')
axes[1][1].plot(x, y)
axes[1][1].set_title('[1][1]')
plt.tight_layout()
fig.suptitle('Figure 1')
fig.subplots_adjust(wspace=0.5,hspace=0.5)
plt.show()

