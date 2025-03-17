import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

h = 6.626e-34
h_cut = 1.055e-34
m = 9.109e-31
e_const = 1.602e-19


U_eV = 1
a = 3e-10
b = 6e-10

U = U_eV * e_const
alpha_0  = np.sqrt(2 * m * U / (h_cut ** 2))
hbar = h_cut / (2 * np.pi)


def kp_p(e):  # e > 1
    return ((1 - 2 * e) / (2 * (e * (e - 1)) ** (1 / 2)) *
            np.sin(alpha_0 * a * e ** (1 / 2)) * np.sin(alpha_0 * b * (e - 1) ** (1 / 2)) +
            np.cos(alpha_0 * a * e ** (1 / 2)) * np.cos(alpha_0 * b * (e - 1) ** (1 / 2)))

def kp_n(e):  # e < 1
    return ((1 - 2 * e) / (2 * (e * (1 - e)) ** (1/2)) *
            np.sin(alpha_0 * a * e ** (1 / 2)) * np.sinh(alpha_0 * b * (1 - e) ** (1 / 2)) +
            np.cos(alpha_0 * a * e ** (1 / 2)) * np.cosh(alpha_0 * b * (1 - e) ** (1 / 2)))

def kronig_penney(e):
    return np.piecewise(e, [e > 1, e < 1], [kp_p, kp_n])

e = np.linspace(0.1, 10, int(1e5))
kp = kronig_penney(e)


plt.figure(figsize=(10, 6))
plt.plot(e, kp, 'b', label="kp(e)")
plt.plot([e[0], e[-1]], [1, 1], 'r--', label="y=1")
plt.plot([e[0], e[-1]], [-1, -1], 'g--', label="y=-1")
plt.ylim([np.min(kp) - 0.5, 3])
plt.xlabel("E")
plt.ylabel("kp")
plt.title(f"График правой части уравнения Кронига-Пенни для U={U_eV} eV; a={a * 1e10:.1f} и b={b * 1e10:.1f}")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.xlabel("Wave Vector, k (m^-1)")
plt.ylabel("Energy, E (eV)")
plt.title(f"Приведенное зонное представление зависимости энергии от волнового вектора для U={U_eV} eV; "
          f"a={a * 1e10:.1f} and b={b * 1e10:.1f}")
xticks = np.array([-np.pi, -np.pi/2, 0, np.pi/2, np.pi]) / (a + b)
xtick_labels = [r"-$\pi/(a+b)$", r"-$\pi/2(a+b)$", "0", r"$\pi/2(a+b)$", r"$\pi/(a+b)$"]
plt.xticks(xticks, xtick_labels)
plt.grid(True)
h1 = plt.gca()

plt.figure(figsize=(10, 6))
plt.xlabel("Wave Vector, k (m^-1)")
plt.ylabel("Energy, E (eV)")
plt.title(f"Расширенное зонное представление зависимости энергии от волнового вектора для U={U_eV} eV; "
          f"a={a * 1e10:.1f} and b={b * 1e10:.1f}")
xticks = np.arange(-6, 7, 2) * np.pi / (a + b)
xtick_labels = [f"{i}π/(a+b)" if i != 0 else "0" for i in range(-6, 7, 2)]
plt.xticks(xticks, xtick_labels)
plt.grid(True)
h2 = plt.gca()




def plot_bands(h1, h2, wave_vector, energy, zone_index, period):
    h1.plot(wave_vector, energy, 'b')
    h1.plot(-wave_vector[::-1], energy[::-1], 'b')

    # перевод из приведенного зонного представления в расширенное
    if zone_index % 2 == 1:
        if zone_index == 1:
            h2.plot(wave_vector, energy, 'b')
            h2.plot(-wave_vector[::-1], energy[::-1], 'b')
        else:
            h2.plot(wave_vector + period * (zone_index - 1), energy, 'b')
            h2.plot(-wave_vector[::-1] - period * (zone_index - 1), energy[::-1], 'b')
    else:
        h2.plot(wave_vector - period * zone_index, energy, 'b')
        h2.plot(-wave_vector[::-1] + period * zone_index, energy[::-1], 'b')

grid = np.pi / (a + b)

allowed_zone = abs(kp) <= 1

zone_index = 1
last_position = 1


while allowed_zone.any() and zone_index < 6:
    # найти первую разрешённую зону
    positions_start = np.where(allowed_zone)[0]
    if len(positions_start) == 0:
        break

    first_position = last_position + positions_start[0] - 1
    allowed_zone = allowed_zone[positions_start[0]:]

    # найти конец текущей разрешённой зоны
    positions_end = np.where(~allowed_zone)[0]
    if len(positions_end) == 0:
        break

    last_position = first_position + positions_end[0] - 1
    allowed_zone = allowed_zone[positions_end[0]:]

    # вычислить векторы и энергии
    wave_vector = np.arccos(kp[first_position:last_position - 1]) / (a + b)
    energy = e[first_position:last_position - 1] * U_eV

    plot_bands(h1, h2, wave_vector, energy, zone_index, grid)
    zone_index += 1

plt.show()




def energy_free_electron(k_vals):
    return (h_cut ** 2 * k_vals ** 2) / (2 * m) / U_eV

def plot_energy_free_electron(k_vals):
    energies = energy_free_electron(k_vals)
    plt.figure(figsize=(10, 6))
    plt.xlabel("Wave Vector, k (m^-1)")
    plt.ylabel("Energy, E (eV)")
    plt.title("Дисперсия свободного электрона")
    plt.plot(k_vals, energies, 'b-')
    plt.grid(True)
    plt.show()

k_vals = np.linspace(-grid / 2, grid / 2, 100)

plot_energy_free_electron(k_vals)


def infinite_well_levels(a, n_max):
    levels = []
    for n in range(1, n_max + 1):
        E_n = (n ** 2 * np.pi ** 2 * hbar ** 2) / (2 * m * a ** 2)
        levels.append(E_n)
    return np.array(levels) / U_eV


def plot_infinite_well_levels(a, n_max):
    levels = infinite_well_levels(a, n_max)
    plt.figure(figsize=(10, 6))
    plt.xlabel("Wave Vector, k (m^-1)")
    plt.ylabel("Energy, E (eV)")
    plt.title("Энергетические уровни в бесконечном потенциальном колодце")
    for n in range(1, n_max + 1):
        plt.hlines(levels[n-1], 0, n_max + 1, colors='b', linestyles='solid')
    plt.xlim(0, n_max + 1)
    plt.ylim(0, np.max(levels) * 1.1)
    plt.grid(True)
    plt.show()


plot_infinite_well_levels(a, 10)



def calculate_band_gaps(e, kp):
    allowed = abs(kp) <= 1
    band_gaps = []

    positions = np.where(allowed)[0]

    # рассматриваем разрешенные зоны, если есть разрыв - считаем размер разрыв
    for i in range(1, len(positions)):
        if positions[i] - positions[i - 1] > 1:
            start = e[positions[i - 1]]
            end = e[positions[i]]
            band_gap = end - start
            band_gaps.append((start, end, band_gap))

    return band_gaps

band_gaps = calculate_band_gaps(e, kp)

for i, (start, end, gap) in enumerate(band_gaps):
    print(f"Band gap {i + 1}: Start = {start:.4f} eV, End = {end:.4f} eV, Size = {gap:.4f} eV")
