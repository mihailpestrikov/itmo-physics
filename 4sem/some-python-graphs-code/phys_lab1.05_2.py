import matplotlib.pyplot as plt
import numpy as np


x = np.array([0.032, 0.036, 0.040, 0.046, 0.053, 0.060])
y = np.array([2.656, 2.982, 3.320, 3.818, 4.2951, 4.916])


A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', color='#00AAFF', markersize=8)

plt.plot(x, m * x + c, 'r', label=f'y = {round(m, 5)}x + {round(c, 4)}')


plt.xlabel('Момент инерции, I')
plt.ylabel('Квадрат периода колебаний, $T^2$')

plt.legend()
plt.show()


