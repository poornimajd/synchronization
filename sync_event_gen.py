#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String,Time


if __name__=='__main__':
    #initialize the node
    rospy.init_node("sync_event_publisher")

    #sync_event topic publish
    pub=rospy.Publisher('time_sync_signal',Time,queue_size=5)

    #Publish at a rate of 10Hz
    rate=rospy.Rate(10)

    #publish until the node is not shutdown
    while not rospy.is_shutdown():
        
        #publish the current system time 
        pub.publish(rospy.get_rostime())
        rate.sleep()
    rospy.loginfo("killed")
