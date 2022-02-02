from src.Figure import Figure

class Rectangle(Figure):

    def __init__(self, a: float, b: float):
        self.a, self.b = a, b
        super().__init__('Rectangle')
        if not (self.correct(a) and self.correct(b)):
            self.raise_error()

    @property
    def area(self) -> float:
        return self.a * self.b

    @property
    def perimeter(self) -> float:
        return 2 * (self.a + self.b)

if __name__ == '__main__':
    pass