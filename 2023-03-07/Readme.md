## Lab (Lecture)

# Operators:

### 7) Membership Operators:
- The membership operators are useful to test for membership in a sequence such as strings, lists, tuples, or dictionaries
- For example, if an element is found in a sequence or not can be asserted using these operators
- There are two membership operators
- 1) in
- 2) not in

#### 1) The in operator:
- This operator returns True if an element is found in the specified sequence
- If the element is not found in the sequence then it returns False

#### 2) The not in operator:
- This operator returns True if an element is not found in the sequence
- If the element is found in the sequence then it returns False

- Example:
```python
city = ('Rajkot', 'Surat', 'Vadodara', 'Ahmedabad')
print('Rajkot' in city)
print('Rajkot' not in city)
```

### 8) Identity Operators:
- These operators compare the <u>memory location</u> of two objects
- The memory location of an object can be seen using id( ) function
- These function returns an integer number, called the identity number internally represents the memory location of the object

```python
    a = 16
    print(id(a))
    b = 16
    print(id(b))
```

- There are two identity operators 
- 1) is
- 2) is not

#### 1) The is operator:
- The is operator is useful to compare wether two objects are located at the same location in the memory or not
- It will internally compare the identity number (Address) of the object
- If the identity number of the objects are same it will return True, otherwise it will return False

#### 2) The is not operator:
- If the identity numbers of the objects are not same it will return True otherwise it will return False

```python
    a = [1, 2, 3]
    b = a
    c = a[:]

    print(a is b, a == b) # True True
    print(a is c, a == c) # False True
    
    print(a is not b, a != b) # False False
    print(a is not c, a != c) # True False
```