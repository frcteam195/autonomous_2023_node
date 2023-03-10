from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction
from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction

from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.StopIntakeAction import StopIntakeAction

from ck_ros_msgs_node.msg import Arm_Goal

class CubeLoadingThreePiece(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="ThreePiece",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=4)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            ScoreCubeHigh(Arm_Goal.SIDE_BACK),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CONE, Arm_Goal.SIDE_FRONT),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.25),
                    IntakeAction(True)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    WaitAction(0.5),
                    StopIntakeAction(True),
                ]),
                SeriesAction([
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_BACK),
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.55),
                    MoveArmAction(Arm_Goal.MID_CONE, Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_180)
                ])
            ]),
            StopIntakeAction(False),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_FRONT),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.50),
                    IntakeAction(False)
                ]),
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    WaitAction(0.5),
                    StopIntakeAction(True)
                ]),
            ]),
            SeriesAction([
                MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_BACK),
                WaitUntilPercentCompletedTrajectoryAction(3, 0.55),
                MoveArmAction(Arm_Goal.MID_CUBE, Arm_Goal.SIDE_BACK)
            ])
        ])
