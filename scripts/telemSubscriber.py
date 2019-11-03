#!/usr/bin/env python
import rospy
import os, random
from swarmhoc.msg import NetTelem

import iwlistparser

def telem_callback_1(data):
    rospy.loginfo(data.data)

def telem_callback_2(data):
    rospy.loginfo(data.data)



def telem_subscriber():
	rospy.init_node('telemSubscriber', anonymous=True)

	rospy.Subscriber('/uav1/networkTelem', NetTelem, telem_callback_1)
	rospy.Subscriber('/uav2/networkTelem', NetTelem, telem_callback_2)

	rospy.spin()

if __name__ == '__main__':
	try:
		telem_subscriber()
	except rospy.ROSInterruptException:
		pass
