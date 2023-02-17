from enum import Enum
import typing

from abc import ABC, abstractmethod
from actions_node.default_actions.SeriesAction import SeriesAction

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
    def __init__(self) -> None:
        super().__init__()
        self.display_name: str = ""
        self.game_piece: GamePiece = GamePiece.Cone
        self.start_position: StartPosition = StartPosition.Loading
        self.trajectory_count = 0

    @abstractmethod
    def get_action(self) -> SeriesAction:
        """
        Abstract method for getting the autonomous action.
        """

    def get_unique_name(self) -> str:
        """
        Returns the unique autonomous name based on the filters and display name.
        """
        return f"{self.game_piece.name}{self.start_position.name}{self.display_name}"

    def get_trajectory_count(self) -> typing.List[str]:
        """
        Get the number of trajectories for the autonomous from the swerve trajectory node.
        """
        # TODO: Call the trajectory service to receive the associated trajectories.
        return 0
