import requests

from src.AstralApiHelper import ASTRAL_API_HELPER
from src.AstralFactory import AstralFactory

my_candidate_id = "2cec4c2a-c75f-4275-b16e-fd9a605aaeb4";

if __name__ == '__main__':
    board = ASTRAL_API_HELPER.get_astral_board()
    for row_number, row in enumerate(board["goal"]):
        for column_number, elem in enumerate(row):
            elem: str
            astral_obj = AstralFactory.build_astral_object(row_number, column_number, elem)
            if astral_obj:
                astral_obj.create()
                print('CREATED: ', astral_obj)

