## Lab (Lecture)

Date: 10-05-2023

# Types of exception (Built in exceptions):

# The assert statement:

- The assert statement is useful to ensure that a give condition is True

- If it is not True it raises an AssertionError

- Syntax:

```python
    assert Condition, Message [Message not mandatory]
```

- Assertion method can be written in two ways, 
    
    1. If the condition is False than the exception by the name AssertionError is raised along with the message written in the assert statement

    2. If the error message is not written then the AssertionError without the message will be displayed

# User defined exception (Custom Exception):

# File Handling:

## Types of Files:

- In python there are two types of files 
    1. Text files
    2. Binary Files

- Text files store the data in the form of characters

- For example. If we store student name 'abc', It will be stored as a three characters and his score is 87 then it store it as a two characters

- Normally text file are used to store characters or strings

- Binary files store entire data in the form of bytes i.e. a group of 8 bits each

- When the data is retrieved from the binary file, The programmer can retrieve the data as bytes

- Binary files can be used to store text, images, audio and video files

## Opening and Closing file:

- We should use open( ) to open a file

- This function accepts 'FileName' and 'OpenMode' in which to open the file

- Syntax:
```python
    fileHandler = open('fileName', 'openMode')
```

### File opening mode:
To write data in to a file if any data is already present in the file, It would be deleted and the present data will be stored

| Mode | Description                                                                                                                                                   |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| w    | To write data in to a file if any data is already present in the file, It would be deleted and the present data will be stored                                |
| r    | Read data from the file. The file pointer is placed at the beginning at the file                                                                              |
| a    | To append data to a file. Appending at the end of existing data. File pointer is placed at the end of the file. If the file is not present it will be created |
| x    | To open the file in exclusive creation mode. The file creation fails if the file already exists                                                               |
| +    | + with w, r, a will allow both reading and writing                                                                                                            |

### Closing the file:

- A file which is opened should be close using the close( )

- If the file is not closed then data may get corrupt or we may loss data.

- Also if file not closed then it may not free the memory till the file is open

- We can close file using f.close()

- 