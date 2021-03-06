import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,9,20)
y = x**3
z = x**2

figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
axes_cube.plot(x,y,"blue")
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cube")


axes_square = figure.add_axes([0.15,0.6,0.25,0.25])
axes_square.plot(x,z,"red")
axes_square.set_xlabel("X Axis")
axes_square.set_ylabel("Y Axis")
axes_square.set_title("Square")

plt.show()

