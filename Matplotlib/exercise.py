import matplotlib.pyplot as plt
import numpy as np

m = np.linspace(0, 10, 11)
c = 3*10**8
e = m*c**2
print(e)
plt.plot(e, m)
plt.show()
