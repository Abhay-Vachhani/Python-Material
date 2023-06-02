## Lab (Lecture)

# Input statements:
- To accept input from the keyboard Python provides the input( ). This function takes a value from the keyboard and returns it as a string

```python
    a = input()
    print(a)

    # With message
    name = input('Enter your name')
    print(name)

    # Restricted entry
    no = int(input('Enter the number'))
    print(no)

    no = float(input('Enter the number'))
    print(no)

    # Only the first character will be displayed
    char = input('Enter the character:')[0]
    print(char)

    # Adding two values by taking from user using .format
    a = int(input('Enter the first value:'))
    b = int(input('Enter the second value:'))
    print('The sum of {0} and {1} is {2}'.format(a, b, a + b))

    # Adding and finding the product of two values by taking from user using .format
    a = int(input('Enter the first value:'))
    b = int(input('Enter the second value:'))
    print('The sum of {0} and {1} is {2} and the product of {0} and {1} is {3}'.format(a, b, a + b, a * b))
```

## Use of split( ) method:
- When the user enters three values, they are accepted as string.
- This strings are divided where ever a space is found (By Default) by split method.
- This strings are read by for loop and converted into integers by the int ( ).
- This integers are stored into no1, no2, no3

```python
    a = [a for a in input('Enter the strings:').split()]
    print(a)

    no1, no2, no3 = [int(no) for no in input('Enter three numbers:').split()]
    print('The sum of three numbers are:', no1 + no2 + no3)
```

## Use of eval( ) function:
- The eval() takes a string and evaluates the result of the string by taking it as a python expression

```python
    a, b = 7, 16
    ans = eval('a + b + 3')
    print(ans)

    # Using eval() along with input(), taking expression from the user.
    a, b = 7, 16
    ans = eval(input('Enter an expression'))
    print('The result of your expression is: %d' % ans)
```