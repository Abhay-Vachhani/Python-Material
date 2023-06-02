## Lab(Lecture)

# Comments in Python

- There are two types of comments
    1) Single Line Comment
    2) Multi Line Comment

#### 1) Single Line Comment:
- Single line comment uses # (Hash) at the starting of a line

- The entire line after the # symbol will be considered as a comment

- Example:
```python
# The below line will print Atmiya University
print('Atmiya University')
print('Rajkot') # Rajkot will be printed
```

- Comments are non executable statements

- It means neither the python compiler nor the PVM will execute them

#### 2) Multiline Comment:
- When it is require to mark more than one line as an comment writing # (Hash) symbol in the beginning of the every line is tedious

- Instead of writing # at the starting of every line, we can use ''' Or """ before and after the lines to be commented

- Example:
```python
'''
Take name from the user
Take contact details from the user
'''

# Or

"""
Take name from the user
Take contact details from the user
"""
```

# Doc Strings:
- In fact python supports only single line comments

- Multiline comments are not available in python the triple double quotes and triple single quotes are actually not multiline comments but they are regular string with the exception that they can ................ multiple lines. In other words memory will be allocated to this strings internally.

- If these strings are not assigned to any variables, then they are removed from the memory by the garbage collector and hence this can be used as comments

- So """ or ''' is not recommended to be used since they internally occupy memory and would west time of interpreter since the interpreter has to check them

- If we write strings inside ''' or """ as first statement in a module, function, class or a method, then this strings are called documentation strings or doc strings

- These doc strings are useful to create an API documentation file from a python program

- An API documentation file is a text file or html file that contains description of all the features of software, language or a product

- This file describes all the classes, modules, functions, etc... which are written in the software

- So we can understand that the API documentation file is like a help file for the end user

- Let's take an example to understand how to create an API

```python
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
```

- We assume that the name of this file is main.py

- In order to create an API file we need to write

```console
python -m pydoc -w main
```

![s](example.svg)