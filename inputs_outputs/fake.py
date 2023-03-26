import errno
try:
    f=open('something.txt', 'r')
except OSError as err:
    if err.errno == errno.ENOENT:
        print('File not found')
    elif err.errno == errno.EACCES:
        print('Bad permissions')



'''
>>> FileNotFoundError.__bases__
(<class 'OSError'>,)
>>> PermissionError.__bases__
(<class 'OSError'>,)
touch something.txt
inputs_outputs  $ python fake.py     
inputs_outputs  $ chmod 700 something.txt && sudo chown root:root something.txt
'''
