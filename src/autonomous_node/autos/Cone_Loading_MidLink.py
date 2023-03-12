from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.LaunchAction import *

from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction

class ConeLoadingMidLink(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="MidLink",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=4)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT),
            ScoreConeMiddle(Arm_Goal.SIDE_FRONT),

            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    MoveArmAction(Arm_Goal.PRE_DEAD_CONE, Arm_Goal.SIDE_BACk),
                    WaitUntilPercentCompletedTrajectoryAction(0, 0.80),
                    IntakeAction(False),
                    MoveArmAction(Arm_Goal.GROUND_DEAD_CONE, Arm_Goal.SIDE_BACK),
                ]),
            ]),
            IntakeAction(True, 0.2),

            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                StopIntakeAction(True),
                SeriesAction([
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_180),
                    WaitUntilPercentCompletedTrajectoryAction(1, 0.8),
                    MoveArmAction(Arm_Goal.MID_CONE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_180),
                ])
            ]),

            ScoreConeMiddle(Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_180),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.5),
                    IntakeAction(False)
                ])
            ]),

            ParallelAction([
                StopIntakeAction(True),
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT)
            ]),
            LaunchAction(True, 1, 0.5),
            #ScoreCubeMiddle(Arm_Goal.SIDE_FRONT),
            #MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT)
        ])
