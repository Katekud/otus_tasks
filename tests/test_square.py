from src.Square import Square

def test_init_square():
    square = Square(5)
    assert isinstance(square, Square)

def test_check_name():
    square = Square(5)
    assert square.name == 'Square'

def test_check_side():
    square = Square(5)
    assert square.a == 5

def test_check_perimeter_square():
    square = Square(5)
    assert square.perimeter == 20

def test_check_area_square():
    square = Square(5)
    assert square.area == 25

def test_add_area_to_square():
    first_figure = Square(5)
    second_figure = Square(4)
    assert first_figure.add_area(second_figure) == 41