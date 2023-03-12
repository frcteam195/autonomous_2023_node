from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.DriveTrajectoryAction import DriveTrajectoryAction

from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.default_actions.WaitAction import WaitAction

class Curve(AutoBase):
    """
    Drive curvy baby. Easy.
    """
    def __init__(self) -> None:
        super().__init__(display_name="Curve",
                         game_piece=GamePiece.Test,
                         start_position=StartPosition.Test,
                         expected_trajectory_count=1)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            WaitAction(2),
            self.trajectory_iterator.get_next_trajectory_action()
        ])
