from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction
from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from actions_node.default_actions.WaitAction import WaitAction

from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.AutoBalanceAction import AutoBalanceAction, BalanceDirection
from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.LaunchAction import LaunchAction


from ck_ros_msgs_node.msg import Arm_Goal


class ConeWallTwoHigh(AutoBase):
    """
    Score two game pieces on the loading side.
    """

    def __init__(self) -> None:
        super().__init__(display_name="TwoHigh",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Wall,
                         expected_trajectory_count=3)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT),
            MoveArmAction(Arm_Goal.HIGH_CONE, Arm_Goal.SIDE_FRONT),
            StopIntakeAction(False, 0.10),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_BACK),
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.70),
                    MoveArmAction(Arm_Goal.PRE_DEAD_CONE, Arm_Goal.SIDE_BACK)
                ])
            ]),
            self.trajectory_iterator.get_next_trajectory_action(),
            MoveArmAction(Arm_Goal.GROUND_DEAD_CONE, Arm_Goal.SIDE_BACK),
            IntakeAction(True, 0.2),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    StopIntakeAction(True),
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.4),
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT),
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.95),
                    MoveArmAction(Arm_Goal.HIGH_CUBE, Arm_Goal.SIDE_FRONT),
                    LaunchAction(True, 1, 0.2)
                ])
            ]),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT),
        ])
