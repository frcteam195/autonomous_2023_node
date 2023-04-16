from enum import Enum

from autonomous_node.autos.Cone_Loading_TwoHighClimb import Cone_Loading_TwoHighClimb
from autonomous_node.autos.Cone_Middle_Climb import Cone_Middle_Climb
from autonomous_node.autos.Cube_Middle_Climb import Cube_Middle_Climb
from autonomous_node.autos.Cube_Loading_ThreePieceCube import Cube_Loading_ThreePieceCube
from autonomous_node.autos.Cube_Bump_ThreePieceCubeCone import Cube_Bump_ThreePieceCubeCone


class AutonomousNames(str, Enum):
    """
    Format must be PRELOAD_STARTINGPOSITION_ANYNAMENOTINCLUDINGAKEYWORDFORPRELOADORSTARTINGPOSITION
    """
    Cone_Loading_TwoHighClimb = "Cone_Loading_TwoHighClimb"
    Cube_Loading_ThreePieceCube = "Cube_Loading_ThreePieceCube"
    Cone_Middle_Climb = "Cone_Middle_Climb"
    Cube_Middle_Climb = "Cube_Middle_Climb"
    Cube_Bump_ThreePieceCubeCone = "Cube_Bump_ThreePieceCubeCone"



    def __str__(self) -> str:
        return str.__str__(self)


AUTONOMOUS_SELECTION_MAP = {}


def init_auto_selection_map():
    """
    Returns an autonomous selection map, mapping auto names to auto programs.
    """
    return {
        AutonomousNames.Cone_Loading_TwoHighClimb: Cone_Loading_TwoHighClimb(),
        AutonomousNames.Cube_Middle_Climb: Cube_Middle_Climb(),
        AutonomousNames.Cone_Middle_Climb: Cone_Middle_Climb(),
        AutonomousNames.Cube_Loading_ThreePieceCube: Cube_Loading_ThreePieceCube(),
        AutonomousNames.Cube_Bump_ThreePieceCubeCone: Cube_Bump_ThreePieceCubeCone(),
    }
