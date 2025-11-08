import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(6.4 * 3, 4.8)
fig.suptitle("kuvaaja", fontsize=16)
ax = fig.subplots()

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(x), np.sin(x)

ax.plot(x, C, color='green', linewidth=2.0, linestyle='--', label='cos(x)')
ax.plot(x, S, color='pink', linewidth=2.0, linestyle='-.', label='sin(x)')

plt.show()