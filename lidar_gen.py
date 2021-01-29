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
    timenow=float(msg.data.secs)+float(msg.data.nsecs)/(10**9)

    #compute the offset between the sync event generated clock and the lidar topic header timestamp
    off=float(timenow)-float(lidt)

    #add the offset to the lidar topic timestamp
    lidtnew=float(lidt)+float(off)
    
def callback_fun(msg):
    global lidt

    #get the lidar topic header timestamp
    lidt=str(float(msg.header.stamp.secs)+(float(msg.header.stamp.nsecs)/(10**9)))

    #get the sync event along with the timestamp from clock
    subnew=rospy.Subscriber('/time_sync_signal',Time,callback1)

    #save the lidar pointcloud using numpy(np) with timestamp as the name
    points = ros_numpy.point_cloud2.pointcloud2_to_array(msg)
    nametosave=str(lidtnew).ljust(13,'0')
    np.save('./offset/imgs/'+str(nametosave),points)


if __name__ == '__main__':


    #initialize the node
    rospy.init_node('cam_lid_sync', anonymous=True)

    #subscribe to lidar topic
    sub=rospy.Subscriber('/velodyne_points',PointCloud2,callback_fun)
    rospy.spin()
