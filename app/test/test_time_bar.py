'''
    Testing the time bar

    @author Nercino Neto
'''


# Native
import sys
import os

# Getting the time bar
import app.scripts.time_bar as tb

# For the tests(Native)
import unittest

# pip install pysimplegui
from PySimpleGUI import theme
  
  
class TestPomodoro(unittest.TestCase):
    """Checking complete functioning of the time bar
    
    Args:
        unittest (_type_): Test engine
    """

    def test_GUI(self):
        """Testing GUI time bar"""

        # Set the theme
        theme('Black')
         
        self.assertIsNone(tb.run_time_bar(max_seconds=3,
                                          title='TEST...'))


if __name__ == '__main__':
    unittest.main()