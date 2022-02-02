from src.Figure import Figure
from src.Square import Square
from math import sqrt


class Triangle(Figure):

    def __init__(self, a: float, b: float, c: float):
        super().__init__('Triangle')
        self.a, self.b, self.c = a, b, c

        if a + b <= c or a + c <= b or c + b <= a:
            self.raise_error()

    @property
    def area(self) -> float:
        p = self.perimeter/2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c

if __name__ == '__main__':
    pass
