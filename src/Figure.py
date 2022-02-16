class Figure:
    def __init__(self, name: str):
        if self.__class__ == Figure:
            raise Exception('Нельзя создавать экземпляры базового класса Figure')
        self.name = name

    def raise_error(self):
        raise ValueError(f'{self} - такой фигуры не существует')

    @property
    def area(self) -> float:
        raise NotImplementedError

    @property
    def perimeter(self) -> float:
        raise NotImplementedError

    def add_area(self, figure: 'Figure') -> float:
        if not isinstance(figure, Figure):
            raise ValueError(f'Некорректный класс({figure})')
        return self.area + figure.area

    @staticmethod
    def correct(a: float) -> bool:
        return a > 0
