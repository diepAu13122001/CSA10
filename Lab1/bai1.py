class Employee:
    def __init__(self, fullname, position) -> None:
        # gan gia tri mac dinh cho attributes
        self.fullname = fullname
        self.position = position

    def say_hi(self):
        return 'Hello ' + self.fullname
    
    def tell_position(self):
        return 'I am ' + self.position


# snake case: get_name
# camel case: getName

# khai bao object
worker1 = Employee("Nguyen Van A", "team leader")
worker2 = Employee("Nguyen Van B", "Java dev")
print(worker1.say_hi())
print(worker2.say_hi())
print(worker2.tell_position())