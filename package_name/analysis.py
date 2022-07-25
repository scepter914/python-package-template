import os
from typing import Tuple

import numpy as np
from matplotlib import pyplot as plt

from package_name.util.plot import get_grid_interval, get_lim, get_lim_from_multiple_values


class TestData:
    def __init__(
        self,
        t: np.ndarray,
        y1: np.ndarray,
        y2: np.ndarray,
    ) -> None:
        self.t: np.ndarray = t
        self.y1: np.ndarray = y1
        self.y2: np.ndarray = y2


class Analyzer:
    """_summary_
    Analyzer template
    """

    def __init__(
        self,
        figure_directory_path: str,
    ) -> None:
        # make log directory
        os.makedirs(figure_directory_path, exist_ok=True)
        self.figure_directory_path: str = figure_directory_path

    def plot(self, data_: TestData, data_name: str) -> None:
        self._subplot(
            data=data_,
            figure_name=data_name + "_test.png",
            title="Title",
            x_label="time [sec]",
            y_label="position [m]",
            legend_location=(0.05, 0.05),
        )

    def _subplot(
        self,
        data: TestData,
        figure_name: str,
        title: str,
        x_label: str,
        y_label: str,
        legend_location: Tuple[float],
    ) -> None:
        # setting figure
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_title(title, fontsize=30)
        ax.set_xlabel(x_label, fontsize=20)
        ax.set_ylabel(y_label, fontsize=20)

        # set data
        data_x: np.ndarray = data.t
        plot_size: float = 150.0 / len(data_x)

        # plot
        ax.scatter(data_x, data.y1, color="red", s=plot_size, label="y1")
        ax.scatter(data_x, data.y2, color="blue", s=plot_size, label="y2")
        # ax.plot(data.t, data.y1, color="red", label="sin")
        # ax.plot(data.t, data.y2, color="blue", label="cos")

        # setting legend
        ax.legend(loc=legend_location, fontsize=14)

        # setting axis
        x_interval: float = get_grid_interval(data_x)
        y_interval: float = max(
            get_grid_interval(data.y1),
            get_grid_interval(data.y2),
        )

        x_max: float
        x_min: float
        x_max, x_min = get_lim(
            value_list=data.t,
            interval=x_interval,
        )

        y_max: float
        y_min: float
        y_max, y_min = get_lim_from_multiple_values(
            value_lists=[data.y1, data.y2],
            interval_=y_interval,
        )

        ax.set_xticks(np.arange(x_min, x_max, x_interval))
        ax.set_yticks(np.arange(y_min, y_max, y_interval))

        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.grid()

        # save
        file_path = os.path.join(self.figure_directory_path, figure_name)
        # plt.savefig(file_path, bbox_inches="tight", transparent=True)
        plt.savefig(file_path, bbox_inches="tight")
