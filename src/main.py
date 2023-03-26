"""
odd/even number checker
Author: Wolf Paulus (https://wolfpaulus.com)
"""


def is_odd(num: int) -> bool:
    """Return True if num is odd, False otherwise."""
    return num % 2 == 1


def is_odd_str(num: str) -> str:
    """Return a string indicating whether num is odd or even."""
    if num.isnumeric():
        return f"{num} is {'odd' if is_odd(int(num)) else 'even'}."
    else:
        return "Please enter a number."
