from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *

from ck_ros_msgs_node.msg import Arm_Goal

class CubeLoadingTwoPiece(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="TwoPiece",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=2)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ScoreCubeHigh(Arm_Goal.SIDE_BACK),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                IntakeConeGround(Arm_Goal.SIDE_FRONT)
            ]),
            IntakeAction(True, 0.5),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                MoveArmAction(Arm_Goal.HOME)
            ]),
            ScoreConeHigh(Arm_Goal.SIDE_BACK)
        ])
