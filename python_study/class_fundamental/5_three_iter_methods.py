"""
__contain__,__iter__,__getitem__
__contain__ > __iter__ > __getitem__
"""


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):
        print('get[%s]:' % item, end='')
        return self.data[item]

    # def __iter__(self):
    #     print('iter=> ', end='')
    #     self.ix = 0
    #     return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

        # def __contains__(self, item):
        #     print('contains: ', end='')
        #     return item in self.data


if __name__ == '__main__':
    # 1.initial version
    # 2.annotate __contain__
    # 3.annotate __contain__ and __iter__
    x = Iters([1, 2, 3, 4, 5])
    # except 'in' op, other iteration use __iter__ and __next__
    print(3 in x)
    for i in x:
        print(i, end=' | ')

    print('\n')
    print([i ** 2 for i in x])
    print(list(map(bin, x)))

    I = iter(x)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
