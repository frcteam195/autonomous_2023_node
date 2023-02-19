from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction
from actions_node.default_actions.DriveTrajectoryAction import DriveTrajectoryAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *

class ConeHigh1ConeBalance(AutoBase):
    """
    Scores a game piece in the cooperatition grid, drives over the charge station, and then balances.
    """
    def __init__(self) -> None:
        super().__init__(display_name="Balance",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Middle,
                         expected_trajectory_count=2)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ScoreCube(False),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    GroundAction(True),
                    IntakeAction(False)
                ])
            ]),
            IntakeAction(False, 0.5),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                InRobotAction()
            ])
        ])
