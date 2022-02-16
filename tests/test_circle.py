from src.Circle import Circle
from math import pi

def test_init_circle():
    circle = Circle(7)
    assert isinstance(circle, Circle)

def test_check_name():
    circle = Circle(7)
    assert circle.name == 'Circle'

def test_check_radius():
    circle = Circle(7)
    assert circle.radius == 7

def test_check_perimeter_circle():
    circle = Circle(7)
    assert circle.perimeter == 2 * pi * 7

def test_check_area_circle():
    circle = Circle(5)
    assert circle.area == pi * 5 ** 2

def test_add_area_to_circle():
    first_figure = Circle(13)
    second_figure = Circle(2)
    assert first_figure.add_area(second_figure) == 543.4955290710342
