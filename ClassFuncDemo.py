# Classes&Functions: Classes, Functions, Objects for Classes
class MyClass:   #1st
    name = "Andrew"

    def __int__(self, name,age):
        self.name = name
        self.age = age

    def sum(self, a, b):
        print(a+b)

x = MyClass()
print(x.name)
x.sum(4,5)


