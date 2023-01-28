from src.AstralObject import Polyanet, Soloon, Cometh, AstralObject
from src.enumerates import Color, Direction


class AstralFactory:

    @staticmethod
    def __build_polyanet__(row, column) -> Polyanet:
        return Polyanet(row, column)

    @staticmethod
    def __build_soloon__(row, column, color) -> Soloon:
        return Soloon(row, column, Color(color.lower()))

    @staticmethod
    def __build_cometh__(row, column, direction) -> Cometh:
        return Cometh(row, column, Direction(direction.lower()))

    @staticmethod
    def build_astral_object(row: int, column: int, name: str) -> AstralObject | None:
        astral_object_properties: list[str] = name.split("_")
        astral_object = None
        if astral_object_properties[-1] == "POLYANET":
            astral_object = AstralFactory.__build_polyanet__(row, column)
        if astral_object_properties[-1] == "SOLOON":
            astral_object = AstralFactory.__build_soloon__(row, column, astral_object_properties[-2])
        if astral_object_properties[-1] == "COMETH":
            astral_object = AstralFactory.__build_cometh__(row, column, astral_object_properties[-2])

        return astral_object
