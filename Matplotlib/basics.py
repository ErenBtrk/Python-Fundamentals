import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,"o--r")
plt.axis([0,6,0,20])

plt.title("Graphic Title")
plt.xlabel("x label")

plt.ylabel("y label")
plt.yticks(np.arange(0,17))

plt.show()