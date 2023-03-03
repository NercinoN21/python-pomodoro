'''
    Testing functions of "pop_ups.py"

    @author Nercino Neto
'''


# Getting the pop ups
import app.scripts.pop_ups as pop

# For the tests(Native)
import unittest

# pip install pysimplegui
# To set the theme
from PySimpleGUI import theme


class TestPopUps(unittest.TestCase): 
    """Test Class for Pop Ups

    Args:
        unittest (_type_): Test engine
    """

    # Set the theme
    theme('Black') 

    # Value for sessions
    value = 21 

    def test_error(self): 
        """Checking error() functionality"""

        self.assertIsNone(pop.error())

    def test_end(self): 
        """Checking end() functionality"""

        self.assertIsNone(pop.end())

    def test_sessions(self): 
        """Checking sessions() functionality"""

        self.assertIsNone(pop.sessions(self.value))


if __name__ == '__main__': 
    unittest.main()