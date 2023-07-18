"""
    Testing the "setting_time" function of the
    "user_input.py" program

    @author Nercino Neto
"""


import unittest
import threading
from time import sleep
from PySimpleGUI import theme
import pyautogui as pag
import app.scripts.user_input as ui


def typing():
    sleep(2)
    pag.write("50")
    pag.press("tab")

    pag.write("10")
    pag.press("tab")

    pag.write("15")
    pag.press("enter")


def calling_setting_time():
    return_values = ui.setting_time()

    example_values = {1: "50", 2: "10", 3: "15"}

    try:
        assert return_values == example_values
    except AssertionError:
        print(
            f"""
>       assert return_values == example_values
E       assert {return_values} != {example_values}
E        +  where return_values = ui.setting_time()

    AssertionError in test_setting_time.py"""
        )


def creating_process(number: int):
    if number == 1:
        typing()
    else:
        calling_setting_time()


class TestSettingTime(unittest.TestCase):
    theme("Black")

    def test_creating_and_starting(self):
        functions = [1, 2]
        processes = []

        for function in functions:
            processes.append(
                threading.Thread(
                    target=creating_process,
                    args=(function,)
                )
            )

        for process in processes:
            process.start()


if __name__ == "__main__":
    unittest.main()
