#!/usr/bin/env python3

import tf2_ros
import rospy
from threading import Thread

from frc_robot_utilities_py_node.frc_robot_utilities_py import *
from frc_robot_utilities_py_node.RobotStatusHelperPy import RobotStatusHelperPy, Alliance, RobotMode
from ck_ros_msgs_node.msg import Autonomous_Configuration

def ros_func():
    global hmi_updates
    global robot_status

    auto_configuration_publisher = rospy.Publisher(name="AutonomousConfiguration", data_class=Autonomous_Configuration, queue_size=50, tcp_nodelay=True)
    autonomous_configuration_options = Autonomous_Configuration()
    autonomous_configuration_options.autonomous_options = ["Climb", "Score Two + Climb"]
    autonomous_configuration_options.game_pieces = ["Cone", "Cube"]
    autonomous_configuration_options.starting_positions = ["Wall", "Middle", "Loading Side"]

    config_publish_counter : int = 1

    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        #Publish auto configuration once every two seconds
        if (config_publish_counter % 100 == 0):
            auto_configuration_publisher.publish(autonomous_configuration_options)
            config_publish_counter = 1
        else:
            config_publish_counter += 1

        if robot_status.get_mode() == RobotMode.AUTONOMOUS:
            pass
        elif robot_status.get_mode() == RobotMode.TELEOP:
            pass
        elif robot_status.get_mode() == RobotMode.DISABLED:
            pass
        elif robot_status.get_mode() == RobotMode.TEST:
            pass

        rate.sleep()


def ros_main(node_name):
    rospy.init_node(node_name)
    register_for_robot_updates()

    t1 = Thread(target=ros_func)
    t1.start()

    rospy.spin()

    t1.join(5)