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
        values_time = {-1: 'exit'}

    window.close()
    
    return values_time

def echoose_break_time(break_time: int, long_break_time: int) -> int:
    layout = [
        [sg.Image(logo)],
        [sg.Text('Choose an option:')],
        [
            sg.Button('Break Time', key=1), 
            sg.Text(f' {break_time} Minutes')
        ],
        [sg.Text('or')],
        [
            sg.Button('Long Break Time', key=2), 
            sg.Text(f' {long_break_time} Minutes')
        ]
    ]

    # Invoking window
    window = sg.Window('Echoose Break Time', layout)

    # Capturing output
    option = window.read()[0]

    # Checking if the user chose a valid key
    if not option == 1 or option == 2:
        option = -1

    window.close()

    return option