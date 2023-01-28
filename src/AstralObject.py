from abc import ABC, abstractmethod
from requests import Response

from src.AstralApiHelper import ASTRAL_API_HELPER
from src.enumerates import Color, Direction, HTTPStatusCode


class AstralObject(ABC):

    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    @property
    @abstractmethod
    def api_suffix(self) -> str:
        ...

    def get_properties(self) -> dict:
        return {
            'row': self.row,
            'column': self.column
        }

    def create(self) -> Response:
        return ASTRAL_API_HELPER.api_call(HTTPStatusCode.POST, self.api_suffix, self.get_properties())

    def delete(self) -> Response:
        return ASTRAL_API_HELPER.api_call(HTTPStatusCode.DELETE, self.api_suffix, self.get_properties())

    def __str__(self) -> str:
        return self.__dict__.__str__()


class Polyanet(AstralObject):

    def __init__(self, row: int, column: int):
        super().__init__(row, column)

    @property
    def api_suffix(self) -> str:
        return "/polyanets"


class Soloon(AstralObject):

    def __init__(self, row: int, column: int, color: Color):
        super().__init__(row, column)
        self.color = color

    @property
    def api_suffix(self) -> str:
        return "/soloons"

    def get_properties(self):
        properties = super().get_properties()
        properties.update({
            'color': self.color
        })
        return properties


class Cometh(AstralObject):

    def __init__(self, row: int, column: int, direction: Direction):
        super().__init__(row, column)
        self.direction = direction

    @property
    def api_suffix(self) -> str:
        return "/comeths"

    def get_properties(self):
        properties = super().get_properties()
        properties.update({
            'direction': self.direction
        })
        return properties
