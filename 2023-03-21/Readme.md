## Lab (Lecture)

# if...elif...else statements:

- When there is a need of testing multiple conditions and execute statements depending on those conditions, You can write several elif statements between if and else

- Syntax:
```python
    if condition:
        statements1
    elif condition:
        statements2
    elif condition:
        statements3
    else:
        statements4
```

- Else is not mandatory while using if...elif

- When condition1 is True, the statements1 will be executed
- If condition1 is False, than condition2 is evaluated
- When condition2 is True, the statements2 will be executed
- When condition2 is False, the condition3 is tested
- If condition3 is True, than statements3 will be executed
- When condition3 is False, the statements4 will be executed
- It means statements4 (Statement under else) will be executed only if None of the conditions are True

- Example:
```python
    if True:
        print('Condition is True')
    elif False:
        print('Condition is False')
    else:
        print('Condition is False')
```