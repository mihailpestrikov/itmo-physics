import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x = np.array([1396.1008, 1484.7103, 1534.4264, 1580.1307, 1625.4750, 1688.0478,
              1725.7246, 1772.1798, 1818.4598, 1866.6392, 1906.9724, 1940.4716, 1975.1724, 2000.8105, 2011.6341])
y = np.array([0.329, 0.300, 0.291, 0.286, 0.283, 0.276, 0.270,
              0.265, 0.263, 0.258, 0.256, 0.254, 0.252, 0.251, 0.249])

plt.figure(dpi=250)

f = interp1d(x, y, kind='cubic')
x_new = np.linspace(min(x), max(x), num=100, endpoint=True)
y_new = f(x_new)


plt.plot(x, y, 'o', color='#00AAFF', markersize=4)
plt.plot(x_new, y_new, linewidth=1, color='#00AAFF')


plt.xlabel('Температура, K')
plt.ylabel('Интегральный коэффициента излучения источника')

plt.show()



