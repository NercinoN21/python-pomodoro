'''
    Testing the "setting_time" function of the 
    "user_input.py" program

    @author Nercino Neto
'''


# Getting the user input
import app.scripts.user_input as ui

# For the tests(Native)
import unittest

# To run two functions at the same time (Native)
import threading

# For the sleep(Native)
from time import sleep

# pip install pysimplegui
from PySimpleGUI import theme

# pip install pyautogui
import pyautogui as pag


def typing():
    """Typing values and confirming"""

    sleep(2)
    pag.write('50')
    pag.press('tab')

    pag.write('10')
    pag.press('tab')

    pag.write('15')
    pag.press('enter')

def calling_setting_time():
    """Calling function and making assert"""

    # Getting values
    return_values = ui.setting_time()

    # Values ​​to compare
    example_values = {1: '50', 2: '10', 3: '15'}

    # Executing assert
    try:
        assert return_values == example_values
    except:
         print(f'''
>       assert return_values == example_values
E       assert {return_values} != {example_values}
E        +  where return_values = ui.setting_time()

    AssertionError in test_setting_time.py''')

def creating_process(number: int):
    """To create threading object"""

    if number == 1:
        typing()
    else:
        calling_setting_time()


class TestSettingTime(unittest.TestCase):
    """Testing setting_time

    Args:
        unittest (_type_): Test engine
    """

    # Set the theme
    theme('Black')

    def test_creating_and_starting(self):
        """Test creating processes and starting"""

        # For creating_process
        functions = [1, 2]

        # Creating and append processes
        processes = []
        for function in functions:
            processes.append(threading.Thread(target=creating_process, 
                                              args=(function,)))
        
        # Starting processes
        for process in processes:
            process.start()


if __name__ == '__main__':
    unittest.main()