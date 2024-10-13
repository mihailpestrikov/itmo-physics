import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray
from scipy.interpolate import PchipInterpolator


def divide_each_array_element(a: ndarray, b: ndarray) -> ndarray:
    y_new = np.array([])
    for i in range(1, len(a)):
        y_new = np.append(y_new, a[i] / b[i])
    return y_new

y1 = np.array([0.2265, 0.2264, 0.2263, 0.2262, 0.2261, 0.226, 0.2259, 0.2256, 0.2225, 0.2143, 0.1868, 0.146, 0.1245, 0.1051, 0.0883, 0.0747, 0.0629, 0.0576, 0.0517, 0.0443, 0.0405, 0.0376, 0.0343, 0.0325, 0.0313])
x1 = np.array([0.0, 0.02, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.43, 0.45, 0.47, 0.49, 0.5])
y1_new = np.array(divide_each_array_element(y1, x1))

y2 = np.array([0.2692, 0.2691, 0.2688, 0.2687, 0.2686, 0.2685, 0.2684, 0.2683, 0.2682, 0.2614, 0.2507, 0.1943, 0.1459, 0.1246, 0.1133, 0.1003, 0.084, 0.0702, 0.0618, 0.0543, 0.05, 0.046, 0.0431, 0.0417])
x2 = np.array([0.0, 0.02, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.35, 0.38, 0.4, 0.42, 0.45, 0.47, 0.49, 0.5])
y2_new = np.array(divide_each_array_element(y2, x2))

y3 = np.array([0.3168, 0.3166, 0.3165, 0.3164, 0.3163, 0.3162, 0.3161, 0.316, 0.3153, 0.3093, 0.2925, 0.2484, 0.1951, 0.1561, 0.1373, 0.1266, 0.113, 0.1031, 0.0905, 0.083, 0.0752, 0.0677, 0.0607, 0.0579, 0.0538])
x3 = np.array([0.0, 0.02, 0.04, 0.06, 0.08, 0.11, 0.13, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.44, 0.46, 0.48, 0.5])
y3_new = np.array(divide_each_array_element(y3, x3))

y4 = np.array([0.367, 0.3669, 0.3667, 0.3664, 0.3662, 0.366, 0.3658, 0.3657, 0.3648, 0.3604, 0.3514, 0.3076, 0.2286, 0.2, 0.1676, 0.1502, 0.1396, 0.1254, 0.1139, 0.1039, 0.0957, 0.0851, 0.079, 0.0717, 0.0676])
x4 = np.array([0.0, 0.02, 0.04, 0.06, 0.09, 0.12, 0.14, 0.17, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.44, 0.46, 0.48, 0.5])
y4_new = np.array(divide_each_array_element(y4, x4))


# Интерполяция по сплайнам Эрмита
f1 = PchipInterpolator(x1[1::], y1_new)
f2 = PchipInterpolator(x2[1::], y2_new)
f3 = PchipInterpolator(x3[1::], y3_new)
f4 = PchipInterpolator(x4[1::], y4_new)

x_dense1 = np.linspace(min(x1), max(x1), 1000)
x_dense2 = np.linspace(min(x2), max(x2), 1000)
x_dense3 = np.linspace(min(x3), max(x3), 1000)
x_dense4 = np.linspace(min(x4), max(x4), 1000)


plt.plot(x_dense1, f1(x_dense1), color='#4682B4', label='U = 9')
plt.plot(x_dense2, f2(x_dense2), color='#D2691E', label='U = 10.5')
plt.plot(x_dense3, f3(x_dense3), color='#20B2AA', label='U = 12')
plt.plot(x_dense4, f4(x_dense4), color='#FF6347', label='U = 13.5')

plt.legend()
plt.xlabel("Ток соленоида, I_L, мкА")
plt.ylabel("Отношение анодного тока к току соленоида, I_a/I_L, мкА")
plt.show()

