import matplotlib.pyplot as plt
import numpy as np

fig,axs = plt.subplots(2,2)

x = np.linspace(0,2,100)

fig.suptitle("Graphics Title")

axs[0,0].plot(x,x,color = "red")
axs[0,1].plot(x,x**2,color = "blue")
axs[1,0].plot(x,x**3,color = "green")
axs[1,1].plot(x,x**4,color = "pink")

plt.tight_layout()
plt.show()