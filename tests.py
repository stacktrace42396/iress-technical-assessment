from __future__ import annotations
import pytest
from helpers import input_parser
from position import Position
from robot import Robot


class TestHelper:
    @pytest.mark.parametrize(
        ("line", "expected_command", "expected_coordinates"),
        (
            ("PLACE 0,0,NORTH", "PLACE", {"x": 0, "y": 0, "f": "NORTH"}), 
            ("PLACE 1,2,EAST", "PLACE", {"x": 1, "y": 2, "f": "EAST"}) ,
            ("PLACE 2,2,SOUTH", "PLACE", {"x": 2, "y": 2, "f": "SOUTH"}), 
        ),
    )
    def test_sucess_cases(self, line, expected_command, expected_coordinates):
        command, coordinates = input_parser(line)
        assert expected_command == command
        assert expected_coordinates == coordinates

    @pytest.mark.parametrize(
        ("line"), ("INVALID", "PLACE 1,2,3,4", "PLACE 1,2,99")
    )
    def test_failure_cases(self, line):
        with pytest.raises(ValueError):
            input_parser(line)


class TestPosition:
    @pytest.mark.parametrize(
        ("x", "y", "f"),
        (
            (0, 2, "NORTH"),
            (1, 3, "SOUTH"),
            (2, 0, "EAST"),
            (3, 1, "WEST"),
        )
    )
    def test_success_cases(self, x, y, f):
        coordinates: dict = {"x": x, "y": y, "f": f}
        position: Position = Position(**coordinates)
        assert coordinates["x"] == position.x
        assert coordinates["y"] == position.y
        assert coordinates["f"] == position.f
        assert coordinates == position.coordinates()

    @pytest.mark.parametrize(
        ("x", "y", "f"),
        (
            (5, 1, "NORTH"),
            (1, 5, "SOUTH"),
            (5, 5, "EAST"),
            (1, 1, "WESTEROS"),
        )
    )
    def test_failure_cases(self, x, y, f):
        coordinates: dict = {"x": x, "y": y, "f": f}
        with pytest.raises(ValueError):
            Position(**coordinates)


class TestRobot:
    @pytest.mark.parametrize(
        ("coordinates", "movements", "expected_output"),
        (
            (
                {"x": 0, "y": 0, "f": "NORTH"},
                ["MOVE"],
                {"x": 0, "y": 1, "f": "NORTH"}
            ),
            (
                {"x": 0, "y": 0, "f": "NORTH"},
                ["LEFT"],
                {"x": 0, "y": 0, "f": "WEST"}
            ),
            (
                {"x": 1, "y": 2, "f": "EAST"},
                ["MOVE", "MOVE", "LEFT", "MOVE"],
                {"x": 3, "y": 3, "f": "NORTH"}
            ),
        ),
    )
    def test_success_cases(self, coordinates, movements, expected_output):
        robot: Robot = Robot()
        robot.place(coordinates=coordinates)
        for move in movements:
            getattr(robot, move.lower())()
        assert expected_output == robot.report()
