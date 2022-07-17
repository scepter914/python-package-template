import pprint
from enum import Enum
from typing import Optional


def format_class_for_log(
    object: object,
    abbreviation: Optional[int] = None,
) -> str:
    """[summary]
    Convert class object to str to save log
    Args:
        object (object): Class object which you want to convert for str
        abbreviation (Optional[int]): If len(list_object) > abbreviation,
                                      then abbreviate the result.
    Returns:
        str: str converted from class object
    Note:
        Reference is below.
        https://stackoverflow.com/questions/1036409/recursively-convert-python-object-graph-to-dictionary
    """
    return format_dict_for_log(class_to_dict(object, abbreviation))


def class_to_dict(
    object: object,
    abbreviation: Optional[int] = None,
    class_key: Optional[str] = None,
) -> dict:
    """[summary]
    Convert class object to dict
    Args:
        object (object): Class object which you want to convert to dict
        abbreviation (Optional[int]): If len(list_object) > abbreviation,
                                      then abbreviate the result
        class_key (Optional[str]): class key for dict
    Returns:
        dict: Dict converted from class object
    Note:
        Reference is below.
        https://stackoverflow.com/questions/1036409/recursively-convert-python-object-graph-to-dictionary
    """

    if isinstance(object, dict):
        data = {}
        for (k, v) in object.items():
            data[k] = class_to_dict(v, abbreviation, class_key)
        return data
    elif isinstance(object, Enum):
        return str(object)  # type: ignore
    elif hasattr(object, "_ast"):
        return class_to_dict(object._ast(), abbreviation)  # type: ignore
    elif hasattr(object, "__iter__") and not isinstance(object, str):
        if abbreviation and len(object) > abbreviation:  # type: ignore
            return f" --- length of element {len(object)} ---,"  # type: ignore
        return [class_to_dict(v, abbreviation, class_key) for v in object]  # type: ignore
    elif hasattr(object, "__dict__"):
        data = dict(
            [
                (key, class_to_dict(value, abbreviation, class_key))
                for key, value in object.__dict__.items()
                if not callable(value) and not key.startswith("_")
            ]
        )
        if class_key is not None and hasattr(object, "__class__"):
            data[class_key] = object.__class__.__name__  # type: ignore
        return data
    else:
        return object  # type: ignore


def format_dict_for_log(
    dict: dict,
) -> str:
    """
    Format dict class to str for logger
    Args:
        dict (dict): dict which you want to format for logger
    Returns:
        (str) formatted str
    """
    formatted_str: str = (
        "\n" + pprint.pformat(dict, indent=1, width=120, depth=None, compact=True) + "\n"
    )
    return formatted_str
