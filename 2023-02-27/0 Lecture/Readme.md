## Lab(Lecture)

# Literals in Python

- A constant value stored in the variable in a program is known as literal
```python
    a = 25
```
- Here 'a' is the variable in which constant value 25 is stored, 25 is called literal
- As 25 is an integer value it is called integer literal
- Types of literal found in python are as below:
    1) Numeric Literals
    2) Boolean Literals
    3) String Literals

#### 1) Numeric Literals:
- Available numeric literals in python are as below:

| Id | Example | Literal Name |
| :--- | :---   | :--- |
| 1 | 340, -34 | Integer Literal |
| 2 | 3.22, -3.22, 1.24E7 | Float Literal |
| 3 | 0x25A | HexaDecimal Literal |
| 4 | 0o241 | Octal Literal |
| 5 | 0B110110 | Binary Literal |
| 6 | 16+7J | Complex Literal |

#### 2) Boolean Literals:
- Boolean Literals are in the form of 'True' or 'False' values stored into boolean type variable

#### 3) String Literal:
- A group of characters is called a string literal
- This string literals are enclosed in single quotes or double quotes or some time in triple quotes as required
- In python there is no difference between single quoted strings or double quoted strings

```python
a = 'Atmiya'
b = "Atmiya"
print(a)
print(b)
a = '''Python is very helpful programming language
It is very trending and highly used language.
'''
print(a)
```

- We can use escape characters as required in a string literals

| Sr No | Escape Character | Meaning |
| :--- | :--- | :--- |
| 1 | \ | New line continuation |
2 | \n | New line
3 | \\\ | Display Single \
4 | \\' | Display Single quote (')
5 | \\" | Display double quote (")
6 | \\b | Backspace
7 | \\r | Enter
8 | \\t | Horizontal Tab
9 | \\v | Vertical Tab


```python
    # Escape Characters
    a = '''Python is very helpful programming language \
    It is very trending and highly used language.
    ''' # Use \ to combine multiple lines in one line
    print(a)

    a = '''Python is very helpful \n programming language
    It is very trending and highly used language.
    '''
```

# Determining the datatype of variable

- We can use the type function to know the datatype of variable or object
```python
    a = 16
    print(type(a))
```
- Since we are storing 16 into 'a' it is assumed by the python interpreter as 'int'
- It means that variable 'a' is an object of the class 'int'
- In fact every datatype, function, method, class, module, lists, sets, are all objects in Python
```python
    a = 16
    print(type(a))
    a = 12.4
    print(type(a))
    a = 'Atmiya'
    print(type(a))
    a = [1, 2, 3, 4]
    print(type(a))
    a = (1, 2, 3, 1,)
    print(type(a))
    a = {1, 2, 3, 1}
    print(type(a))
```


# Characters
- Python does not contain 'char' datatype to represent individual characters
- It has string (str) datatype which represents strings
```python
    a = 'A'
    print(type(a))
```
- We can access individual characters of a string using index or position numbers
```python
    a = 'Atmiya'
    print(a[0])
```