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


class Cube_Bump_TwoPieceClimb(AutoBase):
    """
    Score two game pieces on the loading side.
    """

    def __init__(self) -> None:
        super().__init__(display_name="TwoPieceClimb",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Bump,
                         expected_trajectory_count=3)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            ##MoveArmAction(Arm_Goal.CUBE_PUSH_HARD_AUTO, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
            ParallelAction([
                StopIntakeAction(False, -1),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_90, 5, 5),
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.40),
                    IntakeAction(False, -1, 0.2),
                ])
            ]),
            StopIntakeAction(False),
            ParallelAction([
                MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_90),
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.65),
                    MoveArmAction(Arm_Goal.MID_CUBE_AUTO, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_90)
                ])
            ]),
            LaunchAction(False, 0.21, 0.2),
            ParallelAction([
                StopIntakeAction(False),
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.SPORT_MODE, Arm_Goal.SIDE_FRONT)
            ]),
            WaitAction(0.35),
            AutoBalanceAction(BalanceDirection.ROLL, -90.0)
        ])
