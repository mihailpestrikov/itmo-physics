import matplotlib.pyplot as plt
import numpy as np


x = np.array([0.058, 0.131, 0.214, 0.269, 0.341, 0.396, 0.469])
y = np.array([17.864, 25.870, 33.908, 41.738, 49.672, 55.034, 60.312])
my_xticks = np.array([0.058, 0.131, 0.214, 0.269, 0.341, 0.396, 0.469])
my_yticks = np.array([17.864, 25.870, 33.908, 41.738, 49.672, 55.034, 60.312])

plt.xticks(x, my_xticks)
plt.yticks(y, my_yticks)

A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', markersize=8)
plt.plot(x, m * x + c, 'r', label=f'y = {round(m, 2)}x + {round(c, 2)}')

plt.xlabel('a м/с^2')
plt.ylabel('T мН')

plt.legend()
plt.show()


