from src.Triangle import Triangle
import pytest
import math

def test_init_triangle():
    triangle = Triangle(3, 4, 5)
    assert isinstance(triangle, Triangle)

def test_init_wrong_triangle():
    triangle = Triangle(7, 111, 5)
    assert triangle is None

def test_check_name():
    triangle = Triangle(3, 4, 5)
    assert triangle.name == 'Triangle'

def test_check_side():
    triangle = Triangle(3, 4, 5)
    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5


def test_check_perimeter_triangle():
    triangle = Triangle(3, 4, 2)
    assert triangle.perimeter == 9


def test_check_area_triangle():
    triangle = Triangle(3, 4, 2)
    assert triangle.area == 2.9047375096555625


def test_add_area_to_triangle():
    first_figure = Triangle(3, 4, 2)
    second_figure = Triangle(5, 6, 7)
    assert math.floor(first_figure.add_area(second_figure)) == 17
