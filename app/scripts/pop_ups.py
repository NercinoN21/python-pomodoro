"""
    Pop Ups to help interact with the program

    @author Nercino Neto
"""


import PySimpleGUI as sg


logo = "app/media/logo.png"


def error() -> None:
    """Displaying error message"""

    sg.popup_auto_close(
        "ENTER ONLY WHOLE NUMBERS AND\nPOSITIVES GREATER THAN ZERO!",
        image=logo,
        title="ERROR",
    )


def sessions(amount_of_sessions: int) -> None:
    """Display number of sessions"""

    sg.popup_auto_close(
        f"Total number of sessions: {amount_of_sessions}",
        image=logo,
        title="Sessions",
    )


def end() -> None:
    """Displaying end message"""

    sg.popup_auto_close("SEE YOU LATER!", image=logo, title="Bye")
