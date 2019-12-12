#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from templecar.msg import Drive
from rpiHAT import ServoNT
#from beginner_tutorials.msg import Num
#from rpiHAT import Racecar


def callback(data):
    global s
    global t

    rospy.loginfo(rospy.get_caller_id() + "speed = %f", data.speed)
    rospy.loginfo(rospy.get_caller_id() + "direction = %f", data.steering)

    s.pulse(data.speed)
    t.pulse(data.steering)


def listener():
    rospy.init_node('listener', anonymous=True)
    #rospy.Subscriber("Car", Num, callback)
    rospy.Subscriber("driving", Drive, callback)
    rospy.spin()

if __name__ == '__main__':
    s = ServoNT(channel = 1, freq = 98.1)
    t = ServoNT(channel=2, freq=98.1)
    listener()