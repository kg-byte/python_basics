
import sys

# if len(sys.argv)<2:
#     raise Exception('missing at least one argument')

# name = sys.argv[1]
# print(f'name is {name}')


from cli import main
from cli.errors import ArgumentError

# try:
#     main()
# except ArgumentError as err:
#     print(f'Error: {err}')
#     sys.exit(1) 

# python -O using_exception.py undo assertionerror... the other way is better (above)
try:
    main()
except (ArgumentError, AssertionError) as err:
    print(f'Error: {err}')
    sys.exit(1) 




''' 
raise exception


exception_handling  $ python using_exception.py    
Traceback (most recent call last):
  File "/Users/kg-byte/self_study/python_course/exception_handling/using_exception.py", line 5, in <module>
    raise Exception('missing at least one argument')
Exception: missing at least one argument

exception_handling  $ python using_exception.py kim
name is kim



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