from autonomous_node.autos.AutoBase import AutoBase
from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction
from actions_node.default_actions.DriveTrajectoryAction import DriveTrajectoryAction
from actions_node.game_specific_actions.MoveArmAction import MoveArmAction, ArmPosition
from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *

class SampleAuto(AutoBase):
    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ParallelAction([
                DriveTrajectoryAction("correct_start", True),
                SeriesAction([
                    GroundAction(True),
                    IntakeAction(False)
                ])
            ]),
            IntakeAction(False, 0.5),
            ParallelAction([
                InRobotAction(),
                DriveTrajectoryAction("second_path")
            ]),
            ScoreCube(False),
            InRobotAction(),
            ParallelAction([
                DriveTrajectoryAction("third_path", True),
                SeriesAction([
                    GroundAction(True),
                    IntakeAction(False)
                ])
            ])
        ])