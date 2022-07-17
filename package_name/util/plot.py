import math
from typing import List, Tuple


def get_lim(
    value_list: List[float],
    interval: float,
) -> Tuple[float, float]:
    """Get limit value for set limit function of matplotlib
    Args:
        value_list (List[float]): The value list to plot.
        interval (float): The interval value for grid

    Returns:
        Tuple[float, float]: [max_limit, min_limit] for set_xlim and set_ylim
    """
    min_lim = get_min_lim(min(value_list), interval)
    max_lim = get_max_lim(max(value_list), interval)
    return (max_lim, min_lim)


def get_max_lim(
    max_value: float,
    interval: float,
) -> float:
    """Get max limitation

    Args:
        max_value (float): Max value
        interval (float): Interval value for set_lim for matplotlib

    Returns:
        float: Max value for set_xlim and set_ylim
    """
    decimal_digit: int = -math.ceil(math.log10(interval))
    rounded_value: float = round(max_value, decimal_digit)

    # If rounded_value is truncated, add interval value
    if rounded_value <= max_value:
        rounded_value += interval
    return rounded_value


def get_min_lim(
    min_value: float,
    interval: float,
) -> float:
    """Get min limitation

    Args:
        min_value (float): Min value
        interval (float): Interval value for set_lim for matplotlib

    Returns:
        float: Min value for set_xlim and set_ylim
    """
    decimal_digit: int = -math.ceil(math.log10(interval))
    rounded_value: float = round(min_value, decimal_digit)

    # If rounded_value is truncated, subtract interval value
    if rounded_value >= min_value:
        rounded_value -= interval
    return rounded_value
