"""
    Testing the time bar

    @author Nercino Neto
"""


import unittest
from PySimpleGUI import theme
import app.scripts.time_bar as tb


class TestPomodoro(unittest.TestCase):
    def test_GUI(self):
        theme("Black")

        self.assertIsNone(tb.run_time_bar(
            max_seconds=3,
            title="TEST..."
        ))


if __name__ == "__main__":
    unittest.main()
