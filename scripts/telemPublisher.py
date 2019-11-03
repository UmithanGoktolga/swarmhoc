#!/usr/bin/env python
import rospy
import os, random
from swarmhoc.msg import NetTelem

import iwlistparser

def telem_publisher():
    pub = rospy.Publisher('networkTelem', NetTelem, queue_size=10)
    rospy.init_node('telemPublisher', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        telem_data = NetTelem()

        telem_data.header.frame_id = os.environ['ROS_MASTER_URI'] 
        telem_data.header.stamp = rospy.get_rostime()
	telem_data.quality = iwlistparser.main()[0]
        telem_data.signal = iwlistparser.main()[1]

        if telem_data.quality == -1: # If specified ESSID is not in 'iwlist scan', make connected False
            telem_data.connected = False
        else:
            telem_data.connected = True

        rospy.loginfo(telem_data)
        pub.publish(telem_data)

        rate.sleep()

if __name__ == '__main__':
    try:
        telem_publisher()
    except rospy.ROSInterruptException:
        pass
