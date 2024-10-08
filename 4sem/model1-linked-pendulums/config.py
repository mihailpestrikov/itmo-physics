import math

BETA_SCALE = 10 ** -3  # attenuation coefficient scale

TIME_INTERVAL = 0.05  # time interval between calculations in milliseconds

MAX_PHI = math.pi / 2  # max deflection angle of pendulums, equals to 90 degrees

g = 9.8

ACCURACY_LIMIT = 0.001  # when both oscillation angles become less than this value, the oscillations considered damped
