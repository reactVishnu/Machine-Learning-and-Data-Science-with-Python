import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,6)
print(x)
y = 2*x
print(y)
plt.plot(x,y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('y=2x Relationship')
plt.xlim(0,5)
plt.ylim(0,10)
plt.savefig('myfirst_graph')
plt.show()

#saving the figure
