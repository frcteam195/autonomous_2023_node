from enum import Enum

from autonomous_node.autos.CubeLoadingThreePiece import CubeLoadingThreePiece
from autonomous_node.autos.ConeLoadingThreePieceClimb import ConeLoadingThreePieceClimb
from autonomous_node.autos.ConeLoadingThreePiece import ConeLoadingThreePiece
from autonomous_node.autos.ConeLoadingThreePieceMidLink import ConeLoadingThreePieceMidLink

class AutonomousNames(str, Enum):
    """
    Format must be PRELOAD_STARTINGPOSITION_ANYNAMENOTINCLUDINGAKEYWORDFORPRELOADORSTARTINGPOSITION
    """
    CubeLoadingThreePiece = "Cube_Loading_ThreePiece"
    ConeLoadingThreePieceClimb = "Cone_Loading_ThreePieceClimb"
    ConeLoadingThreePiece = "Cone_Loading_ThreePiece"
    ConeLoadingThreePieceMidLink = "Cone_Loading_ThreePieceMidLink"

    def __str__(self) -> str:
        return str.__str__(self)


AUTONOMOUS_SELECTION_MAP = {
    AutonomousNames.CubeLoadingThreePiece: CubeLoadingThreePiece(),
    AutonomousNames.ConeLoadingThreePieceClimb: ConeLoadingThreePieceClimb(),
    AutonomousNames.ConeLoadingThreePiece: ConeLoadingThreePiece(),
    AutonomousNames.ConeLoadingThreePieceMidLink: ConeLoadingThreePieceMidLink()
}
