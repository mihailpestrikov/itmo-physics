import numpy as np
from matplotlib import pyplot as plt
from math import log
from typing import Callable
from dataclasses import dataclass, field

from model2.config import *


@dataclass
class CalculationResult:
    y: list[float] = field(default_factory=lambda: list())
    x: list[float] = field(default_factory=lambda: list())
    v: list[float] = field(default_factory=lambda: list())
    a: list[float] = field(default_factory=lambda: list())
    t: list[float] = field(default_factory=lambda: list())
    out_of_bounds: bool = False


def plot(name: str, x_label: str, y_label: str, data_x: list[float], data_y: list[float]):
    plt.plot(data_x, data_y, "-")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(name)

def calc_acceleration(u: float, y: float) -> float:
    return (ELECTRON_CHARGE * u) / (ELECTRON_MASS * y * log(R_OUTER / R_INNER))


def calc_y_coordinate(y: float, a: float, v: float) -> float:
    return y + v * TIME + a * TIME ** 2 / 2


def calc_velocity(v: float, a: float) -> float:
    return v + a * TIME


def binary_search(left: float, right: float, comp: Callable) -> float:
    current = 0
    while right - left > (10 ** -6):
        current = (left + right) / 2
        result = comp(current) # проверка вылета из конденсатора

        if result:
            right = current
        else:
            left = current

    return current


def calculate_movement(u: float, final: bool) -> CalculationResult:
    velocity = 0
    y_coordinate = (R_INNER + R_OUTER) / 2
    acceleration = calc_acceleration(u, y_coordinate)
    result = CalculationResult()

    for nano_second in range(1, int(TIME_MAX * 10 ** TIME_SPLIT)):
        y_coordinate = calc_y_coordinate(y_coordinate, acceleration, velocity)
        velocity = calc_velocity(velocity, acceleration)
        acceleration = calc_acceleration(u, y_coordinate)

        if final:
            result.y.append(y_coordinate - (R_INNER + R_OUTER) / 2)
            result.a.append(acceleration)
            result.v.append(velocity)
            result.t.append(nano_second * TIME)

        if not final:
            if y_coordinate < R_INNER or y_coordinate > R_OUTER:
                result.out_of_bounds = True
                return result

    return result


def main():
    def _comp(u: float) -> bool:
        temp_result = calculate_movement(u, False)
        return temp_result.out_of_bounds

    found_u = binary_search(U_START, U_END, _comp)
    result = calculate_movement(found_u, True)
    result.x = list(np.linspace(0, CAPACITOR_LENGTH, len(result.y)))

    plt.figure(figsize=(15, 15))
    plt.subplot(221)
    plot("y(x)", "x, м", "y, м", result.x, result.y)

    plt.subplot(222)
    plot("v(t)", "t, с", "v, м/c", result.t, result.v)

    plt.subplot(223)
    plot("a(t)", "t, с", "a, м/с^2", result.t, result.a)

    plt.subplot(224)
    plot("y(t)", "y, м", "t, с", result.t, result.y)

    plt.show()

    print(f"Final voltage: {round(found_u, 6)} в")
    print(f"Velocity: {round(result.v[-1])}, м/с")
    print("Time:", "%.7f" % TIME_MAX, "с")

if __name__ == "__main__":
    main()
