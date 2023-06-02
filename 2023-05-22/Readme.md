# Checking weather file exists or not

- The Operating System (os) module has a sub module by the name 'path' That contains a method 'isFile'

- This method can be used to know weather a file that we are opening really exists or not

- Syntax:

```python
    os.path.isfile(Path)
```

- It gives True if the file exists other wise False

# Working with binary files:

- Binary files handle data in the form of bytes

- It can store files like text, image, audio or video

- To open a binary file for reading purpose we can use 'rb'.

- Similarly to write bytes into binary files we can use 'wb'

- To read bytes from a binary file we can use the read method and to write bytes into a binary file we can use the write method

# To copy an Image file into Another file

# The with statement:

- The 'with' statement can be used while opening a file

- The advantage of 'with' statement is that it will take care of closing a file which is opened by it

- The format of using with statement is 

```python
    with open('fileName', 'mode') as fp:
        ...
```


# The seek and tell method:

## Tell:

- We can use tell method to know the position of the file pointer

- It returns the current position of the file pointer from the beginning of the file

- It is used in the form

```python
    fp.tell()
```

## Seek:

- If we want to move the file pointer to another position, we can use the seek () method

- It is used in the form

```python
    fp.seek(offset, fromWhere)
```

- Here 'offset' represents how many bytes to move, and 'fromWhere' represent from which position to move

- For example: fromWhere can be 0, 1, or 2

- Here, 0 represents from the beginning of the file, 1 represents from the current position and 2 represents from the ending of the file

- The default value is 0