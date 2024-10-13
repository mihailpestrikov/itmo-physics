import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


x = np.array([0, 4.56, 4.69, 4.84, 5.09, 5.2, 5.39, 5.71, 6.04, 6.38, 6.47, 7.09, 7.65, 7.79, 8.3, 9.07, 9.87, 11.07, 11.55, 12.4, 15.02])
y = np.array([1, 0.7, 0.69, 0.68, 0.66, 0.65, 0.64, 0.62, 0.6, 0.58, 0.57, 0.53, 0.5, 0.48, 0.45, 0.4, 0.34, 0.26, 0.23, 0.17, 0.01])


A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', markersize=4)
plt.plot(x, m * x + c, 'r', label=f'y = {round(m, 2)}x + {round(c, 2)}')

my_text = f"I* = 7.34 А"
plt.scatter([], [], color="w", alpha=0, label=my_text)

plt.xlabel('Сила тока I, А')
plt.ylabel('КПД')

plt.legend()
plt.show()

