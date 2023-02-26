from enum import Enum

from autonomous_node.autos.SimpleAuto import SimpleAuto
from autonomous_node.autos.ToddCircle import ToddCircle
from autonomous_node.autos.CorrectStart import CorrectStart
from autonomous_node.autos.CubeLoadingThreePiece import CubeLoadingThreePiece
from autonomous_node.autos.CubeMiddleOnePieceClimb import CubeMiddleOnePieceClimb
from autonomous_node.autos.CubeWallTwoPiece import CubeWallTwoPiece
from autonomous_node.autos.ConeLoadingTwoPiece import ConeLoadingTwoPiece
from autonomous_node.autos.ConeLoadingThreePieceClimb import ConeLoadingThreePieceClimb
from autonomous_node.autos.ConeLoadingThreePieceMiddle import ConeLoadingThreePieceMiddle
from autonomous_node.autos.ConeLoadingThreePiece import ConeLoadingThreePiece

class AutonomousNames(str, Enum):
    """
    Format must be PRELOAD_STARTINGPOSITION_ANYNAMENOTINCLUDINGAKEYWORDFORPRELOADORSTARTINGPOSITION
    """
    SimpleAuto = "Test_Test_Auto"
    ToddCircle = "Test_Test_ToddCircle"
    CorrectStart = "Test_Test_CorrectStart"
    CubeLoadingThreePiece = "Cube_Loading_ThreePiece"
    CubeMiddleOnePieceClimb = "Cube_Middle_OnePieceClimb"
    CubeWallTwoPiece = "Cube_Wall_TwoPiece"
    ConeLoadingTwoPiece = "Cone_Loading_TwoPiece"
    ConeLoadingThreePieceClimb = "Cone_Loading_ThreePieceClimb"
    ConeLoadingThreePieceMiddle = "Cone_Loading_ThreePieceMiddle"
    ConeLoadingThreePiece = "Cone_Loading_ThreePiece"

    def __str__(self) -> str:
        return str.__str__(self)


AUTONOMOUS_SELECTION_MAP = {
    AutonomousNames.SimpleAuto: SimpleAuto(),
    AutonomousNames.ToddCircle: ToddCircle(),
    AutonomousNames.CorrectStart: CorrectStart(),
    AutonomousNames.CubeLoadingThreePiece: CubeLoadingThreePiece(),
    AutonomousNames.CubeMiddleOnePieceClimb: CubeMiddleOnePieceClimb(),
    AutonomousNames.CubeWallTwoPiece: CubeWallTwoPiece(),
    AutonomousNames.ConeLoadingTwoPiece: ConeLoadingTwoPiece(),
    AutonomousNames.ConeLoadingThreePieceClimb: ConeLoadingThreePieceClimb(),
    AutonomousNames.ConeLoadingThreePieceMiddle: ConeLoadingThreePieceMiddle(),
    AutonomousNames.ConeLoadingThreePiece: ConeLoadingThreePiece()
}
