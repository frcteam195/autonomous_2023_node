"""
Class definition of the autonomous node.
"""

from threading import Thread
import rospy

from ck_ros_msgs_node.msg import Autonomous_Configuration, Autonomous_Selection

from frc_robot_utilities_py_node.frc_robot_utilities_py import *
from frc_robot_utilities_py_node.RobotStatusHelperPy import RobotStatusHelperPy, Alliance, RobotMode

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

            self.autonomous_configuration_publisher.publish(self.autonomous_configuration_options)

            rate.sleep()

    def filter_autonomous_options(self, selections) -> None:
        """
        Filters the available autonomous options based on the currently selected starting position and game piece.
        """
        self.autonomous_configuration_options = AUTONOMOUS_MAP[selections.game_piece][selections.starting_position]

        starting_position = selections.starting_position.replace(' ', '').lower()
        autonomous = selections.autonomous.replace(' ', '').lower()

        self.autonomous_configuration_options.preview_image_name = f"{starting_position}_{autonomous}.png"
