from inspect import stack
from builtins import print as pyPrint, input as pyInput
from ast import literal_eval

def print(*args, **kwargs):
    pyPrint('\t\t', *args, **kwargs, sep='')

def input(__prompt = '', getNumber = False):
    input = pyInput(f'\t\t{__prompt}: ')
    if getNumber:
        try:
            return literal_eval(input) if type(literal_eval(input)) in [int, float] else None
        except:
            return None
    return input

def printT(*args, **kwargs):
    pyPrint('\t', *args, **kwargs, sep='')

class PracticeSet():
    def print(self, programId):
        pyPrint(f':: Program: {programId} ::\n')
        printT('Question:')
        exec(f'print(self._{programId}.__doc__)')
        printT('Output:')
        exec(f'self._{programId}()')
        print()
    
    def _1(self):
        'Write a program that prints your name and your college name.'

        print('Name: Abhay Vachhani')
        print('University Name: Atmiya University')
    
    def _2(self):
        'Write a program that prints your address with name.'

        print('Name: Abhay Vachhani')
        print('Address: Atmiya University, Kalawad Road Rajkot - 360005')
    
    def _3(self):
        'Write a program that accept two numbers and perform all basic mathematical operation and print.'

        num1 = input('Enter first number', True)
        num2 = input('Enter second number', True)

        print()

        print(f'{num1}  +  {num2} = {num1 + num2}')
        print(f'{num1}  -  {num2} = {num1 - num2}')
        print(f'{num1}  *  {num2} = {num1 * num2}')
        print(f'{num1}  /  {num2} = {num1 / num2}')
        print(f'{num1}  %  {num2} = {num1 % num2}')
        print(f'{num1}  // {num2} = {num1 // num2}')
        print(f'{num1}  ** {num2} = {num1 ** num2}')
    
    def _4(self):
        'Write a program to calculate simple interest.'

        p = input('Enter price', True)
        r = input('Enter rate', True)
        n = input('Enter number of years', True)

        print()
        interest = p * r * n / 100
        print(f'Interest: { interest }')
        print(f'End Balance: { interest + p }')
    

practiceSet = PracticeSet()
practiceSet.print(4)