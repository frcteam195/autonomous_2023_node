from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *

from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.game_specific_actions.AutoBalanceAction import AutoBalanceAction, BalanceDirection

class ConeLoadingTwoPieceClimb(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="TwoPieceClimb",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=3)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_BACK),
            ScoreConeMiddle(Arm_Goal.SIDE_BACK),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_FRONT),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.5),
                    IntakeAction(False)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                StopIntakeAction(False),
                SeriesAction([
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_BACK),
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.85),
                    MoveArmAction(Arm_Goal.MID_CUBE, Arm_Goal.SIDE_BACK)
                ])
            ]),
            OuttakeAction(False, 0.1),
            StopIntakeAction(False),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT)
            ]),
            AutoBalanceAction(BalanceDirection.PITCH, 3)
        ]) 

    
