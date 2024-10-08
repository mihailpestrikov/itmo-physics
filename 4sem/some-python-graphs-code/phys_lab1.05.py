import matplotlib.pyplot as plt
import numpy as np


x = np.array([0, 28.01, 57.06,	89.22,	138.90,	162.58])
y = np.array([30, 25, 20, 15, 10, 5])


A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', color='#00AAFF', markersize=8)

print(m, c)

plt.plot(x, m * x + c, 'r', linestyle='dashed')


plt.ylim(top=35, bottom=-30)
plt.xlabel('t с')
plt.ylabel('A')

plt.show()
