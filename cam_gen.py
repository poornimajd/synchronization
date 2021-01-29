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


# def callback1(msg):
#     global imgtnew
#     timenow=float(msg.data.secs)+float(msg.data.nsecs)/(10**9)
#     off=float(timenow)-float(imgt)#compute the offset between the sync event generated clock and the image topic header timestamp
#     imgtnew=float(imgt)+float(off)#add the offset to the image topic timestamp
    
def callback_fun(msg):

    #get the image topic header timestamp
    imgt=str(float(msg.header.stamp.secs)+(float(msg.header.stamp.nsecs)/(10**9))) 

    #wait for the sync signal to be published
    virtualtime=rospy.wait_for_message('time_sync_signal',Time)

    #get the timestamp published by the sync signal
    timenow=float(virtualtime.data.secs)+float(virtualtime.data.nsecs)/(10**9)

    #compute the offset between the sync event generated clock and the image topic header timestamp
    off=float(timenow)-float(imgt)

    #add the offset to the image topic timestamp
    imgtnew=float(imgt)+float(off)

    #save the image using opencv with timestamp as the name 
    img = CV_BRIDGE.imgmsg_to_cv2(msg, 'bgr8')
    nametosave=str(imgtnew).ljust(13,'0')
    cv2.imwrite('./offset/imgs/'+str(nametosave)+'.jpeg',img)


if __name__ == '__main__':

    #initialize the node
    rospy.init_node('cam_lid_sync', anonymous=True)

    #subscribe to image topic
    sub=rospy.Subscriber('image_raw',Image,callback_fun) 
    rospy.spin()