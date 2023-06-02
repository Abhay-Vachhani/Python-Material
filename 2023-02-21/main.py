# main.py
# Use of functions
def add(x, y):
    '''
        This function takes 2 numbers and add them.
        The result of addition will be displayed.
    '''
    print('The sum of two numbers is ', x + y)

# Calling the function
print(add.__doc__)

# To generate documentation of a program
# python -m pydoc -w fileName