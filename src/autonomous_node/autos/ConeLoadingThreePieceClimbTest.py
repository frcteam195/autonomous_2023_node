from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *

from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction

class ConeLoadingThreePieceClimbTest(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="ThreePieceClimbTest",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=5)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            #StopIntakeAction(True),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_BACK),
            ScoreConeMiddle(Arm_Goal.SIDE_BACK),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_FRONT),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.25),
                    IntakeAction(False)
                ])
            ]),
            StopIntakeAction(True),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_BACK),
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.4),
                    MoveArmAction(Arm_Goal.HIGH_CUBE, Arm_Goal.SIDE_BACK)
                ])
            ]),
            OuttakeAction(True, 0.1),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_FRONT),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.25),
                    IntakeAction(False)
                ])
            ]),
            StopIntakeAction(True),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_BACK),
                    WaitUntilPercentCompletedTrajectoryAction(3, 0.4),
                    MoveArmAction(Arm_Goal.MID_CUBE, Arm_Goal.SIDE_BACK)
                ])
            ]),
            OuttakeAction(True, 0.1),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT)
            ])
        ]) 
    
