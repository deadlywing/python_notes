"""
1.Lambda expression
2.map function -> return iterable
3.filter -> return iterable and reduce -> return a number
"""


# 1.1 LEGB
def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action


# 1.2 lambda for jump table
L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]

# 1.3 some logic in lambda
# 1.print -> sys.stdout.write(str(x)+'\n')
# 2.if\else -> b if a else c
# 3.loop -> map function or list comprehension

import sys

showall = lambda x: list(map(sys.stdout.write, x))

# 2. map function for multiple sequential inputs
print(list(map(pow, [1, 2, 3], [2, 3, 4])))

# 3.1 filter function
print(list(filter((lambda x: x > 0), range(-5, 5))))
# 3.2 reduce function
from functools import reduce

print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))

if __name__ == '__main__':
    act = knights()
    print(act('robin'))

for f in L:
    print(f(2))
print(L[0](3))

t = showall(('spam\n', 'toast\n', 'eggs\n'))
