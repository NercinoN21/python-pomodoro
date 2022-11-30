'''
    Pages that will have user input

    @author Nercino Neto
'''


# pip install pysimplegui
import PySimpleGUI as sg

# Setting logo
from main import *


def setting_time() -> dict:
    """Getting user data

    Returns:
        dict: Dictionary numbered from 1 to 3 with the 
              values entered if the user clicks on "Submit", 
              and if he doesn't click on "Submit": 
              return {-1: 'exit'}
    """
    
    layout = [
        [sg.Image(logo)],
        [sg.Text('Enter the time in minutes:')],
        [
            sg.Text('Study ', size=(13, 1)), 
            sg.InputText(size=(10, 1))
        ],
        [
            sg.Text('Break Time', size=(13, 1)), 
            sg.InputText(size=(10, 1))
        ],
        [
            sg.Text('Long Break Time ', size=(13, 1)), 
            sg.InputText(size=(10, 1))
        ],
        [sg.Submit(), sg.Cancel()]
    ]

    # Invoking window
    window = sg.Window('Setting Timer', layout)

    # Capturing outputs
    submit, values_time = window.read()

    # Checking if the user has submitted the values
    if submit != 'Submit':
        return {-1: 'exit'}

    window.close()
    
    return values_time