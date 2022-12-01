'''
    Responsible for run the study time, 
    break and final message

    @author Nercino Neto
'''


# Importing functions needed to create the Pomodoro
from user_input import *
from pop_pups import *
from time_bar import *
from time_bar_data import TimeData


def pomodoro(data: TimeData):

    # Setting time in seconds
    sec_study, sec_break, sec_long_break = data.date_in_seconds()

    number_sessions = 0
    while True:
        # Starting study time
        run_time_bar(sec_study, title='Studying...')

        # Storing user option
        option = echoose_break_time(data.break_time, 
                                    data.long_break_time)
        # Checking option
        match option:
            case 1:
                run_time_bar(sec_break, title='Break Time...')
            case 2:
                run_time_bar(sec_long_break, title='Long Break Time...')
            case -1:
                break
        
        # Showing total sessions
        number_sessions+=1
        sessions(number_sessions)

    end()