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
