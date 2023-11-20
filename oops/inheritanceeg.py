class BaseClass:
    def display(self):
        print("hello")


class SubClass(BaseClass):
    def welcome(self):
        print("Welcome")


x = BaseClass()
x.display()
y = SubClass()
y.display()
y.welcome()
