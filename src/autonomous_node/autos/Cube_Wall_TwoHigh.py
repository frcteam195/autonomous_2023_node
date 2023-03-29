from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction
from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction

from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.LaunchAction import LaunchAction

from ck_ros_msgs_node.msg import Arm_Goal

class Cube_Wall_TwoHigh(AutoBase):
    """
    Score two game pieces on the wall side.
    """

    def __init__(self) -> None:
        super().__init__(display_name="TwoHigh",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Wall,
                         expected_trajectory_count=3)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
            MoveArmAction(Arm_Goal.HIGH_CUBE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
            LaunchAction(False, 0.85, 0.1),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.PRE_DEAD_CONE, Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_180)
            ]),
            IntakeDeadCone(Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_180),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                StopIntakeAction(True),
                SeriesAction([
                    MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.5),
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO)
                ])
            ]),
            ScoreConeHigh(Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO, 7, 9),
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.55),
                    MoveArmAction(Arm_Goal.PRE_DEAD_CONE, Arm_Goal.SIDE_BACK)
                ])
            ]),
            IntakeDeadCone(Arm_Goal.SIDE_BACK, Arm_Goal.WRIST_ZERO),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_ZERO, 7, 9),
            StopIntakeAction(True)
        ])
