'''
fitst example
 class sentence
 attribute
 method
 Inheritance
 Overload
 naming fields
'''


class MixedNames:
    # the assignment of attribute
    data = 'spam'

    # initialize the instance
    def __init__(self, value):
        self.data = value

    # normal method,self means the instance
    def display(self):
        print(self.data, MixedNames.data)


# Inheritance , Overloading
class Super:
    def method(self):
        print('in super.method')


class Sub(Super):
    def method(self):
        print('starting Sub.method')
        Super.method(self)
        print('ending Sub.method')


# naming fields
test = 11


def f():
    print(test)


def g():
    test = 22
    print(test)


class C:
    test = 33

    def m(self):
        test = 44
        self.test = 55


if __name__ == '__main__':
    # x = MixedNames(1)
    # y = MixedNames(2)
    # x.display()
    # y.display()
    # x = Super()
    # x.method()
    # x = Sub()
    # x.method()
    print(test)
    f()
    g()
    print(test)
    obj = C()
    print(obj.test)
    obj.m()
    print(obj.test)
    print(C.test)
    print(C.__dict__.keys())
    print(C.__name__)
    print(C.__bases__)
    print(dir(obj))
