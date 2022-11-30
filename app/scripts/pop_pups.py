'''
    Pop Ups to help interact with the program
    
    @author Nercino Neto
'''

# pip install pysimplegui
import PySimpleGUI as sg

# Setting logo 
from main import *


def error():
    """ Displaying error message """

    sg.popup_auto_close('ENTER ONLY WHOLE NUMBERS ' 
                      + 'AND\nPOSITIVES GREATER THAN ZERO!',
                        image=logo, 
                        title='ERROR')