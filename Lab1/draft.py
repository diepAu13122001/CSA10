class A:
    name = "1"

    def __init__(self) -> None:
        print(self.__dir__())

    def __str__(self) -> str:
        return self.name + "--"


a = A()
b = A()

print(a.__str__())
print(a.name.__add__(b.name))


class B(A):
    def __init__(self) -> None:
        pass


c = B()
print(c.__str__())
