from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *

from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction

class ConeLoadingTwoPiece(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="TwoPiece",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=2)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            StopIntakeAction(True),
            ScoreConeHigh(Arm_Goal.SIDE_FRONT),
            ParallelAction([    
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CONE, Arm_Goal.SIDE_BACK),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.75),
                    IntakeAction(True)
                ])

            ]),
            ParallelAction([
                StopIntakeAction(True),
                MoveArmAction(Arm_Goal.MID_CONE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_180),
                self.trajectory_iterator.get_next_trajectory_action()
            ]),
            StopIntakeAction(False)
        ]) 
