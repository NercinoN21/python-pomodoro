"""
    Pages that will have user input

    @author Nercino Neto
"""


import PySimpleGUI as sg


logo = "app/media/logo.png"


def setting_time() -> dict:
    """Getting user data"""

    layout = [
        [sg.Image(logo)],
        [sg.Text("Enter the time in minutes:")],
        [
            sg.Text("Study ", size=(13, 1)),
            sg.InputText(size=(10, 1))
        ],
        [
            sg.Text("Break Time", size=(13, 1)),
            sg.InputText(size=(10, 1))
        ],
        [
            sg.Text("Long Break Time ", size=(13, 1)),
            sg.InputText(size=(10, 1))
        ],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window("Setting Timer", layout)
    submit, values_time = window.read()

    if submit != "Submit":
        values_time = {-1: "exit"}
    window.close()

    return values_time


def echoose_break_time(break_time: int, long_break_time: int) -> int:
    """Choosing break"""

    layout = [
        [sg.Image(logo)],
        [sg.Text("Choose an option:")],
        [
            sg.Button("Break Time", key=1),
            sg.Text(f" {break_time} Minutes")
        ],
        [sg.Text("or")],
        [
            sg.Button("Long Break Time", key=2),
            sg.Text(f" {long_break_time} Minutes")
        ],
    ]

    window = sg.Window("Echoose Break Time", layout)
    option = window.read()[0]
    window.close()

    return option
