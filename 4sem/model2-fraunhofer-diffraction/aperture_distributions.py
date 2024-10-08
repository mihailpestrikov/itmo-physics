import numpy as np


def horizontal_linear_aperture_distribution(x, y, slit_width):
    """
    Функция для расчета двумерного амплитудного распределения для линейной апертуры (щели).

    """
    X, Y = np.meshgrid(x, y)

    condition1 = np.abs(X) <= slit_width / 2
    condition2 = np.abs(Y) <= 0.1

    aperture = np.where(condition1 & condition2, 1, 0)

    return aperture


def two_vertical_linear_sides_aperture_distribution(x, y, slit_width):
    """
    Функция для расчета двумерного амплитудного распределения для двух вертикальных щелей.

    """

    def full_condition(x, y):
        condition1 = np.abs(y) <= 2
        condition2 = np.abs(x) <= slit_width / 5

        return condition1 & condition2

    shift = 1

    X, Y = np.meshgrid(x - shift, y)
    first_aperture = np.where(full_condition(X, Y), 1, 0)

    X, Y = np.meshgrid(x + shift, y)
    second_aperture = np.where(full_condition(X, Y), 1, 0)

    combined_aperture = np.maximum(first_aperture, second_aperture)

    return combined_aperture


def circular_aperture_distribution(x, y, radius):
    """
    Функция для расчета двумерного амплитудного распределения для круглой апертуры.

    """

    X, Y = np.meshgrid(x, y)

    aperture = np.where(X**2 + Y**2 <= radius**2, 1, 0)

    return aperture


def square_aperture_distribution(x, y, side_length):
    """
    Функция для расчета двумерного амплитудного распределения для квадратной апертуры.

    """

    X, Y = np.meshgrid(x, y)

    half_side = side_length / 2
    aperture = np.where((np.abs(X) <= half_side) & (np.abs(Y) <= half_side), 1, 0)

    return aperture


def two_square_sides_aperture_distribution(x, y, side_length):
    """
    Функция для расчета двумерного амплитудного распределения для двух
    квадратных апертур, расположенных по бокам.

    """
    def full_condition(x, y):
        condition1 = x < side_length
        condition2 = x > -side_length
        condition3 = y < side_length
        condition4 = y > -side_length

        full_condition = condition1 & condition2 & condition3 & condition4

        return full_condition

    shift = 2 * side_length

    X, Y = np.meshgrid(x - shift, y)
    first_aperture = np.where(full_condition(X, Y), 1, 0)

    X, Y = np.meshgrid(x + shift, y)
    second_aperture = np.where(full_condition(X, Y), 1, 0)

    combined_aperture = np.maximum(first_aperture, second_aperture)

    return combined_aperture


def hollow_square_aperture_distribution(x, y, side_length):
    """
    Функция для расчета двумерного амплитудного распределения для контура квадратной апертуры.

    """

    X, Y = np.meshgrid(x, y)

    condition1 = X < side_length
    condition2 = X > -side_length
    condition3 = Y < side_length
    condition4 = Y > -side_length

    condition5 = X > side_length * 0.8
    condition6 = X < -side_length * 0.8
    condition7 = Y > side_length * 0.8
    condition8 = Y < -side_length * 0.8

    outer_condition = condition1 & condition2 & condition3 & condition4
    inner_condition = condition5 | condition6 | condition7 | condition8

    aperture = np.where(inner_condition & outer_condition, 1, 0)

    return aperture


def two_hollow_square_sides_aperture_distribution(x, y, side_length):
    """
    Функция для расчета двумерного амплитудного распределения для двух
    контуров квадратной апертуры, расположенных по бокам.

    """
    def full_condition(x, y):
        condition1 = x < side_length
        condition2 = x > -side_length
        condition3 = y < side_length
        condition4 = y > -side_length

        condition5 = x > side_length * 0.8
        condition6 = x < -side_length * 0.8
        condition7 = y > side_length * 0.8
        condition8 = y < -side_length * 0.8

        outer_condition = condition1 & condition2 & condition3 & condition4
        inner_condition = condition5 | condition6 | condition7 | condition8

        full_condition = inner_condition & outer_condition

        return full_condition

    shift = 2 * side_length

    X, Y = np.meshgrid(x - shift, y)
    first_aperture = np.where(full_condition(X, Y), 1, 0)

    X, Y = np.meshgrid(x + shift, y)
    second_aperture = np.where(full_condition(X, Y), 1, 0)

    combined_aperture = np.maximum(first_aperture, second_aperture)

    return combined_aperture


def hexagonal_aperture_distribution(x, y, side_length):
    """
    Функция для расчета двумерного амплитудного распределения для шестиугольной апертуры.

    """
    X, Y = np.meshgrid(x, y)

    condition1 = np.abs(Y) <= np.sqrt(3) * side_length / 2
    condition2 = np.abs(X) <= np.sqrt(3) * side_length
    condition3 = np.abs(Y) <= np.sqrt(3) * (side_length - np.abs(X))

    aperture = np.where(condition1 & condition2 & condition3, 1, 0)

    return aperture


