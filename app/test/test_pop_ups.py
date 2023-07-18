"""
    Testing functions of "pop_ups.py"

    @author Nercino Neto
"""


import unittest
from PySimpleGUI import theme
import app.scripts.pop_ups as pop


class TestPopUps(unittest.TestCase):
    theme("Black")

    value = 21

    def test_error(self):
        self.assertIsNone(pop.error())

    def test_end(self):
        self.assertIsNone(pop.end())

    def test_sessions(self):
        self.assertIsNone(pop.sessions(self.value))


if __name__ == "__main__":
    unittest.main()
