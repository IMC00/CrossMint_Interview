import pytest

from src.AstralApiHelper import ASTRAL_API_HELPER


def test_get_board():
    try:
        ASTRAL_API_HELPER.get_astral_board()
    except:
        assert False, 'get_astral_board() raised an exception'
