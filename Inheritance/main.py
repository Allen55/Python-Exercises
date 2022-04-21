# inherit, extend, override
class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f"{self.name} is working...")


class SoftwareEngineer(Employee):
    pass


class Designer(Employee):
    pass


se = SoftwareEngineer("Max", 31)
print(se.name, se.age)
se.work()

d = Designer("Lisa", 22)
print(d.name, d.age)
d.work()