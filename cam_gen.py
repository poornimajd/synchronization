#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python 2/3 compatibility
from __future__ import print_function

# Built-in modules
import os
import sys
import time


# External modules
import cv2
import numpy as np


# ROS modules
from std_msgs.msg import Time,String

import rospy
import tf2_ros
from cv_bridge import CvBridge, CvBridgeError
import ros_numpy
CV_BRIDGE = CvBridge()
from sensor_msgs.msg import Image, CameraInfo, PointCloud2


def callback1(msg):
    global imgtnew
    off=(float(imgt)-float(msg.data))#compute the offset between the sync event generated clock and the image topic header timestamp
    imgtnew=float(imgt)+float(off)#add the offset to the image topic timestamp

def callback_fun(msg):
    global imgt

    imgt=str(float(msg.header.stamp.secs)+(float(msg.header.stamp.nsecs)/(10**9))) #get the image topic header timestamp
    subnew=rospy.Subscriber('/signal',String,callback1) #get the sync event along with the timestamp from clock,passed as a String

    img = CV_BRIDGE.imgmsg_to_cv2(msg, 'bgr8')
    nametosave=str(imgtnew).ljust(13,'0')
    cv2.imwrite('./offset/imgs/'+str(nametosave)+'.jpeg',img)#save the image with timestamp as the name 


if __name__ == '__main__':


    rospy.init_node('calibrate_camera_lidar', anonymous=True)
    sub=rospy.Subscriber('/image_raw',Image,callback_fun) #subscribe to image topic
    rospy.spin()
