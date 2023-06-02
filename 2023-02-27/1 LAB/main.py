print('Hello')

a, b = 7, 'Hello'
print(a, b)
print('$'*7)
print('Atmiya'*2)
college = 'Atmiya'
degree = 'MCA'
a = 'Hello'

print('Degree is %s' % degree)
print('Degree is %20s' % degree)
print('Degree is %-20s' % degree)
print('{1} I am doing {0}'.format(degree, a)) # placeholder
print(f'{a} I am doing {degree}')

'''

 -----------------
|  o  |     |     |
 -----------------
 -----------------
|     |  x  |     |
 -----------------
 -----------------
|  o  |     |     |
 -----------------

'''

print('','-' * 17)
print(f'|  o  |{" " * 5}|{" " * 5}|')
print('', '-' * 17)
print(f'|{" " * 5}|  x  |{" " * 5}|')
print('', '-' * 17)
print(f'|  o  |{" " * 5}|{" " * 5}|')
print('', '-' * 17)

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

print(int(400, ))
a = 102548787852
a = 2.5 + 2.5j
b = 3.0 + 0.5j
c = a + b
print(c) # 5.5 + 2j

no1 = 0b110110001
no2 = 0o214
no3 = 0xD214
i = int(no1)
print('The decimal of 0b110110001 is:', i) # 433
i = int(no2)
print('The decimal of 0o214 is:', i) # 140
i = int(no3)
print('The decimal of 0xD214 is:', i) # 53780

no = 7
binary = bin(no)
print(binary)
octal = oct(no)
print(octal)
hexadecimal = hex(no)
print(hexadecimal)

# Converting the integer number into float
a = 34
b = float(a)
print(b)

no = 7 < 34
print(no) # True
no = 7 > 34
print(no) # False
a = True + True
print(a) # 2
a = True + False
print(a) # 1

a = """Python is very interesting
                ok
                """
b = '''Hello
            ok
            '''
print(a)
print(b)
a = 'Atmiya University'
print(a[0])
print(a[11:21])
print(a[-1])
print(a[-12:-1])
print(a*2)

a = [2, 7, 11, 34, 16, 0] # list of bytes number
b = bytes(a) # Convert the list into bytes array
print(b)
print(b[0])
print(b[1])
print(b[5])
# b[1] = 8 # This is not allowed

a = [2, 7, 11, 34, 16, 0] # list of bytes number
b = bytes(a) # Convert the list into bytes array
print(b)
print(b[0])
print(b[1])
print(b[5])
# b[1] = 8 # This is allowed
print(b[1])

a = ['Atmiya', 'University', 'Rajkot', 7, -45, 23.2]
print(a) 
print(a[0]) 
print(a[0:3]) 
print(a[-1]) 
print(a*3)
a[2] = 'Gujarat'
print(a[2]) 
print(a[0:3]) 

a = ('Atmiya', 'University', 'Rajkot', 7, -45, 23.2)
print(a) 
print(a[0]) 
print(a[0:3]) 
print(a[-1]) 
print(a*3)
# a[2] = 'Gujarat' # This will generate an error

a = range(7)
for i in a:print(i)
a = range(11, 44, 2) # It will generate range starting from 11 with 1 jump every time till 43
for i in a:print(i)

a = 25
a = 'Atmiya'
b = "Atmiya"
print(a)
print(b)
a = '''Python is very helpful programming language
It is very trending and highly used language.
'''
print(a)

# Escape Characters
a = '''Python is very helpful programming language \
It is very trending and highly used language.
''' # Use \ to combine multiple lines in one line
print(a)

a = '''Python is very helpful \n programming language
It is very trending and highly used language.
'''

a = 16
print(type(a))

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

a = 'A'
print(type(a))

a = 'Atmiya'
print(a[0])

# 4) Sets

a = {7, 16, 52, 34, 43, 34}
print(a)

# Creating the set using set()
a = set("Atmiya")
print(a)
a = set("AAtmiya")
print(a)

# List can be converted to set using set()
a = [7, 16, 52, 34, 43, 43]
a = set(a)
print(a)

# Adding elements to the set
a.update([20, 11])
print(a)

# Removing the element from the set
a.remove(11)
print(a)

# Frozenset datatype
s = {7, 16, 52, 34, 43, 43}
print(s) # Set created

# Converting the set to the frozenset
fs = frozenset(s)
print(fs)

# Mapping Types, dictionary
a = {
    1: 'ABC',
    2: 'CDE',
    3: 'EFG',
    4: 'GHI',
    5: 'IJK'
}

print(a)

# Retrieving the value using [Key] as below
print(a[2])

# Retrieving all the keys
print(a.keys())

# Retrieving all the values
print(a.values())

# Updating the value of Key
a[2] = 'XYZ'
print(a)

# Deleting the element
del a[2]
print(a)

# We can create empty dictionary
b = {}
print(b)

# Adding keys and values to the empty dictionary
b[1] = 'abc'
b[2] = 'cde'
b[3] = 'efg'
b[4] = 'ghi'
print(b)

