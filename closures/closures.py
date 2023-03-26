#creating functions inside of functions it holds the parameter passed in
#partial function application (similar)
#aka factory function
def greeter(prefix):
    def greet(name):
        other_name = 'dear ' if name == 'Kaki' else '' 
        other_name = 'sweet ' if prefix=='Goodbye,' and name=='Kaki' else other_name
        love = '˚ʚ♡ɞ˚' if other_name == 'dear ' else ''
        love = '♥' if other_name == 'sweet ' else love
        print(f'{prefix} {other_name}{name}{love}')
    return greet

hello = greeter('Hello,')
goodbye = greeter('Goodbye,')

hello('Tino')
hello('Kaki')
goodbye('Tino')
goodbye('Kaki')
