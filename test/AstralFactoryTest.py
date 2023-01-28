import pytest

from src.AstralObject import Polyanet, Soloon, Cometh
from src.enumerates import Color, Direction
from src.AstralFactory import AstralFactory


@pytest.mark.parametrize("test_input,expected", [
    ([0, 0, 'POLYANET'], Polyanet(0, 0)),
    ([1, 3, 'RED_SOLOON'], Soloon(1, 3, Color.RED)),
    ([2, 2, 'RIGHT_COMETH'], Cometh(2, 2, Direction.RIGHT)),
])
def test_happy_path(test_input, expected):
    assert AstralFactory.build_astral_object(*test_input).__eq__(expected)


def test_bad_color():
    with pytest.raises(ValueError):
        AstralFactory.build_astral_object(1, 1, "POTATO_SOLOON")


def test_bad_direction():
    with pytest.raises(ValueError):
        AstralFactory.build_astral_object(1, 1, "MIDDLE_COMETH")
