from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.LaunchAction import LaunchAction


from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.game_specific_actions.AutoBalanceAction import AutoBalanceAction, BalanceDirection


class Cube_Loading_TwoAndHalfPieceClimb(AutoBase):
    """
    Score two game pieces on the loading side.
    """

    def __init__(self) -> None:
        super().__init__(display_name="TwoAndHalfPieceClimb",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=3)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            MoveArmAction(Arm_Goal.LOW_SCORE, Arm_Goal.SIDE_FRONT),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    OuttakeAction(False, 0.2),
                    MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.75),
                    IntakeAction(False, 0.5, 0.2)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.LOW_SCORE, Arm_Goal.SIDE_FRONT),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.1),
                    StopIntakeAction(False),
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.95),
                    LaunchAction(False, 1.0, 0.2)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                SeriesAction([
                    StopIntakeAction(False),
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.45),
                    IntakeAction(False, 0.5, 0.2),
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.55),
                    StopIntakeAction(False),
                    MoveArmAction(Arm_Goal.SPORT_MODE, Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_ZERO, 5, 5)
                ]),

            ]),
            
            AutoBalanceAction(BalanceDirection.ROLL, 270.0)
        ])
