## Lab (Lecture)

Date: 05-05-2023

# Returning multiple values from a function:

- A function in python can written multiple values

- When function calculates multiple results and wants to return all those results we can use the return statement as: return a, b, c

- These values are returned by a function in the form of a tuple

# Pass by Object:

- Immutable objects in python: int, float, string, tuple
- Mutable objects in python: list

![alt](Pass%20By%20Object.jpg)

- As the value assigned to variable 'a' is of integer type, modifying the value of 'a' will not be stored at a same memory address

- As integer is immutable, modifying the value of 'a' will occupy another memory to store a new value of new 'a'

# Formal and Actual Arguments:

def foo(a, b): --> Formal Arguments

                ------
s = 10, m = 6   --> Actual Arguments

# The actual arguments are of 4 types:

- Positional Arguments
- Keyword Arguments
- Default Arguments
- Variable Length Arguments

## Positional Arguments:

- The number of arguments and their positions in the function definition should match exactly with the number and position of the argument in the function call

<!-- Extra -->
## Keyword Arguments:

- Keyword arguments are arguments that identify the parameters by their names

- At the time of calling function, we have to pass two values and we can mention which value is for what


## Default Arguments:
- If required we can set a default value to the parameter

- If at the time of calling the function, the value is not passed to the argument then default value will be used

- And if the value is passed to the argument then the passed value will be used

## Variable Length Arguments:

- In some situation it is possible that the programmer is an aware about the requirement of the parameters in the program 

- if in program two parameters are declared, and while using it user feel to give more than two values than error will occur

- In that case variable length argument can be used

- A variable length argument is an argument that can accept any number of values

# Passing a Group of elements to a function

- Some time it is required to receive group of elements like numbers or strings, we can accept them into a list and then pass the list to the function

# Anonymous Functions (Which is also known as lambda):

- We already know that while writing a function we need to give name to the function

- We usually do it like: def nameOfFunction ( arguments... ):

- But the anonymous function is not defined with def it is defined with the keyword 'lambda'

```python
    def sq(a):
        return a * a
```

- This could be written in anonymous function as

```python
    sq = lambda a : a * a
```


# Generators:

- Generators are functions that return a sequence of values

- A generator function is written like an ordinary functions but it uses yield statement

- The 'yield' statement is useful to return the value
