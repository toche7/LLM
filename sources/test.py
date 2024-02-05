import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [3,3,4,5,5] 
plt.plot(x,y)
plt.show()

import numpy as np 
xnp = np.arange(1,20)
ynp = xnp**2 - 10
plt.plot(xnp,ynp)
plt.show()

# save the plot as a file
plt.plot(xnp,ynp)
plt.savefig('plot.png')
plt.show()


