from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.default_actions.SeriesAction import SeriesAction

from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.AutoBalanceAction import AutoBalanceAction, BalanceDirection, RobotDirection

class AutoBalance(AutoBase):
    """
    Tests the auto balance functionality.
    """
    def __init__(self) -> None:
        super().__init__(display_name="AutoBalance",
                         game_piece=GamePiece.Test,
                         start_position=StartPosition.Test,
                         expected_trajectory_count=1)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            AutoBalanceAction(BalanceDirection.PITCH, 1.0, RobotDirection.FRONT)
        ])
