## Lab (Lecture)

# Input Output Statements:
- The data given to the computer is called input.
- The results returned by computer are called output.
- So we can say that a computer takes input, processes that input and produces the output

## Output Statements:
- The output in Python is displayed using print() function
- The print function can be used in different formats

### The print( ) statement:
- When the print( ) is called simply, it will throw the cursor to the next line.
- It means that a blank line will be displayed

```python
    print()
```

### The print('String') statement:
- The string represents a group of characters
- When a string is passed to the print( ), The string is displayed as it is

```python
    print('Atmiya')
```

- Note that single quotes or double quotes have the same meaning
- We can use escape sequence characters inside the print( )

```python
    print('This is a \n new line')
    print('The tab is \tis used here')
```

- The '+' operator when used with number will add both numbers but when used with strings it will work as a concatenation operator. It will join two strings

```python
    print('The city is ' + 'Rajkot')
```

### The print(variable list) statement:
- We can also display the values of variables using the print( )

```python
    a, b = 7, 16
    print(a, b)
```

- We can separate the string using 'sep' attribute

```python
    print(a, b, sep=', ')
```

- Each print( ) throws the cursor to the next line after displaying the output

```python
    print('Atmiya')
    print('University')
    print('Rajkot')
```

- We can use 'end' attribute as below

```python
    print('Atmiya', end='\t')
    print('University')
    print('Rajkot')
```

### The print(object) statement:
```python
    a = [7, 'Atmiya', 'Rajkot']
    print(a)
```

### The print('String', variable list) statement:
- The most common use of the print( ) is to use strings along with variables inside the print( )

```python
    a = 7
    print(a, 'The value is printed here')
    print('User have entered', a, 'as an input')
```

### The print(formatted string) statement:
- We can formate the output using the print( )
- For that purpose the special operator '%' is used it joins string with a variable
- We can use %i or %d to represent decimal integer numbers
- We can use %f for to represent float values
- We can use %s to represent strings

```python
    a = 7
    print('Value is %i' % a)
    
    a, b = 10, 16
    print('a is %i b is %i' % (a, b))
    print('a is %i b is %i' % (b, a))

    university = 'Atmiya'
    print('Hi %s' % university)
    print('Hi %20s' % university)
    print('Hi (%-20s)' % university)

    print('The first character is %c, and the second character is %c' % (university[0], university[1]))

    num = 123.456789
    print('The number is %f' % num)
    print('The number is %6.2f' % num)
```

### Inside the formatted string:

```python
    no1, no2, no3 = 1, 2, 3
    print('The first number is {0}, the second number is {1}, the third number is {2}'.format(no1, no2, no3))
```