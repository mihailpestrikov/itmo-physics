import matplotlib.pyplot as plt
from aperture_distributions import *

# Размеры сетки
N = 1000
Lx = Ly = 100  # Размер области объекта в миллиметрах
# Интервалы дискретизации вдоль осей x и y соответственно.
dx = Lx / N
dy = Ly / N

# Длина волны и расстояние до плоскости наблюдения
wavelength = 500e-6  # 500 мм, green-blue light
L = 1e3  # 100 мм

# Координаты
x = np.linspace(-Lx / 2, Lx / 2, N)
y = np.linspace(-Ly / 2, Ly / 2, N)

aperture_size = 1  # Параметр размера апертуры, 1 мм
# Для получения апертуры в высоком разрешении
# aperture_size = aperture_size * 10

aperture = hollow_hexagonal_aperture_distribution(x, y, aperture_size)

# Преобразование Фурье и получение частот
U = np.fft.fftn(aperture) * dx * dy
fx = np.fft.fftfreq(N, dx)
fy = np.fft.fftfreq(N, dy)

# Центрирование до центра спектра
U = np.fft.fftshift(U)
fx = np.fft.fftshift(fx)
fy = np.fft.fftshift(fy)

# Нормирование полученных частот к исходным
x_image = fx * wavelength * L
y_image = fy * wavelength * L

# Масштабирование результата преобразования Фурье
k = 2 * np.pi / wavelength
U = np.exp(1j * k * L) * np.exp(1j * k * (x**2 + y**2) / (2 * L)) / (1j * wavelength * L) * U

I = np.abs(U)

plt.imshow(I, extent=(min(x_image), max(x_image), min(y_image), max(y_image)), cmap='gray')
plt.xlabel('x (мм)')
plt.ylabel('y (мм)')
plt.title('Интенсивность в плоскости наблюдения')
plt.colorbar(label='Интенсивность')
plt.show()

plt.imshow(aperture, extent=(x.min(), x.max(), y.min(), y.max()), cmap='gray')
plt.xlabel('x (мм)')
plt.ylabel('y (мм)')
plt.title('Апертура')
plt.show()
