import numpy as np
import matplotlib.pyplot as plt
import csv

dt = np.dtype(">f8")
osciData = np.fromfile('test.bin', dtype=dt)

np.savetxt("test.csv", osciData, delimiter=",")

plt.plot(osciData)
plt.show()