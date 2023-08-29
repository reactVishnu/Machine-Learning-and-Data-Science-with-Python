import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 10, 11)
b = a**4
x = np.arange(10)
y = 2*x

fig = plt.figure(figsize=(5, 5), dpi=200)

# Big One
axes1 = fig.add_axes([0.2, 0.1, 0.7, 0.8])
axes1.plot(a, b)
axes1.set_title('Large Set')
axes1.set_xlabel('A')
axes1.set_ylabel('B')
axes1.set_xlim(0, 10)
axes1.set_ylim(0, 8000)
axes2 = fig.add_axes([0.3, 0.5, 0.3, 0.2])
axes2.plot(x, y)
axes2.set_title('Small Set')
axes2.set_xlabel('X')
axes2.set_ylabel('Y')
axes2.set_xlim(0, 8)
axes2.set_ylim(0, 17)

plt.show(bbox_inches='tight')

fig.savefig('first_fig', bbox_inches='tight')
