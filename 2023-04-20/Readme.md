## Lab (Lecture)

Date: 20-04-2023

# Searching an element from the array:

- Example:
---
![Search element from array](https://pypro.tech/Resources/Images/17_Search-element-from-array.jpg)

Date: 20-04-2023

# Types of Arrays:

## 1. Single Dimensions Arrays:

- These arrays represents only one row or one column of elements

- For example marks obtained by a student in 5 subjects can be written as 

    ```python
        marks = array('i', [20, 30, 40, 50, 60])
    ```
- The above array contains only one row (marks of one student)

- Hence it is called single dimensional array or one dimensional array

## 2. Multi Dimensional Arrays:

- These arrays represents more than one row and more than one column of elements

- For example marks obtained by 3 students in 5 subjects can be written as

    ```python
        marks = [
            [20, 30, 40, 50, 60],
            [20, 30, 40, 50, 60],
            [20, 30, 40, 50, 60],
        ]
    ```

- Python supports only single dimensional  array. But we can create multi dimensional array using third party packages like 'numpy' (Numerical Python)

# Working with arrays using numpy:

- Numpy is a package that contains several classes, functions, variables, etc... to deal with scientific calculations in python

- We can create single dimensional as well as multi dimensional arrays using numpy

- Numpy contains a large library of mathematical functions

- Generally arrays which are created using numpy are called 'n-dimensional array'

- If numpy module not found then install it using below command execute it in terminal

```console
    pip install numpy
```

- To work with numpy we must first import numpy module into our python program

## Creating array using linspace

- Syntax:
```python
    linspace(start, stop, n)
```

- Start: Starting element
- Stop: ending element
- N: Number of parts element should be divided (by default 50)

## Creating array using logspace

- Syntax:
```python
    logspace(start, stop, n)
```

- Start: Starting element (10^start)
- Stop: ending element (10^end)
- N: Number of parts element should be divided (by default 50)

## Creating array using arange

- Syntax:
```python
    arange(start, stop, stepSize)
```

![Numpy Array](https://pypro.tech/Resources/Images/18_Numpy-Array-1.jpg)
![Numpy Array](https://pypro.tech/Resources/Images/19_Numpy-Array-2.jpg)