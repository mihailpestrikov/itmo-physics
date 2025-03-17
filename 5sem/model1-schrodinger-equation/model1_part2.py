import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


m = 9.109e-31 # масса электрона
hbar = 1.055e-34 # приведенная постоянная Планка.
E = 1.6e-19 # энергия частицы
U0 = 2e-19 # максимальная энергия потенциального барьера
h = 0.8e-9 # ширина потенциального барьера


x_min, x_max = -3.64e-9, 3e-9 # пределы по x, в которых будет вычисляться волновая функция
dx = 1e-12 # шаг по x


psi1_0 = 1.0 # начальное значение для волновой функции на первой итерации расчета.
k_0 = np.sqrt(2 * m * E) / hbar # волновое число
psi2_0 = 1j * k_0 * psi1_0 # первая производная волновой функции


def potential(x, h):
    if 0 <= x <= h:
        return U0 * (1 - ((x - h/2)/(h/2))**2)
    return 0


def runge_kutta_4(psi1, psi2, x, dx, E, m, hbar, h):
    def f1(psi1, psi2):
        return psi2

    def f2(psi1, psi2, x):
        return -2 * m / hbar ** 2 * (E - potential(x, h)) * psi1

    k1_1 = dx * f1(psi1, psi2)
    k1_2 = dx * f2(psi1, psi2, x)

    k2_1 = dx * f1(psi1 + 0.5 * k1_1, psi2 + 0.5 * k1_2)
    k2_2 = dx * f2(psi1 + 0.5 * k1_1, psi2 + 0.5 * k1_2, x + 0.5 * dx)

    k3_1 = dx * f1(psi1 + 0.5 * k2_1, psi2 + 0.5 * k2_2)
    k3_2 = dx * f2(psi1 + 0.5 * k2_1, psi2 + 0.5 * k2_2, x + 0.5 * dx)

    k4_1 = dx * f1(psi1 + k3_1, psi2 + k3_2)
    k4_2 = dx * f2(psi1 + k3_1, psi2 + k3_2, x + dx)

    psi1_new = psi1 + (k1_1 + 2 * k2_1 + 2 * k3_1 + k4_1) / 6
    psi2_new = psi2 + (k1_2 + 2 * k2_2 + 2 * k3_2 + k4_2) / 6

    return psi1_new, psi2_new


def calculate_transmission_coefficient(h):
    psi_values = []
    psi_modulus = []

    psi1, psi2 = psi1_0, psi2_0
    for x in x_values:
        psi_values.append(psi1)
        psi_modulus.append(abs(psi1.real) ** 2)
        psi1, psi2 = runge_kutta_4(psi1, psi2, x, dx, E, m, hbar, h)


    psi_right = psi_modulus[np.argmax(x_values > h)]

    T = (psi_right / abs(np.exp(1j * k_0 * h)))**2
    return T, psi_values



x_values = np.arange(x_min, x_max, dx)

T_0, psi_values = calculate_transmission_coefficient(h)

print(f"Коэффициент прохождения: T = {T_0:.6f}")

plt.figure(figsize=(10, 6))
plt.plot(x_values, psi_values, label="Волновая функция psi(x)")
plt.axvline(0, color='red', linestyle='--', label="Границы барьера")
plt.axvline(h, color='red', linestyle='--')
plt.xlabel("x, м^-9")
plt.ylabel("Re(psi(x)), м^-1/2")
plt.title("Прохождение частицы через потенциальный барьер")
plt.legend()
plt.grid()
plt.show()


h_values = np.linspace(4.88e-10, 9e-10, 100)
T_values = [calculate_transmission_coefficient(h)[0] for h in h_values]
last_index = next((i for i, t in reversed(list(enumerate(T_values))) if t >= 1), -1)
if last_index != -1:
    T_values[:last_index + 1] = [1] * (last_index + 1)

plt.figure(figsize=(10, 6))
plt.plot(h_values, T_values, label="Коэффициент прохождения T(h)")
plt.xlabel("h, м^-10")
plt.ylabel("T")
plt.title("Зависимость коэффициента прохождения от ширины барьера")
plt.grid()
plt.legend()
plt.show()
