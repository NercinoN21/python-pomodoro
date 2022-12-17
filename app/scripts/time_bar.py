'''
    Everything related to the time bar window

    @author Nercino Neto
'''


# Native
import time

# pip install pysimplegui
import PySimpleGUI as sg

# I recommend pip install playsound==1.2.2
from playsound import playsound 

# Setting logo and alarm
logo = "app/media/logo.png"
alarm = "app/media/alarm.mp3"


def creat_time_bar(max_seconds: int, title: str) -> sg.Window:
    """Creating time bar window structure

    Args:
        max_seconds (int): Execution time
        title (str): Text that will be in 
                     the header of the page

    Returns:
        sg.Window: To update bar value and close window
    """

    # Window structure
    layout = [
        [sg.Image(logo)],
        [sg.Text('In progress...')],
        [sg.ProgressBar(max_value=max_seconds, 
                        orientation='h', 
                        size=(23, 30), 
                        key='_loading_', 
                        style='classic')]
    ]

    # Invoking window
    window = sg.Window(title, layout)

    return window

def loop_time_bar(window: sg.Window, max_seconds: int) -> bool:
    """Responsible for updating the time bar

    Args:
        window (sg.Window): To update bar value and close window
        max_seconds (int): Execution time

    Returns:
        bool: If the time is completed, it returns true, otherwise false
    """

    for second in range(max_seconds):
        # Capturing output
        event = window.read(timeout=100)[0]

        # If press the "x" close the window
        if event == sg.WIN_CLOSED:
            return False

        # Waiting a second considering processing time
        time.sleep(0.89)

        # updating the bar
        window['_loading_'].UpdateBar(second+1)

    return True

def run_time_bar(max_seconds: int, title: str):
    """General operation of the time bar

       Initializing the window, ringing the alarm when 
       the time is up(or not) and closing the window

    Args:
        max_seconds (int): Execution time
        title (str): Text that will be in 
                     the header of the page
    """

    # Generating time bar
    windons = creat_time_bar(max_seconds, title)

    # If: 
    #   The user does not interrupt the window
    # Else:
    #   The user interrupts the window
    if loop_time_bar(windons, max_seconds):
        playsound(alarm)
        windons.close()
    else:
        windons.close()