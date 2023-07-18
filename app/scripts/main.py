"""
    Getting and processing the data,
    and calling the pomodoro function

    @author Nercino Neto
"""


from user_input import setting_time
from time_bar_data import *
from pomodoro import pomodoro
from pop_ups import *
from PySimpleGUI import theme


def main() -> None:
    """
    Function that applies to
    complete pomodoro operation
    """

    theme("Black")
    datebase = setting_time()

    if checking_data(datebase):
        int_datebase = turning_data_into_int(datebase)

        final_datebase = TimeData(
            int_datebase[0],
            int_datebase[1],
            int_datebase[2]
        )

        pomodoro(final_datebase)
    elif datebase == {-1: "exit"}:
        # Just leave
        pass
    else:
        # Orienting and redirecting
        error()
        main()


if __name__ == "__main__":
    main()
