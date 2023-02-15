"""
Class definition of the autonomous node.
"""

from threading import Thread
import rospy

from actions_node.ActionRunner import ActionRunner
from ck_ros_msgs_node.msg import Autonomous_Configuration, Autonomous_Selection

from frc_robot_utilities_py_node.frc_robot_utilities_py import *
from frc_robot_utilities_py_node.RobotStatusHelperPy import RobotStatusHelperPy, Alliance, RobotMode
from autonomous_node.autos import AUTONOMOUS_SELECTION_MAP, AutonomousNames

#TODO: Update to use the enum from AutonomousNames in __init__.py for the final auto string so that there is no chance of typo
AUTONOMOUS_MAP = {
    "Cube": {
        "Wall": ["Score Cube"],
        "Middle": ["Score + Balance", "Balance"],
        "Loading": ["Score Cube"]
    },
    "Cone": {
        "Wall": ["Score Cone"],
        "Middle": ["Score + Balance", "Balance"],
        "Loading": ["Score Cone"]
    }
}

class AutonomousNode():
    """
    The autonomous node.
    """

    def __init__(self) -> None:

        rospy.Subscriber("AutonomousSelection", Autonomous_Selection, self.filter_autonomous_options)

        self.autonomous_configuration_publisher = rospy.Publisher(
            name="AutonomousConfiguration", data_class=Autonomous_Configuration, queue_size=50, tcp_nodelay=True)

        self.autonomous_configuration_options = Autonomous_Configuration()
        self.selected_autonomous = ""

        self.runner = ActionRunner()

        self.__prev_robot_mode = RobotMode.DISABLED
        self.__selected_auto = AUTONOMOUS_SELECTION_MAP[AutonomousNames.SampleAuto]   #auto mapping is defined in autos.__init__.py


        register_for_robot_updates()
        loop_thread = Thread(target=self.loop)
        loop_thread.start()
        rospy.spin()
        loop_thread.join(5)

    def loop(self) -> None:
        """
        Periodic function for the autonomous node.
        """
        self.autonomous_configuration_options.game_pieces = AUTONOMOUS_MAP.keys()
        self.autonomous_configuration_options.starting_positions = AUTONOMOUS_MAP["Cube"].keys()

        rate = rospy.Rate(50)

        while not rospy.is_shutdown():
            robot_mode : RobotMode = robot_status.get_mode()

            self.autonomous_configuration_publisher.publish(self.autonomous_configuration_options)

            # TODO: Create the autonomous action based on the selected autonomous.

            if robot_mode == RobotMode.AUTONOMOUS:
                #Start the action on the transition from Disabled to Auto
                if self.__prev_robot_mode == RobotMode.DISABLED:
                    if self.__selected_auto is not None:
                        self.runner.start_action(self.__selected_auto.getAction())

                #Maybe report status of the autonomous here?

            self.__prev_robot_mode = robot_mode
            self.runner.loop(robot_mode)

            rate.sleep()

    def filter_autonomous_options(self, selections) -> None:
        """
        Filters the available autonomous options based on the currently selected starting position and game piece.
        """
        self.autonomous_configuration_options = AUTONOMOUS_MAP[selections.game_piece][selections.starting_position]

        starting_position = selections.starting_position.replace(' ', '').lower()
        autonomous = selections.autonomous.replace(' ', '').lower()

        self.selected_autonomous = f"{starting_position}_{autonomous}"
        self.autonomous_configuration_options.preview_image_name = f"{starting_position}_{autonomous}.png"
