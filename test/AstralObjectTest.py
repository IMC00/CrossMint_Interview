import pytest

from src.AstralObject import AstralObject
from src.enumerates import Color, Direction
from test.samples import SAMPLE_ASTRAL_LIST


@pytest.mark.parametrize("test_input", SAMPLE_ASTRAL_LIST)
def test_astral_creation(test_input: AstralObject):
    assert test_input.create().status_code == 200
    assert test_input.delete().status_code == 200


expected_results = [
    {'row': 0, 'column': 0},
    {'row': 1, 'column': 3, 'color': Color.RED},
    {'row': 2, 'column': 2, 'direction': Direction.RIGHT}
]


@pytest.mark.parametrize("test_input,expected", zip(SAMPLE_ASTRAL_LIST, expected_results))
def test_astral_properties(test_input: AstralObject, expected: dict):
    print(test_input.get_properties(), expected)
    assert test_input.get_properties().__eq__(expected)
