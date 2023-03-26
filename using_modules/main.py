#!/usr/bin/env python
# above line specifies the current python ver uses in the directory - regardless of pipenv
# import helpers
# print(f"Lowercase Letters: {helpers.extract_lower(name)}")
# print(f"Upper Letters: {helpers.extract_upper(name)}")

# import helpers as h
# print(f"Lowercase Letters: {h.extract_lower(name)}")
# print(f"Upper Letters: {h.extract_upper(name)}")

# from helpers import my_var as mvar, extract_lower as el, extract_upper as eu
# print(f"Lowercase Letters: {el(name)}")
# print(f"Upper Letters: {eu(name)}")
# print(mvar)

name = "Xiaole Guo"

# from helpers import * ### careful of name collisons!!!
# module imports
# from helpers import *
# import extras

# but if import explicitly no way to hide it
# from helpers import extract_lower
# print(f"Lowercase Letters: {extract_lower(name)}")
# # throw error when not in __all__

# print(f"Upper Letters: {extract_upper(name)}")
# everything inside of a module will excute ONCE the first time it's imported


# print(f"__name__ in main.py: {__name__}")



##### now package imports
from helpers.strings import extract_lower
from helpers import *
from helpers import variables
print(f"Upper Letters: {extract_lower(variables.name)}")
print(f"Upper Letters: {extract_upper(variables.name)}")

import helpers
print(f"From helpers: Upper Letters: {helpers.strings.extract_upper(variables.name)}")
