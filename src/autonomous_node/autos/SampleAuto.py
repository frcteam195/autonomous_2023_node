from autonomous_node.autos.AutoBase import AutoBase
from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction
from actions_node.default_actions.DriveTrajectoryAction import DriveTrajectoryAction
from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

class SampleAuto(AutoBase):
    def __init__(self) -> None:
        super().__init__(display_name="SampleAuto",
                         game_piece=GamePiece.Cube,
                         start_position=StartPosition.Middle,
                         expected_trajectory_count=3)

    def get_action(self) -> SeriesAction:
        return SeriesAction([

        ])