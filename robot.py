from __future__ import annotations
from copy import deepcopy
from helpers import DIRECTIONS
from position import Position


class Robot:
    def __init__(self) -> None:
        self.position: Position = None

    @property
    def coordinates(self) -> dict:
        if self.position is None:
            return {}
        return self.position.coordinates()

    def place(self, coordinates: dict) -> None:
        try:
            self.position = Position(**coordinates)
        except ValueError:
            pass

    def move(self) -> None:
        coordinates: dict = deepcopy(self.coordinates)
        if coordinates.get("f") == "NORTH":
            coordinates["y"] += 1
        elif coordinates.get("f") == "SOUTH":
            coordinates["y"] -= 1
        elif coordinates.get("f") == "EAST":
            coordinates["x"] += 1
        elif coordinates.get("f") == "WEST":
            coordinates["x"] -= 1

        self.position = Position(**coordinates)

    def right(self) -> None:
        coordinates: dict = deepcopy(self.coordinates)
        coordinates["f"]: str = DIRECTIONS[coordinates["f"]]["right"]
        self.position = Position(**coordinates)

    def left(self) -> None:
        coordinates: dict = deepcopy(self.coordinates)
        coordinates["f"]: str = DIRECTIONS[coordinates["f"]]["left"]
        self.position = Position(**coordinates)

    def report(self) -> dict:
        if self.position is not None:
            print(self.position)
            return self.position.coordinates()