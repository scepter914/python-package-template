import argparse
import logging
import os
from typing import Dict

import toml

from package_name.analysis import Analyzer, TestData
from package_name.util.file import format_time
from package_name.util.logger import configure_logger

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="perception analyzer")
    parser.add_argument(
        "-c", "--config", default="config/config.toml", type=str, help="config file"
    )
    args = parser.parse_args()

    with open(args.config) as f:
        config_dict: Dict[str, str] = toml.load(f)

    root_directory: str = format_time(config_dict["output"]["root_directory"])
    log_directory: str = format_time(config_dict["output"]["log_directory"])
    log_directory_path: str = os.path.join(root_directory, log_directory)
    log_file_name: str = format_time(config_dict["output"]["log_file_name"])
    figure_directory: str = format_time(config_dict["output"]["figure_directory"])
    figure_directory_path: str = os.path.join(root_directory, figure_directory)

    logger = logging.getLogger()
    logger = configure_logger(
        log_directory_path=log_directory_path,
        log_file_name=log_file_name,
        console_log_level=logging.INFO,
        file_log_level=logging.DEBUG,
    )

    # analyzer
    analyzer = Analyzer(figure_directory_path=figure_directory_path)
    test_data = TestData()
    analyzer.plot(test_data)

    # test
    logger.warning(log_directory_path)
