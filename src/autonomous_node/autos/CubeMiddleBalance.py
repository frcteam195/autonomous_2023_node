from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction
from actions_node.default_actions.DriveTrajectoryAction import DriveTrajectoryAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *

class CubeMiddleBalance(AutoBase):
    """
    Scores a game piece in the cooperatition grid, drives over the charge station, and then balances.
    """
    def __init__(self) -> None:
        super().__init__()

        self.display_name = "Balance"
        self.game_piece = GamePiece.Cube
        self.start_position = StartPosition.Middle
        self.trajectory_count = 2

    def get_action(self) -> SeriesAction:
        if self.trajectory_count != self.get_trajectory_count():
            pass

        return SeriesAction([
            ScoreCube(False),
            ParallelAction([
                DriveTrajectoryAction(self.get_unique_name(), 0, True),
                SeriesAction([
                    GroundAction(True),
                    IntakeAction(False)
                ])
            ]),
            IntakeAction(False, 0.5),
            ParallelAction([
                DriveTrajectoryAction(self.get_unique_name(), 1, True),
                InRobotAction()
            ])
        ])
