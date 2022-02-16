from src.Figure import Figure
from math import pi

class Circle(Figure):

    def __init__(self, radius: float):
        self.radius = radius
        super().__init__('Circle')

        if not self.correct(radius):
            self.raise_error()

    @property
    def area(self) -> float:
        return pi * self.radius * self.radius

    @property
    def perimeter(self) -> float:
        return pi * 2 * self.radius

if __name__ == '__main__':
    pass