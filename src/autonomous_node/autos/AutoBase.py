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
    Test = 0
    Cone = 1
    Cube = 2

class StartPosition(Enum):
    """
    General start positions on the field.
    """
    Test = 0
    Wall = 1
    Middle = 2
    Loading = 3

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
        return f"{self.game_piece.name}_{self.start_position.name}_{self.display_name}"
    
    def reset(self):
        self.trajectory_iterator.reset_iterator()