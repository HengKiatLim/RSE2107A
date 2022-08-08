#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

rospy.init_node('limo_pov_node', anonymous=True)

def callback(img):    
 cv2.imshow('LIMO POV', img)

 # Porgram will hold the screen until user closes it.
 cv2.waitKey(3)

def bridging(x):
     rospy.loginfo('Image received')
     try:
        cv_img = CvBridge.imgmsg_to_cv2(x, "passthrough")
     except CvBridgeError as e:
        rospy.logerr("CvBridge Error: {0}".format(e))
     callback(cv_img)
rospy.Subscriber("/camera/rgb/image_raw", Image, bridging)

    
while not rospy.is_shutdown():
     rospy.spin()
 
