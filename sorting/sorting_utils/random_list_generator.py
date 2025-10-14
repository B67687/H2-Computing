"""Contains random generators for lists of numbers"""

from string import ascii_letters, digits
from random import randrange, sample

# SETTINGS_1D = (length_of_list, lowest_num, highest_num)
SETTINGS_1D = (10, 10, 100)

# SETTINGS_2D = (*SETTINGS_1D, rows)
SETTINGS_2D = (*SETTINGS_1D, 10)
STR_POOL = ascii_letters + digits

# ================== Random list of numbers ==================


# ------------------ Non-unique random list ------------------
def non_unique_1d(settings: tuple = SETTINGS_1D) -> list[int]:
    """Generates a list of non-unique integers"""
    length, low, high = settings
    return [randrange(low, high) for _ in range(length)]


def non_unique_2d(settings: tuple = SETTINGS_2D) -> list[list[int]]:
    """Generates a matrix of non-unique integers"""
    *settings_1d, rows = settings
    return [non_unique_1d(settings_1d) for _ in range(rows)]


# ------------------ Unique random list ------------------
def unique_1d(settings: tuple = SETTINGS_1D) -> list[int]:
    """Generates a list of unique integers"""
    length, low, high = settings
    return sample(range(low, high), length)


def unique_2d(settings: tuple = SETTINGS_2D) -> list[int]:
    """Generates a matrix of unique integers"""
    *settings_1d, rows = settings
    return [unique_1d(settings_1d) for _ in range(rows)]


# ================== Unique random list of strings ==================
def randstr(length: int) -> list[str]:
    """Generates a unique list of random ascii characters"""
    return sample(STR_POOL, length)
