from autonomous_node.autos.AutoBase import AutoBase
from actions_node.default_actions.SeriesAction import SeriesAction
from actions_node.default_actions.DriveTrajectoryAction import DriveTrajectoryAction

class SampleAuto(AutoBase):
    def getAction(self) -> SeriesAction:
        return SeriesAction([
            DriveTrajectoryAction("correct_start", True)
        ])