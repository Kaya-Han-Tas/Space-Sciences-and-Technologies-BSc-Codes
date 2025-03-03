import numpy as np
import matplotlib.pyplot as plt

x,y = np.meshgrid(np.linspace(-2,2,10),np.linspace(0,5,10))

u = 0.5+(0.8*x)
v = 1.5-(0.8*y)

plt.quiver(x,y,u,v)
plt.show()