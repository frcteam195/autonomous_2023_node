from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.LaunchAction import *

from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction

class Cone_Loading_ThreePiece(AutoBase):
    """
    Ahhhhhhhhhh!
    """
    def __init__(self) -> None:
        super().__init__(display_name="ThreePiece",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=3)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    MoveArmAction(Arm_Goal.GROUND_DEAD_CONE, Arm_Goal.SIDE_FRONT),
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.25),
                    IntakeAction(False, -1, 0.35),
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.5),
                    StopIntakeAction(False),
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.75),
                    MoveArmAction(Arm_Goal.MID_CUBE, Arm_Goal.SIDE_FRONT)
                ]),
            ]),
            OuttakeAction(False, 0.25),
            StopIntakeAction(False),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.5),
                    IntakeAction(False, -1, 0.2)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.MID_CONE, Arm_Goal.SIDE_FRONT),
                SeriesAction([
                    StopIntakeAction(False),
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.80),
                    LaunchAction(False, 1, 0.5),
                ])
            ])
        ])
