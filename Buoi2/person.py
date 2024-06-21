class Person:
    def __init__(self, name, age) -> None:
        # print(self.__dir__())
        self.name = name
        self.age = age

    # override
    def __str__(self):
        return "Your name is: " + self.name

# inheritance
class Student(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

student1 = Student('A', 12)
print(student1.__str__())
    
