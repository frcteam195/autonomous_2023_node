from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction
from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction

from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.AutoBalanceAction import AutoBalanceAction, BalanceDirection
from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.LaunchAction import LaunchAction
from actions_node.game_specific_actions.MoveArmAction import MoveArmAction

from ck_ros_msgs_node.msg import Arm_Goal

class Cone_Loading_TwoHighClimbWhack(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="TwoHighClimbWhack",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=1)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            ScoreConeHigh(Arm_Goal.SIDE_FRONT),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT),
            WaitAction(0.25),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_FRONT),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.40),
                    IntakeAction(False, -1, 0.2),
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.50),
                    StopIntakeAction(False),
                    MoveArmAction(Arm_Goal.HIGH_CUBE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.75),
                    LaunchAction(False, 0.5, 0.2),
                    WaitUntilPercentCompletedTrajectoryAction(0,80),
                    StopIntakeAction(False),
                    MoveArmAction(Arm_Goal.SPORT_MODE, Arm_Goal.SIDE_FRONT),
                ])
            ]),
            AutoBalanceAction(BalanceDirection.ROLL, 90.0)           
        ])