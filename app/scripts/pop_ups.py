'''
    Pop Ups to help interact with the program
    
    @author Nercino Neto
'''

# pip install pysimplegui
import PySimpleGUI as sg

# Setting logo 
logo = "app/media/logo.png"


def error():
    """ Displaying error message """

    sg.popup_auto_close('ENTER ONLY WHOLE NUMBERS ' 
                      + 'AND\nPOSITIVES GREATER THAN ZERO!',
                        image=logo, 
                        title='ERROR')

def sessions(amount_of_sessions: int):
    """Display number of sessions

    Args:
        amount_of_sessions (int): Represents the number 
                                  of sessions held
    """

    sg.popup_auto_close('Total number of sessions: '
                      + f'{amount_of_sessions}', 
                        image=logo, 
                        title='Sessions')

def end():
    """ Displaying end message """

    sg.popup_auto_close("SEE YOU LATER!", 
                        image=logo, 
                        title='Bye')