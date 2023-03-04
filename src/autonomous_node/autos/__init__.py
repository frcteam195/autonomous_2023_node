from enum import Enum

from autonomous_node.autos.AutoBalance import AutoBalance
from autonomous_node.autos.CubeLoadingThreePiece import CubeLoadingThreePiece
from autonomous_node.autos.ConeLoadingThreePieceClimb import ConeLoadingThreePieceClimb
from autonomous_node.autos.ConeLoadingThreePiece import ConeLoadingThreePiece
from autonomous_node.autos.ConeLoadingThreePieceClimbTest import ConeLoadingThreePieceClimbTest
from autonomous_node.autos.ConeLoadingThreePieceMidLink import ConeLoadingThreePieceMidLink
from autonomous_node.autos.Cone_Loading_TwoPieceClimb import ConeLoadingTwoPieceClimb
from autonomous_node.autos.Cube_Bump_FiveScore import Cube_Bump_FiveScore
from autonomous_node.autos.CubeLoadingThreePieceMidLink import CubeLoadingThreePieceMidLink
from autonomous_node.autos.CubeWallThreePiece import CubeWallThreePiece

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
    #Cube_Bump_FiveScore = "Cube_Bump_FiveScore"
    CubeLoadingThreePieceMidLink = "Cube_Loading_ThreePieceMidLink"
    CubeWallThreePiece = "Cube_Wall_ThreePiece"

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
        #AutonomousNames.Cube_Bump_FiveScore: Cube_Bump_FiveScore(),
        AutonomousNames.CubeLoadingThreePieceMidLink: CubeLoadingThreePieceMidLink(),
        AutonomousNames.CubeWallThreePiece: CubeWallThreePiece()

    }
