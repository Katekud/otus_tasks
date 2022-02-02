from src.Figure import Figure

class Square(Figure):

    def __init__(self, a: float):
        self.a = a
        super().__init__('Square')

        if not self.correct(a):
            self.raise_error()

    @property
    def area(self) -> float:
        return self.a * self.a

    @property
    def perimeter(self) -> float:
        return 4 * self.a

if __name__ == '__main__':
    pass

