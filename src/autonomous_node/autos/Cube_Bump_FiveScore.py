from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *

from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.game_specific_actions.AutoBalanceAction import AutoBalanceAction, BalanceDirection

class Cube_Bump_FiveScore(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="FiveScore",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Bump,
                         expected_trajectory_count=8)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT),
            OuttakeAction(False, 0.4),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.1),
                    IntakeAction(False)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                StopIntakeAction(False),
                MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT)
            ]),
            OuttakeAction(False, 0.4),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.1),
                    IntakeAction(False)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                StopIntakeAction(False),
                MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT)
            ]),
            OuttakeAction(False, 0.4),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(4, 0.1),
                    IntakeAction(False)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                StopIntakeAction(False),
                MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT)
            ]),
            OuttakeAction(False, 0.4),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(6, 0.1),
                    IntakeAction(False)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                StopIntakeAction(False),
                MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT)
            ]),
            OuttakeAction(False, 0.4),
        ])
    
