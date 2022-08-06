from typing import Callable, List, Optional, Tuple

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from package_name.util.plot import (get_grid_interval_from_multiple_values,
                                    get_lim_from_multiple_values)


class PlotData:
    def __init__(
        self,
        t: np.ndarray,
        y1: np.ndarray,
        y2: np.ndarray,
    ) -> None:
        self.t: np.ndarray = t
        self.y1: np.ndarray = y1
        self.y2: np.ndarray = y2


class Plotter:
    """_summary_
    Analyzer template
    """

    def __init__(
        self,
        file_path: str,
        figure_size: Tuple[int],
        title_font_size: int,
        label_font_size: int,
        title: str,
        legend_location: Tuple[float],
        legend_font_size: int,
        x_label: str,
        y_label: str,
        xy_pair_lambda: Callable,
        x_grid_config: Optional[Tuple[float]],
        y_grid_config: Optional[Tuple[float]],
        plot_size: Optional[float],
    ) -> None:
        self.file_path: str = file_path
        self.figure_size: Tuple[int] = figure_size
        self.title_font_size: int = title_font_size
        self.label_font_size: int = label_font_size
        self.title: str = title
        self.legend_location: Tuple[float] = legend_location
        self.legend_font_size: int = legend_font_size
        self.x_label: str = x_label
        self.y_label: str = y_label
        self.xy_pair_lambda: Callable = xy_pair_lambda
        self.x_grid_config: Optional[Tuple[float]] = x_grid_config
        self.y_grid_config: Optional[Tuple[float]] = y_grid_config
        self.plot_size: float = self._set_plot_size(plot_size)
        self._set_figure_config()

    def plot_data(
        self,
        data: PlotData,
        color_: str,
        label_: str,
    ):
        # plot
        x_, y_ = self.xy_pair_lambda(data)
        self.ax.scatter(x_, y_, color=color_, s=self.plot_size, label=label_)
        # self.ax.plot(x_, y_, color=color_, s=self.plot_size, label=label_)

    def save_figure(self, data_lists: List[PlotData]):
        self._set_grid_size(data_lists)
        self.ax.legend(loc=self.legend_location, fontsize=14)

        self.fig.savefig(self.file_path, bbox_inches="tight")
        # plt.savefig(self.file_path, bbox_inches="tight")
        # plt.savefig(self.file_path, bbox_inches="tight", transparent=True)

    def _set_figure_config(self) -> None:
        # self.fig, self.ax = plt.subplots(figsize=self.figure_size)
        # self.fig: Figure = plt.figure(self.figure_number, figsize=self.figure_size)
        self.fig: Figure = plt.figure(figsize=self.figure_size)
        self.ax: Axes = self.fig.add_subplot(1, 1, 1)
        self.ax.set_title(self.title, fontsize=self.title_font_size)
        self.ax.set_xlabel(self.x_label, fontsize=self.label_font_size)
        self.ax.set_ylabel(self.y_label, fontsize=self.label_font_size)

    def _set_plot_size(self, plot_size: Optional[float]) -> float:
        if plot_size is None:
            return self.figure_size[0] / 6.0
        else:
            return plot_size

    def _set_grid_size(self, data_lists: List[PlotData]):
        x_value_lists, y_value_lists = self._get_xy_lists(data_lists)
        x_min, x_max, x_interval = self._get_grid_config(self.x_grid_config, x_value_lists)
        y_min, y_max, y_interval = self._get_grid_config(self.y_grid_config, y_value_lists)

        self.ax.set_xticks(np.arange(x_min, x_max, x_interval))
        self.ax.set_yticks(np.arange(y_min, y_max, y_interval))
        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)
        self.ax.grid()

    def _get_xy_lists(self, data_lists: List[PlotData]):
        x_lists: List[float] = []
        y_lists: List[float] = []
        for data_list in data_lists:
            x_, y_ = self.xy_pair_lambda(data_list)
            x_lists.append(x_)
            y_lists.append(y_)
        return x_lists, y_lists

    @staticmethod
    def _get_grid_config(
        grid_config: Optional[Tuple[float]],
        values_lists: List[List[float]],
    ) -> Tuple[float]:
        if grid_config is None:
            interval_: float = get_grid_interval_from_multiple_values(values_lists)
            max_, min_ = get_lim_from_multiple_values(
                value_lists=values_lists,
                interval=interval_,
            )
            return min_, max_, interval_
        else:
            return grid_config
