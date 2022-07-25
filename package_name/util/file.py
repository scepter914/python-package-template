import datetime
import os
from typing import Tuple


def divide_file_path(full_path: str) -> Tuple[str, str, str, str, str]:
    """
    Args:
        full_path (str): './dir/subdir/filename.ext.ext2'
    Return:
        ["./dir/subdir", "filename.ext.ext2", "subdir", "filename" "ext.ext2" ]
    """

    # ./dir/subdir, filename.ext
    dir_name: str = ""
    base_name: str = ""
    dir_name, base_name = os.path.split(full_path)

    # subdir
    subdir_name: str = os.path.basename(os.path.dirname(full_path))

    # filename # .ext
    basename_without_ext: str = ""
    extension: str = ""
    if "." in base_name:
        basename_without_ext, extension = base_name.split(".", 1)
    else:
        basename_without_ext = base_name
        extension = ""

    return dir_name, base_name, subdir_name, basename_without_ext, extension


def format_time(string: str) -> str:
    """
    Format for {Time} macro.
    "{Time}_log" -> "20220401_123456_log"

    Args:
        string (str): string

    Returns:
        str: _description_
    """
    time = "{0:%Y%m%d_%H%M%S}".format(datetime.datetime.now())
    return string.format(Time=time)
