"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(num_layers: int) -> int:
    """Calculate the bake time remaining.

    :param num_layers: int - number of layers.
    :return: int - how many minutes you spent preparing the lasagna.

    Function that takes number of layers you added to the lasagna as a parameter and
    returns how many minutes you spent preparing the lasagna, assuming each layer
    takes you 2 minutes to prepare.
    """

    return num_layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(num_layers: int, actual_minutes_in_oven: int) -> int:
    """Calculate the bake time remaining.

    :param num_layers: int - number of layers.
    :param actual_minutes_in_oven: int -  number of minutes the lasagna has been in the oven.
    :return: int - how many minutes you've worked on cooking the lasagna.

    Function that that takes two parameters: the first parameter is the number of layers you
    added to the lasagna, and the second parameter is the number of minutes the lasagna has
    been in the oven. The function should return how many minutes you've worked on cooking
    the lasagna.
    """

    return preparation_time_in_minutes(num_layers) + actual_minutes_in_oven
