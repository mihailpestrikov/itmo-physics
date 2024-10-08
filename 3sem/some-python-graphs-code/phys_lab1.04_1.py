import matplotlib.pyplot as plt
import numpy as np


x1 = np.array([2.96, 5.13, 7.57, 9.52])
y1 = np.array([0.060, 0.108, 0.156, 0.204])

x2 = np.array([2.00, 3.65, 5.61, 6.48])
y2 = np.array([0.060, 0.109, 0.157, 0.206])

x3 = np.array([1.57, 2.91, 3.91, 4.96])
y3 = np.array([0.060, 0.109, 0.158, 0.206])

x4 = np.array([0.96, 2.00, 3.13, 4.26])
y4 = np.array([0.060, 0.109, 0.158, 0.207])

x5 = np.array([0.83, 1.65, 2.22, 3.00])
y5 = np.array([0.060, 0.109, 0.158, 0.207])

x6 = np.array([0.70, 1.35, 1.96, 2.43])
y6 = np.array([0.060, 0.109, 0.158, 0.208])

xes = [x1, x2, x3, x4, x5, x6]
ys = [y1, y2, y3, y4, y5, y6]

colors = ["blue", "orange", "green", "red", "purple", "brown"]

Mtr = [0.008, 0.013, 0.017,	0.023, 0.032, 0.039]


for i in range(0, 6):
    A = np.vstack([xes[i], np.ones(len(xes[i]))]).T
    m, c = np.linalg.lstsq(A, ys[i], rcond=None)[0]

    plt.plot(xes[i], ys[i], 'o', markersize=4, label=f"mark{i + 1}")
    plt.plot(xes[i], m * xes[i] + c, color=colors[i], linewidth=0.5, label=f"y = {round(m, 3)}x + {Mtr[i]}")


plt.legend()
plt.xlabel('Угловое ускорение Epsilon')
plt.ylabel('Момент натяжения нити M')

plt.show()
