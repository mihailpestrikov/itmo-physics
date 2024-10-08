import numpy as np
import matplotlib.pyplot as plt



x = np.array([9.0000, 10.5000, 12.0000, 13.5000])
y = np.array([0.00004762, 0.00005386, 0.00005936, 0.00006512])

A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', markersize=8)
plt.plot(x, m * x + c, 'r', label=f'y = {round(m, 10)}x + {round(c, 10)}')


plt.legend()
plt.xlabel("Ток соленоида, I_L, мкА")
plt.ylabel("Индукция магнитного поля  мкТЛ")
plt.show()

