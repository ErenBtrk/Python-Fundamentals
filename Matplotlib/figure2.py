import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,9,20)
y = x**3
z = x**2

figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend(loc=4)

plt.show()

