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

class ConeWallOneAndHalfClimb(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="OneAndHalfClimb",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Wall,
                         expected_trajectory_count=23)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            ScoreConeHigh(Arm_Goal.SIDE_FRONT),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.PRE_DEAD_CONE, Arm_Goal.SIDE_BACK)
            ]),
            IntakeDeadCone(Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_ZERO),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.SPORT_MODE, Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_ZERO),
                SeriesAction([
                    IntakeAction(True),
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.5),
                    StopIntakeAction(True)
                ])
            ]),
            AutoBalanceAction(BalanceDirection.ROLL, 270)
        ])