def two_hexagonal_sides_aperture_distribution(x, y, side_length):
    """
    Функция для расчета двумерного амплитудного распределения для двух
    шестиугольных апертур, расположенных по бокам.

    """
    def full_condition(x, y):
        condition1 = np.abs(y) <= np.sqrt(3) * side_length / 2
        condition2 = np.abs(x) <= np.sqrt(3) * side_length
        condition3 = np.abs(y) <= np.sqrt(3) * (side_length - np.abs(x))

        full_condition = condition1 & condition2 & condition3

        return full_condition

    shift = 2 * side_length

    X, Y = np.meshgrid(x - shift, y)
    first_aperture = np.where(full_condition(X, Y), 1, 0)

    X, Y = np.meshgrid(x + shift, y)
    second_aperture = np.where(full_condition(X, Y), 1, 0)

    combined_aperture = np.maximum(first_aperture, second_aperture)

    return combined_aperture


def hollow_hexagonal_aperture_distribution(x, y, side_length):
    """
    Функция для расчета двумерного амплитудного распределения для контура шестиугольной апертуры.

    """
    X, Y = np.meshgrid(x, y)

    # Определяем условия для шестиугольника
    condition1 = np.abs(Y) <= np.sqrt(3) * side_length / 2
    condition2 = np.abs(X) <= np.sqrt(3) * side_length
    condition3 = np.abs(Y) <= np.sqrt(3) * (side_length - np.abs(X))

    condition4 = np.abs(Y) >= np.sqrt(3) * side_length / 2 * 0.8
    condition5 = np.abs(X) >= np.sqrt(3) * side_length * 0.8
    condition6 = np.abs(Y) >= np.sqrt(3) * (side_length - np.abs(X) * 1.2) * 0.8

    outer_condition = condition1 & condition2 & condition3
    inner_condition = condition4 | condition5 | condition6

    aperture = np.where(outer_condition & inner_condition, 1, 0)

    return aperture


def two_hollow_hexagonal_sides_aperture_distribution(x, y, side_length):
    """
    Функция для расчета двумерного амплитудного распределения для двух
    контуров шестиугольных апертур, расположенных по бокам.

    """
    def full_condition(x, y):
        condition1 = np.abs(y) <= np.sqrt(3) * side_length / 2
        condition2 = np.abs(x) <= np.sqrt(3) * side_length
        condition3 = np.abs(y) <= np.sqrt(3) * (side_length - np.abs(x))

        condition4 = np.abs(y) >= np.sqrt(3) * side_length / 2 * 0.8
        condition5 = np.abs(x) >= np.sqrt(3) * side_length * 0.8
        condition6 = np.abs(y) >= np.sqrt(3) * (side_length - np.abs(x) * 1.2) * 0.8

        outer_condition = condition1 & condition2 & condition3
        inner_condition = condition4 | condition5 | condition6

        full_condition = outer_condition & inner_condition

        return full_condition

    shift = 2 * side_length

    X, Y = np.meshgrid(x - shift, y)
    first_aperture = np.where(full_condition(X, Y), 1, 0)

    X, Y = np.meshgrid(x + shift, y)
    second_aperture = np.where(full_condition(X, Y), 1, 0)

    combined_aperture = np.maximum(first_aperture, second_aperture)

    return combined_aperture


def two_hollow_hexagonal_inside_aperture_distribution(x, y, side_length):
    """
    Функция для расчета двумерного амплитудного распределения для двух
    контуров шестиугольных апертур, расположенных одна внутри другой.

    """
    X, Y = np.meshgrid(x, y)

    condition1 = np.abs(Y) <= np.sqrt(3) * side_length / 2
    condition2 = np.abs(X) <= np.sqrt(3) * side_length
    condition3 = np.abs(Y) <= np.sqrt(3) * (side_length - np.abs(X))

    condition4 = np.abs(Y) >= np.sqrt(3) * side_length / 2 * 0.8
    condition5 = np.abs(X) >= np.sqrt(3) * side_length * 0.8
    condition6 = np.abs(Y) >= np.sqrt(3) * (side_length - np.abs(X) * 1.2) * 0.8

    outer_condition = condition1 & condition2 & condition3
    inner_condition = condition4 | condition5 | condition6

    first_full_condition = outer_condition & inner_condition

    condition1 = np.abs(Y) <= np.sqrt(3) * side_length / 2 * 0.5
    condition2 = np.abs(X) <= np.sqrt(3) * side_length * 0.5
    condition3 = np.abs(Y) <= np.sqrt(3) * (side_length - np.abs(X) * 1.8) * 0.5

    condition4 = np.abs(Y) >= np.sqrt(3) * side_length / 2 * 0.4
    condition5 = np.abs(X) >= np.sqrt(3) * side_length * 0.4
    condition6 = np.abs(Y) >= np.sqrt(3) * (side_length - np.abs(X) * 2.1) * 0.4

    outer_condition = condition1 & condition2 & condition3
    inner_condition = condition4 | condition5 | condition6

    second_full_condition = outer_condition & inner_condition

    full_condition = first_full_condition | second_full_condition

    aperture = np.where(full_condition, 1, 0)

    return aperture
