import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,100)

plt.plot(x,x,label="linear",color = "red")
plt.plot(x,x**2,label="quadratic",color = "blue")
plt.plot(x,x**3,label="cubic",color = "green")

plt.xlabel("x label")
plt.ylabel("y label")

plt.legend()
plt.title("Simple Plot")

plt.show()