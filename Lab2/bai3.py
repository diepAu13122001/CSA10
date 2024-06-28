class Square:
    def __init__(self, edge) -> None:
        self.edge = edge

    def cal_area(self):
        return self.edge**2


class Cube(Square):
    def __init__(self, edge) -> None:
        super().__init__(edge)

    def cal_volume(self):
        return self.edge**3

    def cal_area(self):
        return 6 * self.edge**2


# driver code
square_1 = Square(4)
cube_1 = Cube(4)
print(cube_1.cal_area())
