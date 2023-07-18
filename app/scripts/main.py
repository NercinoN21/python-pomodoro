"""
    Getting and processing the data,
    and calling the pomodoro function

    @author Nercino Neto
"""


from user_input import setting_time
import time_bar_data as tbd
from pomodoro import pomodoro
from pop_ups import error
from PySimpleGUI import theme


def main() -> None:
    """
    Function that applies to
    complete pomodoro operation
    """

    theme("Black")
    datebase = setting_time()

    if tbd.checking_data(datebase):
        int_datebase = tbd.turning_data_into_int(datebase)

        final_datebase = tbd.TimeData(
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
