class ExampleError(Exception):
    pass


def bad_function():
    raise ExampleError('this is a message', 1,2, {'something':[3,4,5]})

try:
    bad_function()
except ExampleError as err:
    message, x, y, *other = err.args
    print(message)
    print(x+y)
    print(other)


'''
exception_handling  $ python exception_args.py
this is a message
3
[{'something': [3, 4, 5]}]
'''