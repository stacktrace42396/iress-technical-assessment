from __future__ import annotations
from re import compile, Match

DIRECTIONS: dict = {
    "NORTH": {"left": "WEST", "right": "EAST"},
    "SOUTH": {"left": "EAST", "right": "WEST"},
    "EAST": {"left": "NORTH", "right": "SOUTH"},
    "WEST": {"left": "SOUTH", "right": "NORTH"},
}
COMMANDS: list = ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]
PATTERN: str = r"(?P<X>\d+),(?P<Y>\d+),(?P<F>NORTH|EAST|WEST|SOUTH)"


def input_parser(line: str) -> tuple[str, dict]:
    arguments: list = line.strip().split()
    command: str = arguments[0]
    coordinates: dict = {}
    if command not in COMMANDS:
        raise ValueError("Invalid command.")

    if command == "PLACE" and not len(arguments) < 2:
        match: Match = compile(PATTERN).match(arguments[-1])
        if not match:
            raise ValueError("Invalid command.")
        coordinates.update(
            {"x": int(match["X"]), "y": int(match["Y"]), "f": match["F"]}
        )

    return command, coordinates
