"""
1.1 __getitem__ and __setitem__
1.2 __iter__ and __next__
"""


# __getitem__ intercept index operation and can response iter
class stepper:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value


# __iter__ and __next__
#  __iter__ -> single iteration,while __getitem__  -> multi iteration
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


# create multi iteration version of __iter__
class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 1
            return item


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


if __name__ == '__main__':
    x = stepper(['a', 'b', 'c', 'd'])
    # intercept indexing(slicing) op
    print(x[2])
    print(x[::-1])
    # intercept indexing assignment op
    x[0] = '1'
    # response iter (be able to response multiple times)
    # eg1 : for loop
    for item in x:
        print(item, end=' \n')
    # eg2 : tuple assignment and classic method
    (a, b, c, d) = x
    print(a, c, d, sep=' ')
    print(list(x), ''.join(x), sep=' ')

    # test __iter__ and __next__
    for i in Squares(1, 5):
        print(i, end=' ')
    print('\n')
    y = Squares(1, 5)
    print(iter(y) == y)

    # multi iteration of __init__
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I), sep=' ')
    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
