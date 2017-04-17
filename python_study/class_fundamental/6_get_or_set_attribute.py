"""
1.__getattr__
2.__setattr__
"""


class empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)


class accesscontrlo:
    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__[key] = value
        else:
            raise AttributeError(key + ' not allowed')


if __name__ == '__main__':
    x = empty()
    print(x.age)
    # print(x.name)
    x = accesscontrlo()
    x.age = 40
    print(x.age)
    x.name = 'nel'
