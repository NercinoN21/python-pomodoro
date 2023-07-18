"""
    Everything related to the time bar window

    @author Nercino Neto
"""


import time
import PySimpleGUI as sg
from playsound import playsound


logo = "app/media/logo.png"
alarm = "app/media/alarm.mp3"


def creat_time_bar(max_seconds: int, title: str) -> sg.Window:
    """Creating time bar window structure"""

    layout = [
        [sg.Image(logo)],
        [sg.Text("In progress...")],
        [
            sg.ProgressBar(
                max_value=max_seconds,
                orientation="h",
                size=(23, 30),
                key="_loading_",
                style="classic",
            )
        ],
    ]

    window = sg.Window(title, layout)

    return window


def loop_time_bar(window: sg.Window, max_seconds: int) -> bool:
    """Responsible for updating the time bar"""

    for second in range(max_seconds):
        event = window.read(timeout=100)[0]

        if event == sg.WIN_CLOSED:
            return False

        # Waiting a second considering processing time
        time.sleep(0.89)

        window["_loading_"].UpdateBar(second + 1)

    return True


def run_time_bar(max_seconds: int, title: str) -> None:
    """General operation of the time bar"""

    windons = creat_time_bar(max_seconds, title)

    if loop_time_bar(windons, max_seconds):
        playsound(alarm)
        windons.close()
    else:
        windons.close()
