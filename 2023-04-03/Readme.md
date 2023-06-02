## Lab (Lecture)

## Continue statement:












## pass statement:
- The pass statement is used as a placeholder for future code.

- When the pass statement is executed nothing happens, but you avoid getting an error when empty code is not allowed

- Empty code is not allowed in loops, function def, class definitions or in if statements (some times)

- Using pass inside a loop, function or a class gives you a facility to keep it empty

- Pass statements is used when we need a statement syntactically but we do not any operation

- The difference between pass and comment is that comment is ignored by the interpreter where as pass is not ignored

- Example:

```python
    if True:
        pass
```

## Array:

- An array is an object that stores a group of elements with same data types.

- The main advantage of an array is to store and process a group of elements easily

- An array can store only one type of data

- It means we can store only integer type or only float type elements into an array at a time

- But we cannot store one Integer value, one Float and one Character type element into the same array

- An array can increase or decrease their size dynamically

- It means we need not declare the size of an array

- When elements are added it will increase their size and when element are removed it will automatically decrease their size in memory

## Advantages of array:

- Arrays are similar to list. the main difference is that arrays can store only one type of elements list can store different type of element

- When dealing with huge number of elements array uses less memory than list

- Arrays offer faster execution then list

## Creating an array:

- Syntax:
```python
    variableName = array(type code, [elements])
```

![Type Code](type%20code.jpg)

## Importing array module:

- There are three ways to import the array module into our program
    
1) 
```python
    import array
    a = array.array('i', [1, 2, 3])
```

- When we import the array module we are able to get the array class of that module that helps us to create an array

- Here the first 'array' represents a module name and the next 'array' represents the class name for which object is created

2) 
```python
    import array as ar
    a = ar.array('i', [1, 2, 3])
```

- Here 'ar' is an alias of array module

3) 
```python
    from array import *
    a = array('i', [1, 2, 3])
```

- The meaning of this statement is import all (classes, objects, variables, etc...) from the array module into our program so there is no need to mention the module name before array name while creating


