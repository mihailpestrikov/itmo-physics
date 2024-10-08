import matplotlib.pyplot as plt
import numpy as np



x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400])
y = np.array([0.3360, 0.3756, 0.4169, 0.4681, 0.5053, 0.5658,
              0.5938, 0.6412, 0.6816, 0.6911, 0.7346, 1.1932, 1.7853, 1.9951])


A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', color='#00AAFF', markersize=8)
plt.plot(x, m * x + c, 'r', label=f'y = {round(m, 5)}x + {round(c, 4)} '
                                  f'\n lambda(0) = 0,3360'
                                  f'\n lambda(R) = 0 при R = -75,8581')

plt.xlabel('Сопротивление R Ом')
plt.ylabel('Логарифмичсекий декремент lambda')

plt.legend()
plt.show()