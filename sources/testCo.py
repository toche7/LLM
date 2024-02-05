# print hello world
print("Hello World")

# create number list from 20 to 100
numberList = list(range(20, 101))
print(numberList)

# create numpy array from 20 to 100 with 0.2 step
import numpy as np
x = np.arange(20, 100, 0.2)
print(x)

# create sine wave from x 
y = np.sin(x)

# plot the sine wave
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()



