from enum import StrEnum


class Color(StrEnum):
    BLUE = "blue"
    RED = "red"
    PURPLE = "purple"
    WHITE = "white"


class Direction(StrEnum):
    UP = "up"
    DOWN = "down"
    RIGHT = "right"
    LEFT = "left"


class HTTPStatusCode(StrEnum):
    POST = "POST"
    DELETE = "DELETE"
    GET = "GET"
