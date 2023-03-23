from actions_node.default_actions.WaitUntilPercentCompletedTrajectoryAction import WaitUntilPercentCompletedTrajectoryAction
from autonomous_node.autos.AutoBase import AutoBase, GamePiece, StartPosition

from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.ParallelAction import ParallelAction

from actions_node.game_specific_actions.IntakeAction import IntakeAction
from actions_node.game_specific_actions.AutomatedActions import *
from actions_node.game_specific_actions.LaunchAction import *

from ck_ros_msgs_node.msg import Arm_Goal
from actions_node.default_actions.ResetPoseAction import ResetPoseAction

class Cube_Loading_ExperimentalMidLink(AutoBase):
    """
    Score two game pieces on the loading side.
    """
    def __init__(self) -> None:
        super().__init__(display_name="ExperimentalMidLink",
                         game_piece=GamePiece.Cone,
                         start_position=StartPosition.Loading,
                         expected_trajectory_count=1)

    def get_action(self) -> SeriesAction:
        return SeriesAction([
            ResetPoseAction(self.get_unique_name()),
            #ScoreConeMiddle(Arm_Goal.SIDE_FRONT),
            ParallelAction([
                self.trajectory_iterator.get_next_trajectory_action(),
                #SeriesAction([
                 #   MoveArmAction(Arm_Goal.PRE_DEAD_CONE, Arm_Goal.SIDE_BACK),

                  #  WaitUntilPercentCompletedTrajectoryAction(0, 0.15),
                   # IntakeDeadCone(Arm_Goal.SIDE_BACK, 0),
                    #StopIntakeAction(True),
                    #MoveArmAction(Arm_Goal.PRE_SCORE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_180),

#                    WaitUntilPercentCompletedTrajectoryAction(0, 0.45),
 #                   MoveArmAction(Arm_Goal.MID_CONE, Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_180),
  #                  ScoreConeMiddle(Arm_Goal.SIDE_FRONT, Arm_Goal.WRIST_180),
   #                 MoveArmAction(Arm_Goal.GROUND_CUBE, Arm_Goal.SIDE_BACK),
#
 #                   WaitUntilPercentCompletedTrajectoryAction(0, 0.65),
  #                  IntakeAction(False, -1, 0.2),
   #                 StopIntakeAction(True),
    ##                MoveArmAction(Arm_Goal.MID_CONE, Arm_Goal.SIDE_FRONT),
#
 #                   WaitUntilPercentCompletedTrajectoryAction(0, 0.90),
  #                  LaunchAction(True, 1, 0.5),
   #             ]),
            ]),

        self.trajectory_iterator.get_next_trajectory_action(),
        ])
