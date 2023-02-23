from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *

from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction

class CubeLoadingTwoPiece(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="TwoPiece",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=2)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            ScoreCubeHigh(Arm_Goal.SIDE_BACK),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CONE, Arm_Goal.SIDE_FRONT),
                IntakeAction(True)
            ]),
            IntakeAction(True, 0.0),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectory(1, 0.5),
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_BACK)
                ])
            ]),
            ScoreConeHigh(Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_180)
        ])
