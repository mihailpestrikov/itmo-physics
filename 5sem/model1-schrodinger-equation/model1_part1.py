import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

hbar = 1.055
m = 0.91 # Масса частицы
a = 1.0  # половина ширины потенциальной ямы, нм
U = 30  # глубина потенциальной ямы, эВ
beta = 2 * m * U * a**2 / hbar**2  # бета-параметр

# Функции для трансцендентных уравнений
def even_func(z, beta):
    if z >= np.sqrt(beta):
        return np.nan
    return z * np.tan(z) - np.sqrt(beta - z**2)

def odd_func(z, beta):
    if z >= np.sqrt(beta):
        return np.nan
    return -z / np.tan(z) - np.sqrt(beta - z**2)


# Поиск собственных значений z, удовлетворяющих трансцендентным уравнениям,
# которые соответствуют собственным энергиям частиц в яме.
z_values = []
parities = []  # True для четных, False для нечетных

max_n = 6 # максимальное количество уровней энергии

z_initials = np.linspace(0.1, np.sqrt(beta) - 0.1, 1000)

n_found = 0
z_prev = 0

while n_found < max_n:
    for z0 in z_initials:
        if z0 <= z_prev:
            continue
        try:
            if n_found % 2 == 0:  # Четное состояние
                sol = root_scalar(even_func, args=(beta,), bracket=[z0, z0 + 0.1], method='bisect')
                parity = True
            else:  # Нечетное состояние
                sol = root_scalar(odd_func, args=(beta,), bracket=[z0, z0 + 0.1], method='bisect')
                parity = False

            if sol.converged and sol.root > z_prev:
                z_values.append(sol.root)
                parities.append(parity)
                z_prev = sol.root
                n_found += 1
                break
        except ValueError:
            pass
    else:
        break

# Сортировка решений
z_values, parities = zip(*sorted(zip(z_values, parities)))


# Построение волновых функций
x = np.linspace(-2 * a, 2 * a, 1000)

def wave_function(x, z, beta, even):
    k = z / a
    kappa = np.sqrt(beta - z**2) / a

    if even:
        A = np.cos(k * a)
        psi_inside = np.cos(k * x)
        psi_outside = A * np.exp(-kappa * (np.abs(x) - a))
    else:
        A = np.sin(k * a)
        psi_inside = np.sin(k * x)
        psi_outside = A * np.exp(-kappa * (np.abs(x) - a)) * np.sign(x)

    psi = np.where(np.abs(x) <= a, psi_inside, psi_outside)

    norm_factor = np.sqrt(np.trapezoid(psi**2, x))
    return psi / norm_factor

E_values = [z**2 for z in z_values]

plt.figure(figsize=(12, 8))

for i, (z, parity) in enumerate(zip(z_values, parities)):
    psi = wave_function(x, z, beta, even=parity)
    plt.plot(x, psi + E_values[i], label=f'n={i + 1}, E~{E_values[i]:.2f} (эВ)')

for i, E in enumerate(E_values):
    plt.axhline(E, color='gray', linestyle='--', alpha=0.7)
    plt.text(1.1 * a, E, f'{E:.2f} эВ', va='center')

plt.axvline(-a, color='k', linestyle='--', label="Границы ямы (нм)")
plt.axvline(a, color='k', linestyle='--')

plt.xlabel('x, нм')
plt.ylabel('Энергия, эВ')
plt.title('Собственные волновые функции и уровни энергии (положительная шкала)')
plt.legend(loc='upper right')
plt.grid()
plt.show()
