from enum import Enum

from autonomous_node.autos.AutoBalance import AutoBalance
from autonomous_node.autos.CubeLoadingThreePiece import CubeLoadingThreePiece
from autonomous_node.autos.ConeLoadingThreePieceClimb import ConeLoadingThreePieceClimb
from autonomous_node.autos.ConeLoadingThreePiece import ConeLoadingThreePiece
from autonomous_node.autos.ConeLoadingThreePieceClimbTest import ConeLoadingThreePieceClimbTest
from autonomous_node.autos.ConeLoadingThreePieceMidLink import ConeLoadingThreePieceMidLink
from autonomous_node.autos.Cone_Loading_TwoPieceClimb import ConeLoadingTwoPieceClimb
from autonomous_node.autos.Cone_Loading_2MidClimb import ConeLoading2MidClimb
from autonomous_node.autos.CubeLoadingThreePieceMidLink import CubeLoadingThreePieceMidLink
from autonomous_node.autos.CubeWallThreePiece import CubeWallThreePiece
from autonomous_node.autos.Cone_Wall_OneAndHalfMidClimb import ConeWallOneAndHalfMidClimb
from autonomous_node.autos.Cone_Loading_MidLink import ConeLoadingMidLink
from autonomous_node.autos.Cube_Loading_TwoAndHalfPieceClimb import CubeLoadingTwoAndHalfPieceClimb
from autonomous_node.autos.ConeWallTwoHigh import ConeWallTwoHigh
from autonomous_node.autos.CubeWallTwoHigh import CubeWallTwoHigh
from autonomous_node.autos.CubeMiddleOnePieceClimb import CubeMiddleOnePieceClimb
from autonomous_node.autos.ConeMiddleOnePieceClimb import ConeMiddleOnePieceClimb
class AutonomousNames(str, Enum):
    """
    Format must be PRELOAD_STARTINGPOSITION_ANYNAMENOTINCLUDINGAKEYWORDFORPRELOADORSTARTINGPOSITION
    """
    AutoBalance = "Test_Test_AutoBalance"
    CubeLoadingThreePiece = "Cube_Loading_ThreePiece"
    ConeLoadingThreePieceClimb = "Cone_Loading_ThreePieceClimb"
    ConeLoadingThreePiece = "Cone_Loading_ThreePiece"
    ConeLoadingThreePieceClimbTest = "Cone_Loading_ThreePieceClimb_Test"
    ConeLoadingThreePieceMidLink = "Cone_Loading_ThreePieceMidLink"
    ConeLoadingTwoPieceClimb = "Cone_Loading_TwoPieceClimb"
    ConeLoading2MidClimb = "Cone_Loading_2MidClimb"
    CubeWallThreePiece = "Cube_Wall_ThreePiece"
    ConeWallOneAndHalfMidClimb = "Cone_Wall_OneAndHalfMidClimb"
    CubeLoadingTwoAndHalfPieceClimb = "Cube_Loading_TwoAndHalfPieceClimb"
    CubeLoadingThreePieceMidLink = "Cube_Loading_ThreePieceMidLink"
    ConeLoadingMidLink ="Cone_Loading_MidLink"
    ConeWallTwoHigh = "Cone_Wall_TwoHigh"
    CubeWallTwoHigh = "Cube_Wall_TwoHigh"
    CubeMiddleOnePieceClimb = "Cube_Middle_OnePieceClimb"
    ConeMiddleOnePieceClimb = "Cone_Middle_OnePieceClimb"


    def __str__(self) -> str:
        return str.__str__(self)


AUTONOMOUS_SELECTION_MAP = {}

def init_auto_selection_map():
    return {
        AutonomousNames.AutoBalance: AutoBalance(),
        AutonomousNames.CubeLoadingThreePiece: CubeLoadingThreePiece(),
        AutonomousNames.ConeLoadingThreePieceClimb: ConeLoadingThreePieceClimb(),
        AutonomousNames.ConeLoadingThreePiece: ConeLoadingThreePiece(),
        AutonomousNames.ConeLoadingThreePieceClimbTest: ConeLoadingThreePieceClimbTest(),
        AutonomousNames.ConeLoadingThreePieceMidLink: ConeLoadingThreePieceMidLink(),
        AutonomousNames.ConeLoadingTwoPieceClimb: ConeLoadingTwoPieceClimb(),
        AutonomousNames.ConeLoading2MidClimb: ConeLoading2MidClimb(),
        AutonomousNames.CubeLoadingThreePieceMidLink: CubeLoadingThreePieceMidLink(),
        AutonomousNames.CubeWallThreePiece: CubeWallThreePiece(),
        AutonomousNames.ConeWallOneAndHalfMidClimb: ConeWallOneAndHalfMidClimb(),
        AutonomousNames.ConeLoadingMidLink: ConeLoadingMidLink(),
        AutonomousNames.CubeLoadingTwoAndHalfPieceClimb: CubeLoadingTwoAndHalfPieceClimb(),
        AutonomousNames.ConeWallTwoHigh: ConeWallTwoHigh(),
        AutonomousNames.CubeWallTwoHigh: CubeWallTwoHigh(),
        AutonomousNames.CubeMiddleOnePieceClimb: CubeMiddleOnePieceClimb(),
        AutonomousNames.ConeMiddleOnePieceClimb: ConeMiddleOnePieceClimb()
    }
