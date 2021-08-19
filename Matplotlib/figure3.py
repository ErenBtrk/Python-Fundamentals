import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,9,20)
y = x**3
z = x**2

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,8))

axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("figure1.pdf")

plt.show()

