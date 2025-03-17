import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x = np.array([1396.1008, 1484.7103, 1534.4264, 1580.1307, 1625.4750, 1688.0478,
              1725.7246, 1772.1798, 1818.4598, 1866.6392, 1906.9724, 1940.4716, 1975.1724, 2008.8105, 2011.6341])
y = np.array([949.96, 1106.96, 1227.20, 1354.62, 1500.59, 1668.96, 1821.25,
             1988.25, 2186.22, 2379.15, 2575.46, 2731.41, 2910.40, 3099.70, 3130.40])

plt.figure(dpi=250)

f = interp1d(x, y, kind='cubic')
x_new = np.linspace(min(x), max(x), num=100, endpoint=True)
y_new = f(x_new)
P_2000 = f(2000)


plt.plot(x, y, 'o', color='#00AAFF', markersize=4)
plt.plot(x_new, y_new, linewidth=1, color='#00AAFF')

plt.text(1400, 3000, f'$P_{{2000}} = {np.round(P_2000, 2)}$', fontsize=12)

plt.xlabel('Температура, K')
plt.ylabel('Мощность, Вт')

plt.show()

