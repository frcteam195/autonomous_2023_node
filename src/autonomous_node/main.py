#!/usr/bin/env python3

import tf2_ros
import rospy
from threading import Thread

from frc_robot_utilities_py_node.frc_robot_utilities_py import *
from frc_robot_utilities_py_node.RobotStatusHelperPy import RobotStatusHelperPy, Alliance, RobotMode
from ck_ros_msgs_node.msg import Autonomous_Configuration, Autonomous_Selection
from swerve_trajectory_node.srv import StartTrajectory, StartTrajectoryResponse, GetStartPose, GetStartPoseResponse


run_once = True
run_auto = True
current_start_pose = GetStartPoseResponse(x_inches=0, y_inches=0, heading_degrees=0)

selected_auto = 'correct_start'


def same_pose(pose1: GetStartPoseResponse, pose2: GetStartPoseResponse) -> bool:
    return pose1.x_inches == pose2.x_inches and pose1.y_inches == pose2.y_inches and pose1.heading_degrees == pose2.heading_degrees

def filter_autos(new_selections):
    global autonomous_configuration_options
    
    # Determine the available autonomous.
    if new_selections.starting_position == "Wall":
        autonomous_configuration_options.autonomous_options =  ["Score Two + Climb"]
    elif new_selections.starting_position == "Middle":
        autonomous_configuration_options.autonomous_options =  ["Climb", "Score Two + Climb"]
    elif new_selections.starting_position == "Loading Side":
        autonomous_configuration_options.autonomous_options =  ["Score Three + Climb"]


    # Determine the file name.

    starting_position = f"{new_selections.starting_position.replace(' ', '').lower()}"

    if new_selections.autonomous == "Climb":
        autonomous_configuration_options.preview_image_name = f"{starting_position}_climb.png"
    elif new_selections.autonomous == "Score Two + Climb":
        autonomous_configuration_options.preview_image_name = f"{starting_position}_score_two.png"
    elif new_selections.autonomous == "Score Three + Climb":
        autonomous_configuration_options.preview_image_name = f"{starting_position}_score_three.png"
  

    

def ros_func():
    global autonomous_configuration_options
    global hmi_updates
    global robot_status
    global get_pose
    global run_once
    global run_auto
    global current_start_pose
    global selected_auto

    auto_configuration_publisher = rospy.Publisher(name="AutonomousConfiguration", data_class=Autonomous_Configuration, queue_size=50, tcp_nodelay=True)
    autonomous_configuration_options = Autonomous_Configuration()
   # autonomous_configuration_options.autonomous_options =  ["Climb", "Score Two + Climb"]
    autonomous_configuration_options.game_pieces = ["Cone", "Cube"]
    autonomous_configuration_options.starting_positions = ["Wall", "Middle", "Loading Side"]

    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        if run_once:
            rospy.sleep(5)
            get_pose = rospy.ServiceProxy('/get_start_pose', GetStartPose)
            start_pose: GetStartPoseResponse = get_pose(selected_auto)

            print(start_pose)
            reset_robot_pose(start_pose.x_inches, start_pose.y_inches, start_pose.heading_degrees)
            run_once = False

        if run_auto and robot_status.get_mode() == RobotMode.AUTONOMOUS:
            auto_runner = rospy.ServiceProxy('/start_trajectory', StartTrajectory)
            auto_runner(selected_auto)
            run_auto = False 
        elif robot_status.get_mode() == RobotMode.DISABLED:
            run_auto = True

        auto_configuration_publisher.publish(autonomous_configuration_options)

        rate.sleep()


def ros_main(node_name):
    rospy.init_node(node_name)
    register_for_robot_updates()
    
    rospy.Subscriber("AutonomousSelection", Autonomous_Selection, filter_autos)

    t1 = Thread(target=ros_func)
    t1.start()

    rospy.spin()

    t1.join(5)