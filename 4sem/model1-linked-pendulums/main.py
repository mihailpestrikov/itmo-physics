from dataclasses import dataclass, field

import matplotlib.pyplot as plt
import numpy as np
from config import *


k = 0.3  # rigidity coefficient
m = 1  # mass
L = 8  # length
L1 = L * 0.5  # distance of spring from pendulum mounting point

beta = 10 * BETA_SCALE  # attenuation coefficient
#  Let's assume that beta = 0.1 is 100% of attenuation
#  as pendulum completes only one oscillation with this coefficient.
#  Therefore, beta is specified as a percentage of the attenuation coefficient.

phi_1_initial = math.pi / 6  # initial angle of deflection of second pendulum
phi_2_initial = 0  # initial angle of deflection of second pendulum

omega_n1 = math.sqrt(g / L)  # natural frequency of the first pendulum
omega_n2 = math.sqrt(g / L + 2 * (k * L1 ** 2) / (m * L ** 2))  # natural frequency of the second pendulum

phi_01 = 0  # phase of first pendulum
phi_02 = 0  # phase of second pendulum

A1 = (phi_1_initial + phi_2_initial) / 2  # amplitude of first pendulum
A2 = (phi_1_initial - phi_2_initial) / 2  # amplitude of second pendulum


@dataclass
class CalculationResult:
    phi_1: list[float] = field(default_factory=lambda: list())
    phi_2: list[float] = field(default_factory=lambda: list())
    v_1: list[float] = field(default_factory=lambda: list())
    v_2: list[float] = field(default_factory=lambda: list())
    time: list[float] = field(default_factory=lambda: list())


result = CalculationResult()


# calculates deflection angle using general solution for natural
# coordinates until deflection angle of any pendulum get less than ACCURACY_LIMIT
def calculate_pendulums_deflection_angles():
    seconds = 0

    result.phi_1.append(phi_1_initial)
    result.phi_2.append(phi_2_initial)
    result.time.append(seconds)

    phi_1 = 1
    phi_2 = 1

    while abs(phi_1) > ACCURACY_LIMIT or abs(phi_2) > ACCURACY_LIMIT or seconds < 50:
        seconds += TIME_INTERVAL

        damping_function = math.exp(-seconds * beta)

        phi_1 = damping_function * (A1 * math.cos(omega_n1 * seconds + phi_01) +
                                    A2 * math.cos(omega_n2 * seconds + phi_02))

        phi_2 = damping_function * (A1 * math.cos(omega_n1 * seconds + phi_01) -
                                    A2 * math.cos(omega_n2 * seconds + phi_02))

        result.phi_1.append(phi_1)
        result.phi_2.append(phi_2)
        result.time.append(seconds)


# calculates derivatives of phi for each value to get rotational speed
def calculate_pendulums_velocities():
    seconds = 0

    for i in range(len(result.time)):
        damping_function = math.exp(-seconds * beta)

        v_1 = damping_function * (-A1 * omega_n1 * math.sin(omega_n1 * seconds + phi_01) -
                                  A2 * omega_n2 * math.sin(omega_n2 * seconds + phi_02))

        v_2 = damping_function * (-A1 * omega_n1 * math.sin(omega_n1 * seconds + phi_01) +
                                  A2 * omega_n2 * math.sin(omega_n2 * seconds + phi_02))

        result.v_1.append(v_1)
        result.v_2.append(v_2)

        seconds += TIME_INTERVAL


def main():
    calculate_pendulums_deflection_angles()
    calculate_pendulums_velocities()

    print(f"Natural frequency of first pendulum: {omega_n1:.4f} Hz")
    print(f"Natural frequency of second pendulum: {omega_n2:.4f} Hz")

    y_ticks_coordinates = np.array([phi_1_initial, 0, phi_2_initial])
    y_labels = np.array([f'{round(math.degrees(phi_1_initial), 0)}°', '0°', f'{round(math.degrees(phi_2_initial), 0)}°'])

    plt.figure(figsize=(30, 15))

    plt.subplot(211)
    plt.plot(result.time, result.phi_1)
    plt.plot(result.time, result.phi_2)
    plt.title("\u03C6(t)")
    plt.xlabel("t, s")
    plt.ylabel("\u03C6, radians")
    plt.ylim(-MAX_PHI, MAX_PHI)
    plt.yticks(y_ticks_coordinates, y_labels)

    plt.subplot(212)
    plt.plot(result.time, result.v_1)
    plt.plot(result.time, result.v_2)
    plt.title("V(t)")
    plt.xlabel("t, s")
    plt.ylabel("V, rad/s")

    plt.show()


if __name__ == "__main__":
    main()
