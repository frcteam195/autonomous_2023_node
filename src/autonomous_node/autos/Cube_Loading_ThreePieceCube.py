from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.LaunchAction import *

from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction

class Cube_Loading_ThreePieceCube(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="ThreePieceCube",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=4)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            MoveArmAction(Arm_Goal.CUBE_PUSH_AUTO, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                SeriesAction([
                    StopIntakeAction(False),
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.50),
                    IntakeAction(False, -1, 0.35)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.MID_CUBE_AUTO, Arm_Goal.SIDE_FRONT),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.03),
                    StopIntakeAction(False),
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.85),
                    LaunchAction(False, 0.20, 0.2)
                ])
            ]),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO, 5, 5),
            ParallelAction([
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.1),
                    StopIntakeAction(False),
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.50),
                    IntakeAction(False, -1, 0.35)
                ])
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(3, 0.07),
                    StopIntakeAction(False),
                ]),
                SeriesAction([
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_90),
                    WaitUntilPercentCompletedTrajectoryAction(3, 0.70),
                    MoveArmAction(Arm_Goal.HIGH_CUBE_AUTO, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_90),
                    WaitUntilPercentCompletedTrajectoryAction(3, 0.98),
                    LaunchAction(False, 0.20, 0.2)

                ])  
            ]),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO, 4, 4),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT)
        ])
