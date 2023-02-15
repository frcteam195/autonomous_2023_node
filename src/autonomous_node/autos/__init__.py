from autonomous_node.autos.SampleAuto import SampleAuto
from autonomous_node.autos.AutoBase import AutoBase
from enum import Enum

class AutonomousNames(str, Enum):
    SampleAuto = "SampleAuto",
    Auto1 = "Auto1"




    def __str__(self) -> str:
        return str.__str__(self)




AUTONOMOUS_SELECTION_MAP = {
    AutonomousNames.SampleAuto: SampleAuto()
}