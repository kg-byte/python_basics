def extract_upper(phrase):
    '''
    extract_upper takes a string and return a list containing
    only the upper characters from the string.

    >>> extract_upper('Hello There, NONO')
    ['H', 'T', 'N', 'O', 'N', 'O']
    '''
    # to run doctest from docstrings
    #python -m doctest helpers/strings.py --verbose
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    '''
    extract_lower takes a string and return a list containing
    only the upper characters from the string.

    >>> extract_lower('Hello THERE, NONO')
    ['e', 'l', 'l', 'o']
    '''
    return list(filter(str.islower, phrase))

# my_var = 'extract lower and upper'
# this only prints when helper.py is run as a script  python using_modules/helpers.py
# not when imported as a module or python -m using_modules.helpers
# if __name__ =="__main__":
#     print('HELLOW FROM HELPERS')

# from helpers import * (only this is accessible)
# __all__ = ['extract_upper']

#or can be hidden as private method : _extract_upper. this would not show when from helpers import *
# but can still be explicitly imported ... only stops import *

# Show currently imported path/module
# import sys
# sys.path
# add new path/module to pthon path
# PYTHON_PATH = 'SOMEPATH/SOME_MOD'
# now we can import SOME_MOD... always look at system module first cannot be overwritten


# package module + __init__.py yay!!!

