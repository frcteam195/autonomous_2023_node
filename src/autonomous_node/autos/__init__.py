from autonomous_node.autos.SampleAuto import SampleAuto
from autonomous_node.autos.SimpleAuto import SimpleAuto
from autonomous_node.autos.ToddCircle import ToddCircle
from autonomous_node.autos.CorrectStart import CorrectStart
from autonomous_node.autos.CubeMiddle1CubeBalance import CubeMiddle1CubeBalance
from autonomous_node.autos.CubeLoadingTwoPiece import CubeLoadingTwoPiece
from enum import Enum

class AutonomousNames(str, Enum):
    """
    Format must be PRELOAD_STARTINGPOSITION_ANYNAMENOTINCLUDINGAKEYWORDFORPRELOADORSTARTINGPOSITION
    """
    CubeMiddle1CubeBalance = "Cube_Middle_1CUB_Bal",
    ConeHigh1ConeBalance = "Cone_High_1CON_Bal",
    SimpleAuto = "Null_Null_auto",
    ToddCircle = "Null_Null_ToddCircle",
    CorrectStart = "Null_Null_CorrectStart"
    CubeLoadingTwoPiece = "Cube_Loading_TwoPiece"

    def __str__(self) -> str:
        return str.__str__(self)




AUTONOMOUS_SELECTION_MAP = {
    AutonomousNames.SimpleAuto: SimpleAuto(),
    AutonomousNames.CubeMiddle1CubeBalance: SimpleAuto(),    #Temporarily stop error. Make sure to put proper auto back
    AutonomousNames.ConeHigh1ConeBalance: SimpleAuto(),    #Temporarily stop error. Make sure to put proper auto back
    AutonomousNames.ToddCircle : ToddCircle(),
    AutonomousNames.CorrectStart : CorrectStart(),
    AutonomousNames.CubeLoadingTwoPiece : CubeLoadingTwoPiece()
}