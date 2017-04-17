"""
list __slots__ limit the attribute of instance
"""


class limiter(object):
    __slots__ = ['age', 'name', 'job']


if __name__ == '__main__':
    x = limiter()
    x.age = 14
    print(x.age)
    x.ape = 100
