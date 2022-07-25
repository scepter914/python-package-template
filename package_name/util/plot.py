import math
from typing import List, Tuple


def get_lim(
    value_list: List[float],
    interval: float,
) -> Tuple[float, float]:
    """Get limit value for set_lim function of matplotlib
    Args:
        value_list (List[float]): The value list to plot.
        interval (float): The interval value for grid

    Returns:
        Tuple[float, float]: [max_limit, min_limit] for set_xlim and set_ylim
    """
    min_lim = _get_min_lim(min(value_list), interval)
    max_lim = _get_max_lim(max(value_list), interval)
    return (max_lim, min_lim)


def get_lim_from_multiple_values(
    value_lists: List[List[float]],
    interval_: float,
) -> Tuple[float, float]:
    """Get limit value from multiple value lists for set_lim function of matplotlib
    Args:
        value_list (List[List[float]]): The value lists to plot.
        interval (float): The interval value for grid

    Returns:
        Tuple[float, float]: [max_limit, min_limit] for set_xlim and set_ylim
    """

    max_lim_list: List[float] = []
    min_lim_list: List[float] = []
    max_lim: float
    min_lim: float

    for value_list_ in value_lists:
        max_lim, min_lim = get_lim(value_list=value_list_, interval=interval_)
        max_lim_list.append(max_lim)
        min_lim_list.append(min_lim)

    return max(max_lim_list), min(min_lim_list)


def _get_max_lim(
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


def _get_min_lim(
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


def get_grid_interval(value_list: List[float]) -> float:
    """Get grid interval value for plot

    Args:
        value_list (List[float]): Plot value list

    Returns:
        float: Grid interval value for plot
    """
    value_range: float = max(value_list) - min(value_list)
    interval_value = _get_grid_interval(value_range)
    return interval_value


def _get_grid_interval(value_range: float) -> float:
    """Get grid interval value for plot

    Args:
        value_range (float): Range for plot value

    Returns:
        float: Grid interval value for plot
    """

    digit_number: int = math.floor(math.log10(value_range))
    first_digit: float = value_range / math.pow(10.0, digit_number)
    if first_digit <= 1:
        RuntimeError("Error in digit_number")
    elif first_digit <= 2:
        return 0.1 * math.pow(10, digit_number)
    elif first_digit <= 5:
        return 0.2 * math.pow(10, digit_number)
    else:
        return 0.5 * math.pow(10, digit_number)
