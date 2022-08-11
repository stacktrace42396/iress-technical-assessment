from __future__ import annotations
from dataclasses import dataclass, asdict

DIRECTIONS: list[str] = ["NORTH", "EAST", "WEST", "SOUTH"]
DIMENSIONS: list[int] = list(range(5))


@dataclass
class Position:
    x: int
    y: int
    f: str

    def __post_init__(self) -> None:
        if (
            self.x not in DIMENSIONS
            or self.y not in DIMENSIONS
            or self.f not in DIRECTIONS
        ):
            raise ValueError("Invalid position.")

    def coordinates(self) -> dict:
        return asdict(self)
