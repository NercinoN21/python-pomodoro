'''
    Control of data on study time and 
    break times entered by the user.

    @author Nercino Neto
'''

# Native
import re
from dataclasses import dataclass


@dataclass
class TimerData:
    study_time: int
    break_time: int
    long_break_time: int

    def date_in_seconds(self) -> list[int] :
        """Converts from minutes to seconds.

        Returns:
            list[int]: Returns the variables 
            in "self" multiplied by 60
        """
        
        return [self.study_time * 60,
                self.break_time * 60,
                self.long_break_time * 60]

def checking_data(initial_data: dict) -> bool:
    """Checking user input

    Args:
        initial_data (dict): A dictionary with time 
                             entered by the user

    Returns:
        bool: Value verification result.
              Checks if the user's input is a number,
              does not start with 0 and is greater than zero.
    """
    
    regex_number = "^[0-9]+$"
    for value in initial_data.values():
        if not re.search(regex_number, value) or value[0] == "0":
             return False

    return True

def turning_data_into_int(initial_data: dict) -> list[int]:
    """Transforming dict values to list of int

    Args:
        initial_data (dict): Dict of user-entered data

    Returns:
        list[int]: Dict values ​​converted to int
    """
    return [int(value) for value in initial_data.values()]