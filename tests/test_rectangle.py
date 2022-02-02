from src.Rectangle import Rectangle

def test_init_rectangle():
    rectangle = Rectangle(3, 6)
    assert isinstance(rectangle, Rectangle)

def test_check_name():
    rectangle = Rectangle(3, 7)
    assert rectangle.name == 'Rectangle'

def test_check_sides():
    rectangle = Rectangle(3, 2)
    assert rectangle.a == 3
    assert rectangle.b == 2

def test_check_perimeter_rectangle():
    rectangle = Rectangle(6, 4)
    assert rectangle.perimeter == 20

def test_check_area_rectangle():
    rectangle = Rectangle(3, 7)
    assert rectangle.area == 21

def test_add_area_to_rectangle():
    first_figure = Rectangle(12, 4)
    second_figure = Rectangle(3, 8)
    assert first_figure.add_area(second_figure) == 72