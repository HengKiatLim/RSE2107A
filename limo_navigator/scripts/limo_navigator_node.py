#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():


    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 0.0
    goal.target_pose.pose.position.y = -2.0
    goal.target_pose.pose.orientation.w = 1.0
    goal.target_pose.pose.orientation.z = 8.0


    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()
       

def movebase_client2():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal2 = MoveBaseGoal()
    goal2.target_pose.header.frame_id = "map"
    goal2.target_pose.header.stamp = rospy.Time.now()
    goal2.target_pose.pose.position.x = -4.0
    goal2.target_pose.pose.position.y = -2.0
    goal2.target_pose.pose.orientation.w = 1.0
    goal2.target_pose.pose.orientation.z = 2.0

    client.send_goal(goal2)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

def movebase_client3():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal3 = MoveBaseGoal()
    goal3.target_pose.header.frame_id = "map"
    goal3.target_pose.header.stamp = rospy.Time.now()
    goal3.target_pose.pose.position.x = -4.0
    goal3.target_pose.pose.position.y = 0.6
    goal3.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal3)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result() 

def movebase_client4():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal4 = MoveBaseGoal()
    goal4.target_pose.header.frame_id = "map"
    goal4.target_pose.header.stamp = rospy.Time.now()
    goal4.target_pose.pose.position.x = 0.0
    goal4.target_pose.pose.position.y = 0.0
    goal4.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal4)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()               

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("GOAL1 execution DONE!")
        result2 = movebase_client2()
        if result2:
            rospy.loginfo("GOAL2 execution DONE!")
        result3 = movebase_client3()
        if result3:
            rospy.loginfo("GOAL3 execution DONE!")
        result4 = movebase_client4()
        if result4:
            rospy.loginfo("GOAL4 execution DONE!")                        

    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")

