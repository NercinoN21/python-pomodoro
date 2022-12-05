'''
    Testing functions of "pop_pups.py"

    @author Nercino Neto
'''


# Native
import sys
import os

import colorama
colorama.init()
from colorama import Fore

# Getting the scripts module
sys.path.insert(0,os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__), '..')))
import scripts.pop_pups as pp

# For the tests(Native)
import unittest

# pip install pysimplegui
# To set the theme
from PySimpleGUI import theme