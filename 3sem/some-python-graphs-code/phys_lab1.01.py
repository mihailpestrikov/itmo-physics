import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


x = np.array(['4.8', '4.88', '4.96', '5.04', '5.12', '5.2', '5.27'])
y = np.array([1.04, 1.56, 3.11, 3.89, 1.81, 0.52, 0.26])
x2 = np.array([0, 1, 2, 3, 4, 5, 6])
y2 = np.array([0.63, 1.85, 3.27, 3.44, 2.16, 0.81, 0.22])

x_new = np.linspace(min(x2), max(x2), 300)
spl = make_interp_spline(x2, y2, k=3)
power_smooth = spl(x_new)

plt.plot(x_new, power_smooth, color='r')
plt.bar(x, y, width=0.99)

plt.xlabel('t')
plt.ylabel('ΔN/NΔt')
plt.title('Histogram of timer inaccuracy')
plt.show()
