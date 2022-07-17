import os

import numpy as np
from matplotlib import pyplot as plt

from package_name.util.plot import get_lim


class TestData:
    def __init__(self) -> None:
        self.t = np.linspace(10.0, 16.28, 628)
        self.y1 = np.sin(self.t)
        self.y2 = np.cos(self.t)


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

    def plot(self, data: TestData) -> None:
        # setting figure
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_title("Title", fontsize=30)
        ax.set_xlabel("time [sec]", fontsize=20)
        ax.set_ylabel("position [m]", fontsize=20)

        # plot
        ax.scatter(
            data.t,
            data.y1,
            color="red",
            s=1.0,
            label="sin",
        )
        ax.scatter(
            data.t,
            data.y2,
            color="blue",
            s=1.0,
            label="cos",
        )
        # ax.plot(data.t, data.y1, color="red", label="sin")
        # ax.plot(data.t, data.y2, color="blue", label="cos")

        # setting legend
        ax.legend(loc=(0.05, 0.05), fontsize=14)

        # setting axis
        x_interval: float = 1.0
        y_interval: float = 0.1

        x_max: float
        x_min: float
        y_max: float
        y_min: float

        x_max, x_min = get_lim(
            value_list=data.t,
            interval=x_interval,
        )
        y_max, y_min = get_lim(
            value_list=data.y1,
            interval=y_interval,
        )

        ax.set_xticks(np.arange(x_min, x_max, x_interval))
        ax.set_yticks(np.arange(y_min, y_max, y_interval))

        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.grid()

        # save
        file_path = os.path.join(self.figure_directory_path, "test.png")
        # plt.savefig(file_path, bbox_inches="tight", transparent=True)
        plt.savefig(file_path, bbox_inches="tight")
