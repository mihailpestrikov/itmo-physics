import matplotlib.pyplot as plt
import numpy as np

x = np.array([15.02, 12.4, 11.55, 11.07, 9.87, 9.07, 8.3, 7.79, 7.65, 7.09, 6.47, 6.38, 6.04, 5.71, 5.39, 5.2, 5.09, 4.84, 4.69, 4.56])
y = np.array([0.07, 1.78, 2.34, 2.68, 3.49, 4.04, 4.57, 4.9, 5.07, 5.39, 5.81, 5.86, 6.1, 6.32, 6.54, 6.65, 6.74, 6.91, 7.01, 7.1])


A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', markersize=3)
plt.plot(x, m * x + c, 'r', linewidth=0.5, label=f'y = {round(m, 2)}x + {round(c, 2)}')

plt.xlabel("сила тока I, А")
plt.ylabel("напряжение U, В")

my_text = f"E = {round(c, 2)} В \nr = {abs(round(m, 2))} Ом"
plt.scatter([], [], color="w", alpha=0, label=my_text)

plt.legend()
plt.show()


