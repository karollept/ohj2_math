from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
fig.suptitle("Yksikköympyrä ja kulmapisteet välillä $-3\\pi$ – $3\\pi$", fontsize=16)
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.set_xticklabels([r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$'])
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticklabels([r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$'])
#30, 45, 60, 90, 120, 150, 180, 270
pi=np.pi
ax.set_xlim(-3*pi, 3*pi)
pist_xy=np.array([pi, pi, 2*pi, pi, 4*pi, 5*pi, pi, 3*pi])
nim=np.array([6, 4, 6, 2, 6, 6, 1, 2])
varit=np.array(['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'pink', 'brown'])

text = [r'$\frac{\pi}{6}$',r'$\frac{\pi}{4}$',r'$\frac{\pi}{3}$',r'$\frac{\pi}{2}$',r'$\frac{2\pi}{3}$',r'$\frac{5\pi}{6}$',r'$\pi$',r'$\frac{3\pi}{2}$']


x = np.cos(pist_xy/nim)
y = np.sin(pist_xy/nim)

plt.scatter(x, y, color=varit, marker='*')

for i in range(len(pist_xy)):
    plt.annotate(text[i],
             xy=(np.cos(pist_xy[i]/nim[i]), np.sin(pist_xy[i]/nim[i])), xycoords='data',
             xytext=(+30, +5), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))


plt.show()