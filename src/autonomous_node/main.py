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

from autonomous_node.autos import CorrectStart

from threading import RLock


class AutonomousNode():
    """
    The autonomous node.
    """

    def __init__(self) -> None:

        rospy.Subscriber("AutonomousSelection", Autonomous_Selection, self.get_selected_auto, tcp_nodelay=True)
        
        self.autonomous_configuration_publisher = rospy.Publisher(name="AutonomousConfiguration", data_class=Autonomous_Configuration, queue_size=50, tcp_nodelay=True)
        self.autonomous_configuration_options = Autonomous_Configuration()
        self.selected_autonomous = ""

        self.runner = ActionRunner()

        self.__lock = RLock()

        self.__prev_robot_mode = RobotMode.DISABLED
        self.__selected_auto = None


        register_for_robot_updates()
        loop_thread = Thread(target=self.loop)
        loop_thread.start()
        rospy.spin()
        loop_thread.join(5)

    def loop(self) -> None:
        """
        Periodic function for the autonomous node.
        """
        rate = rospy.Rate(50)

        self.autonomous_configuration_options.autonomous_options = [auto_name.value for auto_name in AutonomousNames]

        while not rospy.is_shutdown():
            robot_mode : RobotMode = robot_status.get_mode()
            self.autonomous_configuration_publisher.publish(self.autonomous_configuration_options)

            try:
                with self.__lock:
                    if AutonomousNames(self.selected_autonomous) in AUTONOMOUS_SELECTION_MAP:
                        self.__selected_auto = AUTONOMOUS_SELECTION_MAP[AutonomousNames(self.selected_autonomous)]
                    else:
                        self.__selected_auto = None
            except:
                rospy.logerr_throttle(period=10,msg="Invalid auto string received!")
                self.__selected_auto = None

            if robot_mode == RobotMode.AUTONOMOUS:
                # Start the action on the transition from Disabled to Auto.
                if self.__prev_robot_mode == RobotMode.DISABLED:
                    if self.__selected_auto is not None:
                        self.runner.start_action(self.__selected_auto.getAction())

            self.__prev_robot_mode = robot_mode
            self.runner.loop(robot_mode)

            rate.sleep()

    def get_selected_auto(self, selections : Autonomous_Selection) -> None:
        with self.__lock:
            self.selected_autonomous = selections.autonomous