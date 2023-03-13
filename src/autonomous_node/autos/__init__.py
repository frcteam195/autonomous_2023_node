from enum import Enum

from autonomous_node.autos.AutoBalance import AutoBalance
from autonomous_node.autos.Cone_Loading_2MidClimb import ConeLoading2MidClimb
from autonomous_node.autos.Cone_Wall_OneAndHalfMidClimb import ConeWallOneAndHalfMidClimb
from autonomous_node.autos.Cone_Loading_MidLink import ConeLoadingMidLink
from autonomous_node.autos.Cube_Loading_TwoAndHalfPieceClimb import CubeLoadingTwoAndHalfPieceClimb
from autonomous_node.autos.ConeWallTwoHigh import ConeWallTwoHigh
from autonomous_node.autos.CubeWallTwoHigh import CubeWallTwoHigh
from autonomous_node.autos.CubeMiddleOnePieceClimb import CubeMiddleOnePieceClimb
from autonomous_node.autos.ConeMiddleOnePieceClimb import ConeMiddleOnePieceClimb
from autonomous_node.autos.StraightLine import StraightLine
from autonomous_node.autos.Curve import Curve

class AutonomousNames(str, Enum):
    """
    Format must be PRELOAD_STARTINGPOSITION_ANYNAMENOTINCLUDINGAKEYWORDFORPRELOADORSTARTINGPOSITION
    """
    AutoBalance = "Test_Test_AutoBalance"
    ConeLoading2MidClimb = "Cone_Loading_2MidClimb"
    ConeWallOneAndHalfMidClimb = "Cone_Wall_OneAndHalfMidClimb"
    CubeLoadingTwoAndHalfPieceClimb = "Cube_Loading_TwoAndHalfPieceClimb"
    ConeLoadingMidLink ="Cone_Loading_MidLink"
    ConeWallTwoHigh = "Cone_Wall_TwoHigh"
    CubeWallTwoHigh = "Cube_Wall_TwoHigh"
    CubeMiddleOnePieceClimb = "Cube_Middle_OnePieceClimb"
    ConeMiddleOnePieceClimb = "Cone_Middle_OnePieceClimb"
    StraightLine = "Test_Test_StraightLine"
    Curve = "Test_Test_Curve"


    def __str__(self) -> str:
        return str.__str__(self)


AUTONOMOUS_SELECTION_MAP = {}

def init_auto_selection_map():
    return {
        AutonomousNames.AutoBalance: AutoBalance(),
        AutonomousNames.ConeLoading2MidClimb: ConeLoading2MidClimb(),
        AutonomousNames.ConeWallOneAndHalfMidClimb: ConeWallOneAndHalfMidClimb(),
        AutonomousNames.ConeLoadingMidLink: ConeLoadingMidLink(),
        AutonomousNames.CubeLoadingTwoAndHalfPieceClimb: CubeLoadingTwoAndHalfPieceClimb(),
        AutonomousNames.ConeWallTwoHigh: ConeWallTwoHigh(),
        AutonomousNames.CubeWallTwoHigh: CubeWallTwoHigh(),
        AutonomousNames.CubeMiddleOnePieceClimb: CubeMiddleOnePieceClimb(),
        AutonomousNames.ConeMiddleOnePieceClimb: ConeMiddleOnePieceClimb(),
        AutonomousNames.StraightLine: StraightLine(),
        AutonomousNames.Curve: Curve()
    }
