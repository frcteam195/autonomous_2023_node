from enum import Enum

from autonomous_node.autos.Cone_Loading_TwoMidClimb import Cone_Loading_TwoMidClimb
from autonomous_node.autos.Cone_Middle_Climb import Cone_Middle_Climb
from autonomous_node.autos.Cone_Wall_GatherAndClimb import Cone_Wall_GatherAndClimb
from autonomous_node.autos.Cone_Loading_MidLink import Cube_Loading_MidLink
from autonomous_node.autos.Cube_Middle_Climb import Cube_Middle_Climb
from autonomous_node.autos.Cube_Wall_TwoHigh import Cube_Wall_TwoHigh

# Incomplete Autos
# from autonomous_node.autos.Cube_Loading_GatherAndClimb import Cube_Loading_GatherAndClimb

# Test Autos
# from autonomous_node.autos.AutoBalance import AutoBalance
# from autonomous_node.autos.Curve import Curve
# from autonomous_node.autos.StraightLine import StraightLine


class AutonomousNames(str, Enum):
    """
    Format must be PRELOAD_STARTINGPOSITION_ANYNAMENOTINCLUDINGAKEYWORDFORPRELOADORSTARTINGPOSITION
    """
    Cone_Loading_TwoMidClimb = "Cone_Loading_TwoMidClimb"
    Cone_Middle_Climb = "Cone_Middle_Climb"
    Cone_Wall_GatherAndClimb = "Cone_Wall_GatherAndClimb"
    Cube_Loading_MidLink = "Cone_Loading_MidLink"
    Cube_Middle_Climb = "Cube_Middle_Climb"
    Cube_Wall_TwoHigh = "Cube_Wall_TwoHigh"

    # Incomplete Autos
    # Cube_Loading_GatherAndClimb = "Cube_Loading_GatherAndClimb"

    # Test Autos
    # AutoBalance = "Test_Test_AutoBalance"
    # Curve = "Test_Test_Curve"
    # StraightLine = "Test_Test_StraightLine"

    def __str__(self) -> str:
        return str.__str__(self)


AUTONOMOUS_SELECTION_MAP = {}


def init_auto_selection_map():
    """
    Returns an autonomous selection map, mapping auto names to auto programs.
    """
    return {
        AutonomousNames.Cone_Loading_TwoMidClimb: Cone_Loading_TwoMidClimb(),
        AutonomousNames.Cube_Middle_Climb: Cube_Middle_Climb(),
        AutonomousNames.Cone_Wall_GatherAndClimb: Cone_Wall_GatherAndClimb(),
        AutonomousNames.Cube_Loading_MidLink: Cube_Loading_MidLink(),
        AutonomousNames.Cone_Middle_Climb: Cone_Middle_Climb(),
        AutonomousNames.Cube_Wall_TwoHigh: Cube_Wall_TwoHigh(),

        # Incomplete Autos
        # AutonomousNames.Cube_Loading_GatherAndClimb: Cube_Loading_GatherAndClimb(),

        # Test Autos
        # AutonomousNames.AutoBalance: AutoBalance(),
        # AutonomousNames.Curve: Curve(),
        # AutonomousNames.StraightLine: StraightLine(),
    }
