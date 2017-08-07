# test git


def print_test():
    print('print 1')


def print_test1(*arg):
    print(arg)


# define some class

class Father:
    def __init__(self, name, age, gender):
        """

        :rtype: Father type
        """
        self.__Name = name
        self._Age = age
        self.Gender = gender

    def Fprint(self):
        print('this is father')

    @property
    def salarys(self):
        return self.salary

    @salarys.setter
    def salarys(self, sal):
        self.salary = sal


bob = Father("BOB", 45, 'male')
# print(bob._Age)
# print(bob._Father__Name)
bob.salary = 15000
print(bob.salarys)

# print_test1('test', 12, ['df', 12])
