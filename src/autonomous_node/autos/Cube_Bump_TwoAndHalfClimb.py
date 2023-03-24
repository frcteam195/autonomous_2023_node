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


class Cube_Bump_TwoAndHalfClimb(AutoBase):
    """
    Score two game pieces on the loading side.
    """

    def __init__(self) -> None:
        super().__init__(display_name="TwoAndHalfClimb",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Bump,
                         expected_trajectory_count=3)

    def get_action(self) -> SeriesAction:
        rospy.logerr("Test Run")
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            self.trajectory_iterator.get_next_trajectory_action(),
            WaitAction(2.0),
            self.trajectory_iterator.get_next_trajectory_action(),
            WaitAction(2.0),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.80),
                    MoveArmAction(Arm_Goal.SPORT_MODE, Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_ZERO, 5, 5)
                ])
            ]),
            AutoBalanceAction(BalanceDirection.ROLL, 90.0)
        ])
