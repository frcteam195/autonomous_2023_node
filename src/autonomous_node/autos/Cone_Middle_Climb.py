from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction
from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction

from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.AutoBalanceAction import AutoBalanceAction, BalanceDirection
from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.LaunchAction import LaunchAction

from ck_ros_msgs_node.msg import Arm_Goal

class Cone_Middle_Climb(AutoBase):
    """
    Scores one in Cube Node and climbs
    """
    def __init__(self) -> None:
        super().__init__(display_name="Climb",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Middle,
                         expected_trajectory_count=3)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            StopIntakeAction(True),
            ScoreConeHigh(Arm_Goal.SIDE_FRONT),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
            ParallelAction([
                MoveArmAction(Arm_Goal.SPORT_MODE, Arm_Goal.SIDE_FRONT),
                self.trajectory_iterator.get_next_trajectory_action(),
            ]),
            self.trajectory_iterator.get_next_trajectory_action(),
            WaitAction(0.3),
            self.trajectory_iterator.get_next_trajectory_action(),
            AutoBalanceAction(BalanceDirection.ROLL, 90.0)
        ])