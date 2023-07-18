"""
    Responsible for run the study time,
    break and final message

    @author Nercino Neto
"""


from user_input import *
from pop_ups import *
from time_bar import *
from time_bar_data import TimeData


def pomodoro(data: TimeData) -> None:
    """Responsible for operation after obtaining data"""

    sec_study, sec_break, sec_long_break = data.date_in_seconds()

    number_sessions = 0
    while True:
        run_time_bar(sec_study, title="Studying...")
        option = echoose_break_time(data.break_time, data.long_break_time)

        match option:
            case 1:
                run_time_bar(sec_break, title="Break Time...")
            case 2:
                run_time_bar(sec_long_break, title="Long Break Time...")
            case _:
                break

        number_sessions += 1
        sessions(number_sessions)

    end()
