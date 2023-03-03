'''
    Testing the "echoose_break_time" function of 
    the "user_input.py" program

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
    """Typing value and confirming"""

    sleep(2)
    pag.press('tab')
    pag.press('tab')
    pag.press('space')


def calling_echoose_break_time():
    """Calling function and making assert"""

    # Getting value
    return_value = ui.echoose_break_time(10, 20)

    # Value ​​to compare
    example_value = 2

    # Executing assert
    try:
        assert return_value == example_value
    except AssertionError:
        print(f'''
>       assert return_value == example_value
E       assert {return_value} != {example_value}
E        +  where return_value = ui.echoose_break_time(10, 20)

    AssertionError in test_echoose.py''')


def creating_process(number: int):
    """To create threading object"""

    if number == 1:
        typing()
    else:
        calling_echoose_break_time()


class TestEchooseBreakTime(unittest.TestCase):
    """Testing echoose_break_time

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