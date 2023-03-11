from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.default_actions.ResetPoseAction import ResetPoseAction
from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from actions_node.game_specific_actions.AutoBalanceAction import * 

from ck_ros_msgs_node.msg import Arm_Goal

class ConeWallOnePiece(AutoBase):
    """
    Score one game pieces on the wall side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="OnePiece",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Wall,
                         expected_trajectory_count=2)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            StopIntakeAction(True),
            ScoreConeHigh(Arm_Goal.SIDE_BACK),
           
            ParallelAction([    
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.HOME, Arm_Goal.SIDE_FRONT),
               
            ]),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.SPORT_MODE, Arm_Goal.SIDE_BACK)
            ]),
            AutoBalanceAction(BalanceDirection.ROLL, 270.0),   
            StopIntakeAction(False)
        ])
