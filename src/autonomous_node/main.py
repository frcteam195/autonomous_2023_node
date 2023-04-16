"""
Class definition of the autonomous node.
"""

from threading import Thread
import rospy

from actions_node.ActionRunner import ActionRunner
from ck_ros_msgs_node.msg import Autonomous_Configuration, Autonomous_Selection

from frc_robot_utilities_py_node.frc_robot_utilities_py import *
from frc_robot_utilities_py_node.RobotStatusHelperPy import RobotMode
from autonomous_node.autos import AUTONOMOUS_SELECTION_MAP, AutonomousNames
from autonomous_node.autos.AutoBase import AutoBase
from actions_node.default_actions.Action import Action
from autonomous_node.autos import init_auto_selection_map
from threading import RLock


class AutonomousNode():
    """
    The autonomous node.
    """

    def __init__(self) -> None:

        rospy.Subscriber("AutonomousSelection", Autonomous_Selection, self.get_selected_auto, tcp_nodelay=True)

        self.autonomous_configuration_publisher = rospy.Publisher(
            name="AutonomousConfiguration", data_class=Autonomous_Configuration, queue_size=50, tcp_nodelay=True)
        self.autonomous_configuration_options = Autonomous_Configuration()
        self.selected_autonomous_string : str = ""
        self.__prev_selected_autonomous_string : str = ""

        self.runner = ActionRunner()

        self.__lock = RLock()

        self.__prev_robot_mode = RobotMode.DISABLED
        self.__selected_auto : AutoBase = None
        self.__prev_selected_auto : AutoBase = None
        self.__selected_auto_action : Action = None

        register_for_robot_updates()
        global AUTONOMOUS_SELECTION_MAP
        AUTONOMOUS_SELECTION_MAP = init_auto_selection_map()
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

            if robot_mode == RobotMode.TELEOP:
                rate.sleep()
                continue

            self.autonomous_configuration_publisher.publish(self.autonomous_configuration_options)

            try:
                with self.__lock:
                    if (self.__selected_auto is None or self.selected_autonomous_string != self.__prev_selected_autonomous_string) \
                            and AutonomousNames(self.selected_autonomous_string) in AUTONOMOUS_SELECTION_MAP:
                        
                        self.__selected_auto : AutoBase = AUTONOMOUS_SELECTION_MAP[AutonomousNames(self.selected_autonomous_string)]
                    elif AutonomousNames(self.selected_autonomous_string) not in AUTONOMOUS_SELECTION_MAP:
                        self.__selected_auto = None
            except:
                rospy.logerr_throttle_identical(period=10,msg=f"Invalid auto string received! {self.selected_autonomous_string}")
                self.__selected_auto = None

            if robot_mode == RobotMode.AUTONOMOUS:
                # Start the action on the transition from Disabled to Auto.
                if self.__prev_robot_mode == RobotMode.DISABLED:
                    if self.__selected_auto is not None:
                        self.runner.start_action(self.__selected_auto_action)
                        self.__prev_selected_auto = None
            elif robot_mode == RobotMode.DISABLED:
                if self.__prev_robot_mode == RobotMode.AUTONOMOUS:
                    self.__selected_auto = None
                    self.runner.reset_action_list()

                if self.__selected_auto != self.__prev_selected_auto:
                    if self.__selected_auto != None:
                        self.__selected_auto_action = self.__selected_auto.get_action()
                    elif self.__prev_robot_mode == RobotMode.AUTONOMOUS:
                        pass
                    else:
                        rospy.logerr_throttle_identical(period=10,msg=f"Selected auto is none! {self.selected_autonomous_string}")
                        
                if self.__selected_auto is not None:
                    self.__selected_auto.reset()

            self.__prev_robot_mode = robot_mode
            self.__prev_selected_auto = self.__selected_auto
            self.__prev_selected_autonomous_string = self.selected_autonomous_string

            if self.__prev_robot_mode == RobotMode.AUTONOMOUS:
                # Only loop in auto
                self.runner.loop(robot_mode)

            rate.sleep()

    def get_selected_auto(self, selections : Autonomous_Selection) -> None:
        """
        Returns the selected autonomous from a mutex.
        """
        with self.__lock:
            self.selected_autonomous_string = selections.autonomous
