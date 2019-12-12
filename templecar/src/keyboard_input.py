#!/usr/bin/env python

#install termios, tty, select, rospy

from __future__ import print_function

import rospy

from templecar.msg import Drive

import sys, select, termios, tty

msg = """
Reading from the keyboard  and Publishing to drive!
---------------------------
Moving around:
   q    w    e
   a    s    d

CTRL-C to quit
"""

speedBindings={
        'w':(0.17,0.15),
        's':(0.13,0.15),
        'a':(0.15,0.12),
        'd':(0.15,0.18),
        'q':(0.17,0.13),
        'e':(0.17,0.17),
    }

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def vels(speed,steering):
    return "currently:\tspeed %s\tsteering %s " % (speed,steering)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    pub = rospy.Publisher('driving', Drive, queue_size = 1)
    rospy.init_node('keyboard_driver')
    speed = 0.15
    steering = 0.15
    try:
        print(msg)
        print(vels(speed,steering))
        while(1):
            key = getKey()
            print(vels(speed,steering))
            if key in speedBindings.keys():
                speed = speedBindings[key][0]
                steering = speedBindings[key][1]
            else:
                speed = 0.15
                steering = 0.15
                if (key == '\x03'):
                    break

            drive = Drive()
            drive.speed = speed
            drive.steering = steering
            pub.publish(drive)

    except Exception as e:
        print(e)

    finally:
        drive = Drive()
        drive.speed = 0.15
        drive.steering = 0.15
        pub.publish(drive)

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
