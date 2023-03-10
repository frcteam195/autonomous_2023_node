from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction

from ck_ros_msgs_node.msg import Arm_Goal

class CubeWallTwoPiece(AutoBase):
    """
    Score two game pieces on the wall side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="TwoPiece",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Wall,
                         expected_trajectory_count=2)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            StopIntakeAction(True),
            ScoreCubeHigh(Arm_Goal.SIDE_BACK),
            ParallelAction([    
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CONE, Arm_Goal.SIDE_FRONT),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.75),
                    IntakeAction(True, 1.0)
                ])
            ]),
            ParallelAction([
                StopIntakeAction(True),
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_BACK),
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.75),
                    MoveArmAction(Arm_Goal.HIGH_CONE, Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_180)         
                ])
            ]),
            
            StopIntakeAction(False)
        ])
