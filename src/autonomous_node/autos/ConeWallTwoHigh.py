from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction
from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction

from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.AutoBalanceAction import AutoBalanceAction, BalanceDirection, RobotDirection
from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.LaunchAction import LaunchAction


from ck_ros_msgs_node.msg import Arm_Goal

class ConeWallTwoHigh(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="TwoHigh",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Wall,
                         expected_trajectory_count=4)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT),
            MoveArmAction(Arm_Goal.HIGH_CONE, Arm_Goal.SIDE_FRONT),
            StopIntakeAction(False),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_BACK)
            ]),
            self.trajectory_iterator.get_next_trajectory_action(),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
                    WaitUntilPercentCompletedTrajectoryAction(2, 0.5),
                    IntakeAction(False)
                ])
            ]),
            ParallelAction([            
                StopIntakeAction(False),
                self.trajectory_iterator.get_next_trajectory_action(),
                SeriesAction([
                    WaitUntilPercentCompletedTrajectoryAction(3, 0.4),
                    MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT),
                    WaitUntilPercentCompletedTrajectoryAction(3, 0.95),   
                    MoveArmAction(Arm_Goal.HIGH_CUBE, Arm_Goal.SIDE_FRONT),
                    LaunchAction(False, 1, 0.2)
                ])
            ]),
            MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT),
          
        ])
