import sys
import random
try:
    print(f'First argument {sys.argv[1]}')
    args = sys.argv
    random.shuffle(args)
    print(f'Random argument {args[0]}')
except (IndexError, KeyError) as err: # will catch indexError, keyError or any subclass of these two (using tuple)
    print(f'error: no arguments, please provide at least one ({err})')
    sys.exit(1)
except NameError:
    print('Error: random module not loaded')
    sys.exit(1)
else: # happy path runs when no exception caught
    print('else is running')
finally: # always runs 
    print('finally is running')



'''
exception_handling  $ python using_try.py
error: no arguments, please provide at least one (list index out of range)

exception_handling  $ python using_try.py something.py
First argument something.py
Error: random module not loaded

exception_handling  $ python using_try.py             
error: no arguments, please provide at least one (list index out of range)
finally is running

exception_handling  $ python using_try.py something.py
First argument something.py
Random argument using_try.py
else is running
finally is running
exception_handling  $ 
'''


''' 
raise exception

>>> err=Exception('something went wrong')
>>> str(err)
'something went wrong'

>>> dir(err)
['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', 'args', 'with_traceback']
>>> 


Exception.__subclasses__()
[<class 'TypeError'>, <class 'StopAsyncIteration'>, <class 'StopIteration'>, <class 'ImportError'>, <class 'OSError'>, <class 'EOFError'>, <class 'RuntimeError'>, <class 'NameError'>, <class 'AttributeError'>, <class 'SyntaxError'>, <class 'LookupError'>, <class 'ValueError'>, <class 'AssertionError'>, <class 'ArithmeticError'>, <class 'SystemError'>, <class 'ReferenceError'>, <class 'MemoryError'>, <class 'BufferError'>, <class 'Warning'>, <class 'warnings._OptionError'>, <class 're.error'>, <class 'sre_parse.Verbose'>, <class 'locale.Error'>, <class 'tokenize.TokenError'>, <class 'tokenize.StopTokenizing'>, <class 'inspect.ClassFoundException'>, <class 'inspect.EndOfBlock'>]

>>> IndexError.__bases__
(<class 'LookupError'>,)

'''