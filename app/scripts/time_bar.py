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


def run_time_bar(max_seconds: int, title: str):
    """General operation of the time bar

    Args:
        max_seconds (int): Execution time
        title (str): Text that will be in 
                     the header of the page
    """

    layout = [[sg.Image(logo)],
              [sg.Text('In progress...')],
              [sg.ProgressBar(max_value=max_seconds, orientation='h', 
                    size=(23, 30), key='_loading_', style='classic')]
    ]

    # Invoking window
    window = sg.Window(title, layout)

    # Window to update
    refresh_window = window['_loading_']

    current_value = 0
    while True:
        # Capturing output
        event = window.read(timeout=100)[0]
    
        # If press the "x" close the window
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            break
        else:
            current_value+=1

            # Ring the alarm and close the window
            if current_value > max_seconds:
                playsound(alarm)
                window.close()
                break
            
            # Waiting 1 second and updating the bar
            time.sleep(1)
            refresh_window.UpdateBar(current_value)