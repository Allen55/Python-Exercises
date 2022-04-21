def code(se):
    print(f"{se[1]} is writing code")


class SoftwareEngineers:

    # class attributes
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")

    # def information(self):
    #    information = f"name = {self.name}, age = {self.age}, level={self.level}"
    #    return information

    # dunder method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level={self.level}"
        return information




se1 = SoftwareEngineers("Tim", 31, "E5", 5000)
se1.code()
se1.code_in_language("Python")


print(se1)