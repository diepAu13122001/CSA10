class Rectangle:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def calPerimeter(self):
        return "=> Perimeter: " + str((self.height + self.width) * 2)

    def calArea(self):
        return "=> Area: " + str(self.height * self.width)


class Circle:
    PI = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius

    def calPerimeter(self):
        return "=> Perimeter: " + str((self.radius * self.PI) * 2)

    def calArea(self):
        return "=> Area: " + str(self.radius**2 * self.PI)


user_input = input("Shape (rectangle|circle): ")
# match - case
match user_input:
    case "rectangle":
        h = float(input("Height: "))
        w = float(input("Width: "))
        # khai bao obj - instance
        rec = Rectangle(height=h, width=w)
        print(rec.calPerimeter())
        print(rec.calArea())

    case "circle":
        r = float(input("Radius: "))
        # khai bao obj - instance
        cir = Circle(radius=r)
        print(cir.calPerimeter())
        print(cir.calArea())

    case _:
        print("=> Invalid!")
