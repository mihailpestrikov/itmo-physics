import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error


L = np.array([800, 700, 600, 500, 400])
delta_x = np.array([10, 9.11, 7.89, 6.89, 6.11])
_lambda = 632.82 * 10 ** (-9)
delta_lambda = 0.01 * 10 ** (-9)


def calculate_error(Xs, ys, K, b):
    mse = mean_squared_error(ys, (K * Xs + b)) * 5 / 3
    delta_k = np.sqrt(mse / np.sum((Xs - np.mean(Xs)) ** 2))
    delta_d = np.sqrt((delta_lambda / K) ** 2 + (_lambda * delta_k / K ** 2) ** 2)
    return delta_d


A = np.vstack([L, np.ones(len(L))]).T
m, c = np.linalg.lstsq(A, delta_x, rcond=None)[0]

plt.figure(figsize=(12, 5), dpi=250)

plt.plot(L, delta_x, 'o', color='#00AAFF', markersize=8)

plt.plot(L, m * L + c, 'r', linestyle='dashed', label=f'K = {round(m, 3)}')

plt.xlabel('L, мм')
plt.ylabel('$\\Delta x, мм$')

delta_b = calculate_error(L, delta_x, m, c)
print('Погрешность для щели для объекта 33: {} мкм'.format(int(round(delta_b * 10 ** 6))))


plt.legend()
plt.show()
