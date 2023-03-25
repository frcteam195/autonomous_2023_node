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


class Cube_Bump_Whack(AutoBase):
    """
    Score two game pieces on the loading side.
    """

    def __init__(self) -> None:
        super().__init__(display_name="Whack",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Bump,
                         expected_trajectory_count=4)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            MoveArmAction(Arm_Goal.PRE_DEAD_CONE, Arm_Goal.SIDE_BACK),
            self.trajectory_iterator.get_next_trajectory_action(),
            IntakeDeadCone(Arm_Goal.SIDE_BACK),
            IntakeAction(True, -1, 0.25),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT),
            StopIntakeAction(True, -1),
            self.trajectory_iterator.get_next_trajectory_action(),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT),
            ScoreConeHigh(Arm_Goal.SIDE_FRONT),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    IntakeAction(False, -1, 0.2),
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.50),
                    MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK, 5, 5)
                ])
            ]),
            StopIntakeAction(False),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT),
            self.trajectory_iterator.get_next_trajectory_action(),
            ScoreCubeMiddle(Arm_Goal.SIDE_FRONT),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT)
        ])
