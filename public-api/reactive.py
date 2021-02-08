from rx import from_

def print_number(x):
    
    print('The number is {}'.format(x))

from_(range(10)).subscribe(print_number)