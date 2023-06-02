## Lab (Lecture)

Date: 09-05-2023

# Exception:

- An exception is an event which occurs during the execution of a program that changes the normal flow of the program's instruction

- An exception is a runtime error which can be handled by the programmer

- It means if the programmer can guess an error in the program and he can do something to eliminate the harm caused by the error, then it is called an exception

- If the programmer can not do anything in case of an error, then it is called an error not an exception

- All exceptions are represented as classes in Python

- The exceptions which are already available in python are called built-in exceptions

- The base class of all built-in exceptions is 'BaseException' class


# Exception Handling:

- Exception handling is the process of responding to unwanted or unexpected events when a computer program runs

- Exception handling deals with these events to avoid the program or system crashing

- The purpose of exception handling is to give a proper error message to the user when error occurs

- To handle exceptions, the programmer should perform following three steps.

    - ### Step 1:

        - The programmer should observe the statements in his program where their maybe possibility of exceptions

        - Such statements must be written inside a 'try block'

        ```python
            try:
                ...
            except:
                ...
        ```

        - If an error arises inside the try block the program will not be terminated

        - The PVM will understand that there is an exception, it will jump into an 'except block'

    - ### Step 2:

        - The programmer should write the except block where he should display the exception details to the user

        - The programmer should also display an error message regarding what can be done to avoid this error

        ```python
            try:
                ...
            except [ExceptionClass]:
                ...
        ```

        - Statements written inside an except block are called 'handlers' since they handle the situation

    - ### Step 3:
        
        - The programmer should perform clean-up actions like closing the file and terminating any other processes which are running

        - It should be written in the 'finally block'

       ```python
            try:
                ...
            except [ExceptionClass]:
                ...
            finally:
                ...
       ```

       - The speciality of finally block is that the statements inside finally block are executed irrespective of wether there is an error or not

- Performing the above three tasks is called exception handling

- Note:
    - A single try block can be followed by multiple except blocks

    - Except blocks can not be written without a try block

    - Writing except block and finally block is not mandatory

    - For finally block if written the will always executed


```python
    try:
        ...
    except:
        ...
    else:
        ...
    finally:
        ...
```