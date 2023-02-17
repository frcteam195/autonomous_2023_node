from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction
from actions_node.default_actions.DriveTrajectoryAction import DriveTrajectoryAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *

class SimpleAuto(AutoBase):
    """
    Scores a game piece in the cooperatition grid, drives over the charge station, and then balances.
    """
    def __init__(self) -> None:
        super().__init__(display_name="auto",
                         game_piece=GamePiece.Null,
                         start_position=StartPosition.Null,
                         expected_trajectory_count=2)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            self.trajectory_iterator.get_next_trajectory_action(),
            self.trajectory_iterator.get_next_trajectory_action(),
        ])
