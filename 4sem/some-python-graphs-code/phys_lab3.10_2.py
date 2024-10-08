import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

x = np.array([75.858, 85.858, 95.858, 105.858, 115.858, 125.858, 135.858, 145.858,
              155.858, 165.858, 175.858, 275.858, 375.858, 475.858])
y = np.array([12.841, 11.896, 11.109, 10.336, 9.880, 9.274,
              9.040, 8.695, 8.443, 8.389, 8.161, 6.919, 6.465, 6.402])


x_new = np.linspace(min(x), max(x), 300)
spl_Pr = make_interp_spline(x, y, k=3)
power_smooth_Pr = spl_Pr(x_new)
plt.plot(x, y, 'o', color='#00AAFF', markersize=6)
plt.plot(x_new, power_smooth_Pr, linewidth=1, color='#00AAFF')

plt.xlabel('Споротивление контура R Ом')
plt.ylabel('Добротность Q')


plt.ylim(bottom=0)
plt.show()
