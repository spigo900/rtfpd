"""
Dice rolling and calculations for Past Due.
"""
import random
from typing import Sequence


SIDES = 10


def roll_die(*, explodes: bool = True) -> int:
    """
    Roll a die, optionally exploding when we roll a 10.
    """
    result = roll = random.randint(1, SIDES + 1)
    if explodes:
        while roll == SIDES:
            roll = random.randint(1, SIDES + 1)
            result += roll
    return result


def roll_dice(n_roll: int, *, explodes: bool) -> Sequence[int]:
    """
    Roll the given number of dice, returning the rolls.
    """
    return [roll_die(explodes=explodes) for _ in range(n_roll)]


def calculate_value(rolls: Sequence[int], n_keep: int) -> int:
    """
    Calculate the value of a dice roll, given the rolls and number to keep.
    """
    in_order = sorted(rolls)
    return sum(in_order[-n_keep:])