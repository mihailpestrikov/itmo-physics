import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

x = np.array([4.56, 4.69, 4.84, 5.09, 5.2, 5.39, 5.71, 6.04, 6.38, 6.47, 7.09, 7.65, 7.79, 8.3, 9.07, 9.87, 11.07, 11.55, 12.4, 15.02])
y_Pr = np.array([32.38, 32.88, 33.44, 34.31, 34.58, 35.25, 36.09, 36.84, 37.39, 37.59, 38.22, 38.79, 38.17, 37.93, 36.64, 34.45, 29.67, 27.03, 22.07, 1.05])
y_Ps = np.array([14.1, 14.96, 15.93, 17.62, 18.39, 19.76, 22.17, 24.81, 27.68, 28.47, 34.18, 39.8, 41.27, 46.85, 55.94, 66.24, 83.33, 90.71, 104.56, 151.91])
y_P = np.array([46.42, 47.74, 49.27, 51.82, 52.94, 54.87, 58.13, 61.49, 64.95, 65.86, 72.18, 77.88, 79.3, 84.49, 92.33, 100.48, 112.69, 117.58, 126.23, 152.9])


x_new = np.linspace(min(x), max(x), 300)
spl_Pr = make_interp_spline(x, y_Pr, k=3)
power_smooth_Pr = spl_Pr(x_new)
spl_Ps = make_interp_spline(x, y_Ps, k=3)
power_smooth_Ps = spl_Ps(x_new)
spl_P = make_interp_spline(x, y_P, k=3)
power_smooth_P = spl_P(x_new)

plt.plot(x, y_Pr, 'o', markersize=3)
plt.plot(x, y_Ps, 'o', markersize=3)
plt.plot(x, y_P, 'o', markersize=3)
plt.plot(x_new, power_smooth_Pr, 'b', linewidth=0.5, label=f'Полезная Pr')
plt.plot(x_new, power_smooth_Ps, 'orange', linewidth=0.5, label=f'Потерь Ps')
plt.plot(x_new, power_smooth_P, 'g', linewidth=0.5, label=f'Полная P')


plt.xlabel("сила тока I, А")
plt.ylabel("мощность P, мВт")

my_text = f"I* = {round(10.18 / (2 * 0.68), 2)} А"
plt.scatter([], [], color="w", alpha=0, label=my_text)


plt.legend()
plt.show()
