## Lab(Lecture)

# Data Types in Python
- A Datatype represents tthe type of data stored into a variable or memory

- BuiltIn Datatypes:
    1) None
    2) Numeric
    3) Sequences
    4) Sets
    5) Mappings

#### 1) None
- The None datatype in the python represents an object that does not contain any value

- In Python it is called None Object

- Python allows only one None Object in the program

- None can be used inside a function as a default value of the arguments

- While calling a function if no value is passed then the default value will be taken as None

#### 2) Numeric Types (int, float, complex):
- #### Int datatype:
    - An int datatype represents an Integer Number
    - The number must be without decimal or fraction value
    - Values can be either positive or negative; It can store very large Integer value easily
   ```python
    a = 102548787852
   ```

- #### Float datatype:
    - A float datatype represents floating point number
    - The number must be with decimal or fractional value
    - It also accepts number in scientific notation where we use 'e' or 'E' to represent power of 10
    - For example: 3.4 * 10<sup>3</sup> is written as 3.4e<sup>3</sup>
    - Suppose we write like a = 3.4*10<sup>3</sup> than is stored into variable 'a'

- #### Complex datatype:
    - A complex number is a number that is written in the form of 'a+bj'
    - Here 'a' represents the real part(Real number) of the number and 'b' may represent the imaginary part of the number
    - The part 'a' and 'b' may contain Integer or Float value for example 3+5j, 0.2+7j
    ```python
        a = 2.5 + 2.5j
        b = 3.0 + 0.5j
        c = a + b
        print(c) # 5.5 + 2j
    ```

- #### Representing binary, octal, hexadecimal numbers: 
    - A binary numbers are written by prefixing '0b' (Zero and b or B) before the value for example 0b11000011

    - Octal numbers are written by prefixing 0o (Zero and o or O) for example 0o214

    - Hexadecimal numbers are written by prefixing 0x (Zero and x or X) for example 0xD214

   ```python
    no1 = 0b110110001
    no2 = 0o214
    no3 = 0xD214
    i = int(no1)
    print('The decimal of 0b110110001 is:', i) # 433
    i = int(no2)
    print('The decimal of 0o214 is:', i) # 140
    i = int(no3)
    print('The decimal of 0xD214 is:', i) # 53780
   ```

   - We can convert a number to binary using bin(), to octal using oct() and hexadecimal using hex()
   ```python
    no = 7
    binary = bin(no)
    print(binary)
    octal = oct(no)
    print(octal)
    hexadecimal = hex(no)
    print(hexadecimal)
   ```

- #### Converting the datatype explicitly:
    - Python assumes the datatype for the variable depending upon the type of data

    - If somebody wants to convert the datatype by his own, it is called type conversion

   ```python
    # Converting the integer number into float
    a = 34
    b = float(a)
    print(b)

   ```

- #### Boolean Datatype:
    ```python
    no = 7 < 34
    print(no) # True
    no = 7 > 34
    print(no) # False
    a = True + True
    print(a) # 2
    a = True + False
    print(a) # 1

    ```