import rospy
from enum import Enum
import typing

from abc import ABC, abstractmethod
from actions_node.default_actions.SeriesAction import SeriesAction
from ck_utilities_py_node.geometry import *
from actions_node.default_actions.DriveTrajectoryActionIterator import DriveTrajectoryActionIterator

class GamePiece(Enum):
    """
    Starting game pieces.
    """
    Cone = 0
    Cube = 1

class StartPosition(Enum):
    """
    General start positions on the field.
    """
    Wall = 0
    Middle = 1
    Loading = 2

class AutoBase(ABC):
    """
    Base class for all autonomous definitions.
    """
    def __init__(self, display_name : str, game_piece : GamePiece, start_position : StartPosition, expected_trajectory_count : int) -> None:
        self.display_name: str = display_name
        self.game_piece: GamePiece = game_piece
        self.start_position: StartPosition = start_position
        self.expected_trajectory_count = expected_trajectory_count
        self.trajectory_iterator : DriveTrajectoryActionIterator = DriveTrajectoryActionIterator(self.get_unique_name(), self.expected_trajectory_count)

    @abstractmethod
    def get_action(self) -> SeriesAction:
        """
        Abstract method for getting the autonomous action.
        """
        pass

    def get_unique_name(self) -> str:
        """
        Returns the unique autonomous name based on the filters and display name.
        """
        return f"{self.game_piece.name}{self.start_position.name}{self.display_name}"