with open('FILE_IO/xmen.txt', 'w+') as my_file:
    my_file.write('Beast\n')
    my_file.write('phoenix\n')
    my_file.writelines([
        'Cyclops\n',
        'Bishop\n',
        'Nightcralwer\n',
    ])
    # cursor is after Nightcralwer\n
    # reset curser to 0
    my_file.seek(0)
    my_file.write('Morph')
    my_file.seek(0)

    # print(my_file.read())
    for line in my_file.readlines():
        print(line)
    #lines =  my_file.readlines()

# my_file = open('FILE_IO/xmen.txt', 'r')
# print(my_file.read())






>>> bytes
<class 'bytes'>
>>> b'this is a byte object'
b'this is a byte object'
>>> bytearray
<class 'bytearray'>
>>> my_byte=b'this is a byte object'
>>> bytes(10)
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> bytes(range(10))
b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t'
>>> 
>>> b'\x09'
b'\t'
 my_byte[0]
116
>>> my_byte[0:1] # represents the slice via integer
b't'

>>> bytearray() --- mutible
bytearray(b'')

>>> bytearray(10)
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> bytearray(range(10))
bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t')

>>> b_array = bytearray(10)
>>> b_array
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> b_array[0]=b'T'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object cannot be interpreted as an integer
>>> b_array[0:1]=b'T'
>>> b_array
bytearray(b'T\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> b_array[0]=0x10
>>> b_array
bytearray(b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> b2_array = bytearray('this is bytes')
>>> b2_array[0:1] = b'n'
>>> b2_array
bytearray(b'nhis is bytes')


>>> with open('FILE_IO/xmen.txt', 'rb') as f:
...     f.read()
... 
b'Morph\nphoenix\nCyclops\nBishop\nNightcralwer\n'

>>> with open('FILE_IO/xmen.txt', 'rb') as f:
...     f.readlines()
... 
[b'Morph\n', b'phoenix\n', b'Cyclops\n', b'Bishop\n', b'Nightcralwer\n']


>>> import sys
>>> sys.stderr.write('error\n')
error
6
>>> sys.stdout.write('testing\n')
testing
8
>>> lines = sys.stdin.readlines()
>>> lines
[]
>>> lines = sys.stdin.readlines()
writing something into lines
lines is being written to
>>> lines
['writing something into lines\n', 'lines is being written to\n']
'''