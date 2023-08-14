class A:
    def public(self):
        return 42
    def _print(self):
        return 'test'
    def __protected(self):
        return(True)
    def func(self):
        return self.__protected()
a=A()
print(a.public())
print(a._print())
print(a.func( ))
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        print(f'Имя: {self.name}, возраст: {self.age}')
tom=Person('Tom', 16)
tom.print_info()