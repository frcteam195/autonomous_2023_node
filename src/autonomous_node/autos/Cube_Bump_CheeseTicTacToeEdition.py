from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

import rospy

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.LaunchAction import LaunchAction


from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.game_specific_actions.AutoBalanceAction import AutoBalanceAction, BalanceDirection


class Cube_Bump_CheeseTicTacToeEdition(AutoBase):
    """
    Score three game pieces on the wall side.
    """

    def __init__(self) -> None:
        super().__init__(display_name="CheeseTicTacToeEdition",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Bump,
                         expected_trajectory_count=4)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.PRE_DEAD_CONE, Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_ZERO)
            ]),
            IntakeDeadCone(Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_ZERO),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
            self.trajectory_iterator.get_next_trajectory_action(),
            ScoreConeMiddle(Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
            MoveArmAction(Arm_Goal.PRE_DEAD_CONE, Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_ZERO),
            self.trajectory_iterator.get_next_trajectory_action(),
            IntakeDeadCone(Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_ZERO),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                WaitUntilPercentCompletedTrajectoryAction(3, 0.8),
                MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO)
            ]),
            ScoreConeHigh(Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
        ])