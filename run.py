from __future__ import annotations
import fileinput
from helpers import input_parser
from position import Position
from robot import Robot


class ToySimulator:
    def __init__(self) -> None:
        self.robot: Robot = Robot()
        self.command_mapping: dict = {
            "MOVE": self.robot.move,
            "RIGHT": self.robot.right,
            "LEFT": self.robot.left,
            "REPORT": self.robot.report,
        }

    def __call__(self) -> Position:
        print("Instruct movement:")
        for line in fileinput.input():
            try:
                command, coordinates = input_parser(line)
                if command == "PLACE":
                    self.robot.place(coordinates)
                    continue
                self.command_mapping.get(command)()
                if command == "REPORT":
                    fileinput.close()
            except (ValueError, AttributeError) as exception:
                print(exception)
                fileinput.close()


if __name__ == "__main__":
    application: ToySimulator = ToySimulator()
    application()
