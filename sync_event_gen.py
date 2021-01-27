#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String


if __name__=='__main__':
    rospy.init_node("sync_event_publisher")
    pub=rospy.Publisher('/signal',String,queue_size=10)#sync_event topic
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        msg=String()
        #get the timestamp to be published on the sync event topic
        nowtime=float(rospy.get_rostime().secs)+(float(rospy.get_rostime().nsecs)/(10**9))
        
        msg.data=str(nowtime)

        pub.publish(msg.data)
        rate.sleep()
    rospy.loginfo("killed")