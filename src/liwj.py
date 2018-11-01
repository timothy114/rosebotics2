"""
  Capstone Project.  Code written by Timothy Li.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
from ev3dev import ev3

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
        robot.drive_system.spin_in_place_degrees((180-angle),speed)

def beep_when_hand(robot):
    #This is for the part where when you stick your hand in front of the robot it stops and beeps

    drive = rb.DriveSystem
    robot.drive_system.start_moving()
    print("Driving")
    sensor = rb.InfraredAsProximitySensor(ev3.INPUT_4)
    while(True):
        #Get disstance
        dist = sensor.get_distance_to_nearest_object_in_inches()
        print(dist)
        #Stopping if 12 inches away
        if dist <= 12:
            robot.drive_system.stop_moving()
            print("Object detected that is less than 12 inches away")
            ev3.Sound.beep(1)
            break

def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()

    #polygon(robot,5,20)
    #time.sleep(2)
    #polygon(robot,3,20)
    #time.sleep(2)
    #polygon(robot,6,15)

    beep_when_hand(robot)

main()
