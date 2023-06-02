## Lab(Lecture)

#### 3) Sequence:
- Sequence represents group of elements or items.
- A group of integer number will form a sequence.
    1) Str Data type
        - A String is represented by a group of characters which are enclosed in single quotes or double quotes.
        - String can also be written inside ''' or """ to span group of lines including spaces
       ```python
            a = """Python is very interesting
                        ok
                        """
            b = '''Hello
                        ok
                        '''
       ```
       - To retrieve pice of string from whole string [] (Square Brackets) are used
       - The count of string begins with 0
       ```python
            print(a)
            print(b)
            a = 'Atmiya University'
            print(a[0])
            print(a[11:21])
            print(a[-1])
            print(a[-12:-1])
            print(a*2*)
       ```
    2) Bytes
        - The Bytes Datatype represents a group of byte number just like an array
        - A byte number can be any positive numbers between 0 - 255 (Both included)
        - We cannot modify any element
        ```python
            a = [2, 7, 11, 34, 16, 0] # list of bytes number
            b = bytes(a) # Convert the list into bytes array
            print(b)
            print(b[0])
            print(b[1])
            print(b[5])
            b[1] = 8 # This is not allowed
        ```
    3) Byte Array DataType
        - Byte array datatype is similar to bytes datatype, with one difference. The difference is that we can modify the elements of byte array

        ```python
            a = [2, 7, 11, 34, 16, 0] # list of bytes number
            b = bytes(a) # Convert the list into bytes array
            print(b)
            print(b[0])
            print(b[1])
            print(b[5])
            b[1] = 8 # This is allowed
            print(b[1])
        ```
    4) List DataType
        - List in python is similar to arrays in C or Java
        - A list represents a group of elements
        - The difference between list and array is that a list can store different types of elements but an array can store only one type of elements
        - The size of array is fixed but list can grow dynamically
        - Elements of lists are written between [ ... ] (Square Brackets)
        - Elements of list can be modified
        ```python
            a = ['Atmiya', 'University', 'Rajkot', 7, -45, 23.2]
            print(a) 
            print(a[0]) 
            print(a[0:3]) 
            print(a[-1]) 
            print(a*3)
            a[2] = 'Gujarat'
            print(a[2]) 
            print(a[0:3]) 
        ```
        - When using ...:... for example x[:3] it will give value of 0,1,2
    5) Tuple DataType
        - A tuple contains a group of elements which can be of different types
        - List and tuple are same with two difference
        - The first difference is that elements of tuple are written between () (Parenthesis) And the second difference is elements of tuple can not be modified
        ```python
            a = ('Atmiya', 'University', 'Rajkot', 7, -45, 23.2)
            print(a) 
            print(a[0]) 
            print(a[0:3]) 
            print(a[-1]) 
            print(a*3)
            a[2] = 'Gujarat' # This will generate an error
        ```
        - When using ...:... for example x[:3] it will give value of 0,1,2
    6) Range Datatype
        - The range datatype represents a sequence of numbers
        - The numbers in the range are not modifiable
        - Generally range is used for repeating a 'for' loop for a specific number of times
        ```python
            a = range(7)
            for i in a:print(i)
            a = range(11, 44, 2) # It will generate range starting from 11 with 1 jump every time till 43
            for i in a:print(i)
        ```