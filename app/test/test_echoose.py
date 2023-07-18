"""
    Testing the "echoose_break_time" function of
    the "user_input.py" program

    @author Nercino Neto
"""


import unittest
import threading
from PySimpleGUI import theme
from time import sleep
import pyautogui as pag
import app.scripts.user_input as ui


def typing():
    sleep(2)
    pag.press("tab")
    pag.press("tab")
    pag.press("space")


def calling_echoose_break_time():
    return_value = ui.echoose_break_time(10, 20)
    example_value = 2

    try:
        assert return_value == example_value
    except AssertionError:
        print(
            f"""
>       assert return_value == example_value
E       assert {return_value} != {example_value}
E        +  where return_value = ui.echoose_break_time(10, 20)

    AssertionError in test_echoose.py"""
        )


def creating_process(number: int):
    if number == 1:
        typing()
    else:
        calling_echoose_break_time()


class TestEchooseBreakTime(unittest.TestCase):
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
