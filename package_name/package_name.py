import argparse
import logging
import os
from typing import Dict, List

import numpy as np
import toml

from package_name.analysis import PlotData, Plotter
from package_name.util.file import format_time
from package_name.util.logger import configure_logger


def make_test_data() -> List[PlotData]:
    test_data_list: List[PlotData] = []
    t_ = np.linspace(10.0, 16.28, 628)
    test_data_list.append(
        PlotData(
            t=t_,
            y1=np.sin(t_),
            y2=np.cos(t_),
        )
    )

    t_ = np.linspace(9.0, 15.28, 628)
    test_data_list.append(
        PlotData(
            t=t_,
            y1=0.1 * (t_ - 9.0),
            y2=0.1 * (t_ - 9.0) * (t_ - 9.0),
        )
    )

    return test_data_list


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
    log_file_name: str = format_time(config_dict["output"]["log_file_name"])
    figure_directory: str = format_time(config_dict["output"]["figure_directory"])

    log_directory_path: str = os.path.join(root_directory, log_directory)
    figure_directory_path: str = os.path.join(root_directory, figure_directory)
    os.makedirs(figure_directory_path, exist_ok=True)

    logger = logging.getLogger()
    logger = configure_logger(
        log_directory_path=log_directory_path,
        log_file_name=log_file_name,
        console_log_level=logging.INFO,
        file_log_level=logging.DEBUG,
    )

    # test data
    test_data_list = make_test_data()

    # set plotter
    plotters: List[Plotter] = []
    plotters.append(
        Plotter(
            os.path.join(figure_directory_path, "test_1.png"),
            (12, 8),
            30,
            20,
            "title_1",
            (0.05, 0.05),
            14,
            "time[s]",
            "position [m]",
            (lambda data: (data.t, data.y1)),
            None,
            None,
            None,
        )
    )
    plotters.append(
        Plotter(
            os.path.join(figure_directory_path, "test_2.png"),
            (12, 8),
            30,
            20,
            "title_2",
            (0.05, 0.05),
            14,
            "time[s]",
            "position [m]",
            (lambda data: (data.t, data.y2)),
            None,
            None,
            None,
        )
    )

    for plotter in plotters:
        plotter.plot_data(test_data_list[0], "red", "y1")
        plotter.plot_data(test_data_list[1], "blue", "y2")

        plotter.save_figure(test_data_list)

    # test
    logger.warning(log_directory_path)
