import random

# Total number of significant digits in result
PRECISION = 5


def read_sensor():
    return 20 + int(2000 * (random.random() - 0.5)) / 1000


def get_raw_temp():
    val = read_sensor()
    return val  # f"{val:.{PRECISION}}"
