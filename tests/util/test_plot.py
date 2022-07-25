import unittest
from typing import List

from package_name.util.plot import _get_grid_interval, _get_max_lim, _get_min_lim


class TestPlot(unittest.TestCase):
    def test_get_max_lim(self) -> None:
        # test_max_value, test_interval, answer
        test_cases: List[List[float, float, float]] = [
            [-3.12, 0.5, -3.0],
            [-0.626, 0.01, -0.62],
            [-0.626, 0.1, -0.6],
            [-0.626, 0.5, -0.5],
            [-0.626, 1.0, -0.0],
            [1.126, 0.01, 1.13],
            [1.126, 0.1, 1.2],
            [1.126, 0.5, 1.5],
            [1.126, 1.0, 2.0],
            [1.30, 0.1, 1.4],
            [2.124, 0.01, 2.13],
            [2.124, 0.1, 2.2],
            [2.124, 0.5, 2.5],
            [2.124, 1.0, 3.0],
        ]
        for test_case in test_cases:
            self.assertAlmostEqual(_get_max_lim(test_case[0], test_case[1]), test_case[2])

    def test_get_min_lim(self) -> None:
        # test_min_value, test_interval, answer
        test_cases: List[List[float, float, float]] = [
            [-3.12, 0.5, -3.5],
            [-0.626, 0.01, -0.63],
            [-0.626, 0.1, -0.7],
            [-0.626, 0.5, -1.0],
            [-0.626, 1.0, -1.0],
            [1.626, 0.01, 1.62],
            [1.626, 0.1, 1.6],
            [1.626, 0.5, 1.5],
            [1.626, 1.0, 1.0],
            [1.30, 0.1, 1.2],
            [2.124, 0.01, 2.12],
            [2.124, 0.1, 2.1],
            [2.124, 0.5, 2.0],
            [2.124, 1.0, 2.0],
        ]
        for test_case in test_cases:
            self.assertAlmostEqual(_get_min_lim(test_case[0], test_case[1]), test_case[2])

    def test_get_interval(self) -> None:
        # test_range, answer
        test_cases: List[List[float, float]] = [
            [0.9, 0.05],
            [3.0, 0.2],
            [9.9, 0.5],
            [11.0, 1.0],
            [36.0, 2.0],
            [68.0, 5.0],
        ]
        for test_case in test_cases:
            self.assertAlmostEqual(_get_grid_interval(test_case[0]), test_case[1])


if __name__ == "__main__":
    unittest.main()
