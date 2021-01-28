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
from sensor_msgs.msg import Image, CameraInfo, PointCloud2

def callback1(msg):
    
    global lidtnew
    
    off=float(lidt)-float(msg.data)#compute the offset between the sync event generated clock and the lidar topic header timestamp
    
    lidtnew=float(lidt)+float(off)#add the offset to the lidar topic timestamp

def callback_fun(msg):
    global lidt
    
    lidt=str(float(msg.header.stamp.secs)+(float(msg.header.stamp.nsecs)/(10**9)))#get the lidar topic header timestamp
    subnew=rospy.Subscriber('/signal',String,callback1)#get the sync event along with the timestamp from clock,passed as a String

    points = ros_numpy.point_cloud2.pointcloud2_to_array(msg)
    nametosave=str(lidtnew).ljust(13,'0')
    np.save('./offset/imgs/'+str(nametosave),points)#save the lidar pointcloud with timestamp as the name


if __name__ == '__main__':

    rospy.init_node('calibrate_camera_lidar', anonymous=True)
    sub=rospy.Subscriber('/velodyne_points',PointCloud2,callback_fun)#subscribe to lidar topic
    rospy.spin()
