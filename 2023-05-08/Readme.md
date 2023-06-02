## Lab (Lecture)

Date: 08-05-2023

# Packages:

- A python module may contain several classes, functions, variables, etc ... where as, a python package contains several modules

- In simpler term package is a folder that contains several modules

- A package should contain an additional file named '\_\_init__.py' so that a python interpreter can understand that this is a package

- \_\_init__.py helps a python interpreter to differentiate between a simple folder and a package 

- In other words, \_\_init__.py helps the python interpreter reorganize that the folder is a package

- Now lets create a folder named DemoPackage, In which we would make \_\_init__.py, Add.py, Sub.py, Mul.py, Div.py is also created

- A python file named Add.py, Sub.py, Mul.py, Div.py will contain a function as per our requirement

- Now create another file named main.py file in which we may call all the above modules except \_\_init__.py

- The location main.py would be in the same hierarchy of DemoPackage folder

- Note that main.py should be not inside the folder DemoPackage


# Composition:

- Composition is much more elegant way of using methods and attributes from a parent class in a child class

- The problem with inheritance is that child class inherits all attributes and methods

- With composition we can choose what is to be inherited from the parent class

- Inheritance = Take everything
- Composition = Take what you need, and leave the rest

# Errors in Python:

- A software developer is a human being and human being can commit errors

- This error could be at the designing phase or while writing a code

- In general we can classify errors in a program into one of these three types 

    1. Compile time errors
    2. Runtime errors
    3. Logical errors

## 1. Compile time Errors:

- These types of errors are generally a syntactical error in the code, due to which a program fails to compile

- It could be because of forgetting a ':' after writing a loop, or after if or else 

- Such errors are detected by the python compiler

- If the indentation rule of a code is not maintained in the code then it would end up into compile time error

```python
    a = 10
    if a == 10
    print('The value of a is 10')
```

## 2. Runtime Errors:

- When the PVM cannot execute the bytecode, it flags runtime error

- For example in sufficient memory to store something

- Runtime errors are not detected by the python compiler they are detected by the PVM only at runtime

```python
    def concat(a, b):
        print(a + b)
    concat('I like programming', 100)
```


- The above code may result into a 'TypeError' which could not be caught by the compiler

- Type checking is done by PVM only at runtime

```python
    print([0,1,2][5]) # IndexError
```

- The above code may result into a 'IndexError' which could not be caught by the compiler

- Index checking is done by PVM only at runtime

## 3. Logical Errors:

- Logical errors are neither detected by the compiler nor by the PVM

- It is a type of error which happens when the programmer might be using a wrong formula or some times design of the program it self is wrong

- The programmer is solely responsible for these types of errors

```python
    def inc(sal):
        sal = sal * 15 / 100 # sal += sal * 15 / 100
        return sal
    sal = inc(1000)
```

- Incase of runtime errors when the programmer knows which type of error occurs he has to handle them using exceptional handling mechanism

