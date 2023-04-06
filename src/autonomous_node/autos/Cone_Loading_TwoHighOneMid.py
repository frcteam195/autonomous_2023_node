from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.LaunchAction import *

from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction

class Cone_Loading_TwoHighOneMid(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="TwoHighOneMid",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=4)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            ScoreConeHigh(Arm_Goal.SIDE_FRONT),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO, 7, 7),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO, 7, 9),
                    MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                ]),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.70),
                    IntakeAction(False, -1, 0.25)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.15),
                    StopIntakeAction(False),
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.85),
                    LaunchAction(False, 0.12, 0.2)
                ])
            ]),
            ParallelAction([
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.1),
                    StopIntakeAction(False),
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.75),
                    IntakeAction(False, -1, 0.25)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    StopIntakeAction(False),
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT),
                    WaitUntilPercentCompletedTrajectoryAction(3, 0.70),
                    MoveArmAction(Arm_Goal.HIGH_CUBE, Arm_Goal.SIDE_FRONT),
                    WaitUntilPercentCompletedTrajectoryAction(3, 0.98),
                    LaunchAction(False, 0.45, 0.2)

                ])  
            ]),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO, 7, 7),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT)
        ])
