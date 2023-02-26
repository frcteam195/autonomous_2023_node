from enum import Enum

from autonomous_node.autos.SimpleAuto import SimpleAuto
from autonomous_node.autos.ToddCircle import ToddCircle
from autonomous_node.autos.CorrectStart import CorrectStart
from autonomous_node.autos.CubeLoadingTwoPiece import CubeLoadingTwoPiece
from autonomous_node.autos.CubeMiddleOnePieceClimb import CubeMiddleOnePieceClimb
from autonomous_node.autos.CubeWallTwoPiece import CubeWallTwoPiece
from autonomous_node.autos.ConeLoadingTwoPiece import ConeLoadingTwoPiece
from autonomous_node.autos.ConeLoadingThreePieceClimb import ConeLoadingThreePieceClimb

class AutonomousNames(str, Enum):
    """
    Format must be PRELOAD_STARTINGPOSITION_ANYNAMENOTINCLUDINGAKEYWORDFORPRELOADORSTARTINGPOSITION
    """
    SimpleAuto = "Test_Test_Auto"
    ToddCircle = "Test_Test_ToddCircle"
    CorrectStart = "Test_Test_CorrectStart"
    CubeLoadingTwoPiece = "Cube_Loading_TwoPiece"
    CubeMiddleOnePieceClimb = "Cube_Middle_OnePieceClimb"
    CubeWallTwoPiece = "Cube_Wall_TwoPiece"
    ConeLoadingTwoPiece = "Cone_Loading_TwoPiece"
    ConeLoadingThreePieceClimb = "Cone_Loading_ThreePieceClimb"

    def __str__(self) -> str:
        return str.__str__(self)


AUTONOMOUS_SELECTION_MAP = {
    AutonomousNames.SimpleAuto: SimpleAuto(),
    AutonomousNames.ToddCircle: ToddCircle(),
    AutonomousNames.CorrectStart: CorrectStart(),
    AutonomousNames.CubeLoadingTwoPiece: CubeLoadingTwoPiece(),
    AutonomousNames.CubeMiddleOnePieceClimb: CubeMiddleOnePieceClimb(),
    AutonomousNames.CubeWallTwoPiece: CubeWallTwoPiece(),
    AutonomousNames.ConeLoadingTwoPiece: ConeLoadingTwoPiece(),
    AutonomousNames.ConeLoadingThreePieceClimb: ConeLoadingThreePieceClimb()
}
