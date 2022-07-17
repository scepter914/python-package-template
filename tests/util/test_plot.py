import unittest
from typing import List

from package_name.util.plot import get_max_lim, get_min_lim


class TestPlot(unittest.TestCase):
    def test_get_max_lim(self):
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
            self.assertAlmostEqual(get_max_lim(test_case[0], test_case[1]), test_case[2])

    def test_get_min_lim(self):
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
            self.assertAlmostEqual(get_min_lim(test_case[0], test_case[1]), test_case[2])


if __name__ == "__main__":
    unittest.main()
