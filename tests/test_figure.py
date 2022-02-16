import pytest

from src.Figure import Figure
from src.Circle import Circle
from src.Square import Square

def test_init_figure():
    with pytest.raises(Exception):
        figure = Figure('Фигура')

def test_add_area():
    circle = Circle(6)
    square = Square(4)
    assert circle.add_area(square) == 129.09733552923257
    assert square.add_area(circle) == 129.09733552923257
