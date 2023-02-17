from autonomous_node.autos.SampleAuto import SampleAuto
from autonomous_node.autos.SimpleAuto import SimpleAuto
from autonomous_node.autos.CubeMiddleBalance import CubeMiddleBalance
from autonomous_node.autos.AutoBase import AutoBase
from enum import Enum

class AutonomousNames(str, Enum):
    CubeMiddleBalance = "Cube_Middle_Balance",
    SimpleAuto = "Null_Null_auto"




    def __str__(self) -> str:
        return str.__str__(self)




AUTONOMOUS_SELECTION_MAP = {
    AutonomousNames.SimpleAuto: SimpleAuto(),
    AutonomousNames.CubeMiddleBalance: CubeMiddleBalance()
}