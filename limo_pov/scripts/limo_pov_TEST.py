#!/usr/bin/env python

# Python libs
import sys, time
 
# Ros libraries
import roslib
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
 
# OpenCV
import numpy as np
import cv2

# Load an color image in colour
img = cv2.imread(Image,1)

# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
(h, w, d) = img.shape
print("width={}, height={}, depth={}".format(w, h, d))

def callback(data):

    
 cv2.imshow('LIMO POV', img)

 # Porgram will hold the screen until user closes it.
 cv2.waitKey(0)

 # It is for removing/deleting created GUI window from screen and memory
 cv2.destroyAllWindows()
     
def listener():
 
     # In ROS, nodes are uniquely named. If two nodes with the same
     # name are launched, the previous one is kicked off. The
     # anonymous=True flag means that rospy will choose a unique
     # name for our 'listener' node so that multiple listeners can
     # run simultaneously.
     rospy.init_node('limo_pov_node', anonymous=True)
 
     rospy.Subscriber("/camera/rgb/image_raw", Image, callback)
     rospy.bridge = CvBridge()
 
     # spin() simply keeps python from exiting until this node is stopped
     rospy.spin()
 
if __name__ == '__main__':
     listener()