"""
  Capstone Project.  Code written by Timothy Li.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time

#Making the polygon one

def polygon(robot,num,length,speed=100):
    #robot is the robot lol
    #num is an integer that is the number of sides
    #length is a float that is the length of each side in inches

    #Finding the interior angle of the polygon
    angle = ((num - 2)*180)/num

    print("There are " + str(num) + " sides")
    print("Angle is " + str(angle) + " degrees")
    print("Length is " + str(length) + " inches")

    for i in range(num):
        robot.drive_system.go_straight_inches(length,speed)
        robot.drive_system.spin_in_place_degrees(angle,speed)

def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    polygon(robot,5,20)

main()
