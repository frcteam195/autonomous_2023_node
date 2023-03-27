from enum import Enum

from autonomous_node.autos.Cone_Loading_TwoHighClimb import Cone_Loading_TwoHighClimb
from autonomous_node.autos.Cone_Loading_TwoMidClimb import Cone_Loading_TwoMidClimb
from autonomous_node.autos.Cone_Middle_Climb import Cone_Middle_Climb
from autonomous_node.autos.Cone_Wall_GatherAndClimb import Cone_Wall_GatherAndClimb
from autonomous_node.autos.Cone_Loading_MidLink import Cube_Loading_MidLink
from autonomous_node.autos.Cone_Loading_ExperimentalMidLink import Cube_Loading_ExperimentalMidLink
from autonomous_node.autos.Cube_Middle_Climb import Cube_Middle_Climb
from autonomous_node.autos.Cube_Wall_TwoHigh import Cube_Wall_TwoHigh
from autonomous_node.autos.Cube_Bump_Whack import Cube_Bump_Whack
from autonomous_node.autos.Cube_Loading_TwoAndHalfPieceClimb import Cube_Loading_TwoAndHalfPieceClimb
from autonomous_node.autos.Cone_Loading_TwoHighClimbWhack import Cone_Loading_TwoHighClimbWhack
from autonomous_node.autos.Cone_Loading_ThreePiece import Cone_Loading_ThreePiece
from autonomous_node.autos.Cube_Loading_ThreePieceBumper import Cube_Loading_ThreePieceBumper


# Incomplete Autos
# from autonomous_node.autos.Cube_Loading_GatherAndClimb import Cube_Loading_GatherAndClimb

# Test Autos
# from autonomous_node.autos.AutoBalance import AutoBalance
from autonomous_node.autos.Curve import Curve
# from autonomous_node.autos.StraightLine import StraightLine
# from autonomous_node.autos.Curve import Curve
from autonomous_node.autos.StraightLine import StraightLine


class AutonomousNames(str, Enum):
    """
    Format must be PRELOAD_STARTINGPOSITION_ANYNAMENOTINCLUDINGAKEYWORDFORPRELOADORSTARTINGPOSITION
    """
    Cone_Loading_TwoHighClimb = "Cone_Loading_TwoHighClimb"
    Cone_Loading_TwoMidClimb = "Cone_Loading_TwoMidClimb"
    Cone_Middle_Climb = "Cone_Middle_Climb"
    # Cone_Wall_GatherAndClimb = "Cone_Wall_GatherAndClimb"
    Cube_Loading_MidLink = "Cone_Loading_MidLink"
    Cube_Loading_ExperimentalMidLink = "Cone_Loading_ExperimentalMidLink"
    Cube_Middle_Climb = "Cube_Middle_Climb"
    Cube_Wall_TwoHigh = "Cube_Wall_TwoHigh"
    Cube_Bump_Whack = "Cube_Bump_Whack"
    Cube_Loading_TwoAndHalfPieceClimb = "Cube_Loading_TwoAndHalfPieceClimb"
    Cone_Loading_TwoHighClimbWhack = "Cone_loading_TwoHighClimbWhack"
    Cone_Loading_ThreePiece = "Cone_Loading_ThreePiece"
    Cube_Loading_ThreePieceBumper = "Cube_Loading_ThreePieceBumper"


    # Incomplete Autos
    # Cube_Loading_GatherAndClimb = "Cube_Loading_GatherAndClimb"

    # Test Autos
    # AutoBalance = "Test_Test_AutoBalance"
    Curve = "Test_Test_Curve"
    # StraightLine = "Test_Test_StraightLine"
    # Curve = "Test_Test_Curve"
    StraightLine = "Test_Test_StraightLine"

    def __str__(self) -> str:
        return str.__str__(self)


AUTONOMOUS_SELECTION_MAP = {}


def init_auto_selection_map():
    """
    Returns an autonomous selection map, mapping auto names to auto programs.
    """
    return {
        AutonomousNames.Cone_Loading_TwoHighClimb: Cone_Loading_TwoHighClimb(),
        AutonomousNames.Cone_Loading_TwoMidClimb: Cone_Loading_TwoMidClimb(),
        AutonomousNames.Cube_Middle_Climb: Cube_Middle_Climb(),
        # AutonomousNames.Cone_Wall_GatherAndClimb: Cone_Wall_GatherAndClimb(),
        AutonomousNames.Cube_Loading_MidLink: Cube_Loading_MidLink(),
        AutonomousNames.Cube_Loading_ExperimentalMidLink: Cube_Loading_ExperimentalMidLink(),
        AutonomousNames.Cone_Middle_Climb: Cone_Middle_Climb(),
        AutonomousNames.Cube_Wall_TwoHigh: Cube_Wall_TwoHigh(),
        AutonomousNames.Cube_Bump_Whack: Cube_Bump_Whack(),
        AutonomousNames.Cube_Loading_TwoAndHalfPieceClimb: Cube_Loading_TwoAndHalfPieceClimb(),
        AutonomousNames.Cone_Loading_TwoHighClimbWhack: Cone_Loading_TwoHighClimbWhack(),
        AutonomousNames.Cone_Loading_ThreePiece: Cone_Loading_ThreePiece(),
        AutonomousNames.Cube_Loading_ThreePieceBumper: Cube_Loading_ThreePieceBumper(),

        # Incomplete Autos
        # AutonomousNames.Cube_Loading_GatherAndClimb: Cube_Loading_GatherAndClimb(),

        # Test Autos
        # AutonomousNames.AutoBalance: AutoBalance(),
        AutonomousNames.Curve: Curve(),
        # AutonomousNames.StraightLine: StraightLine(),
        # AutonomousNames.Curve: Curve(),
        AutonomousNames.StraightLine: StraightLine(),
    }
