import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.006, 0.010, 0.016, 0.023, 0.031, 0.041])
y = np.array([0.017, 0.024, 0.033, 0.034, 0.053, 0.064])

plt.yticks(y, y)
plt.xticks(x, x)


A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, "o")
plt.plot(x, m * x + c, 'r', label=f'y = {round(m, 2)}x + {round(c, 2)}')

my_text = f"m = {round(m, 2) / 4}"
plt.scatter([], [], color="w", alpha=0, label=my_text)

plt.xlabel('R^2')
plt.ylabel('moment of inertia I')

plt.legend()
plt.show()
