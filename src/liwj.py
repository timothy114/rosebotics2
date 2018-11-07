"""
  Capstone Project.  Code written by Timothy Li.
  Fall term, 2018-2019.
"""
# Tim

import rosebotics_new as rb
from ev3dev import ev3
import time

import tkinter
from tkinter import ttk
import math

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
    #This is for the part where when you stick your hand in front of the robot it  beeps

    #drive = rb.DriveSystem
    #robot.drive_system.start_moving()
    print("Starting")
    sensor = rb.InfraredAsProximitySensor(ev3.INPUT_4)
    while(True):
        #Get disstance
        dist = sensor.get_distance_to_nearest_object_in_inches()
        print(dist)
        #Stopping if 15 inches away
        if dist <= 15:
            #robot.drive_system.stop_moving()
            print("Object detected that is less than 15 inches away")
            if dist >= 9:
                print("Object detected that is between 9 and 15 inches away")
                ev3.Sound.beep(1)
                break

def brick_GUI():
    """
    # Sprint 3 for the robot project
    root = tkinter.Tk()

    # Making the background yellow and making a 500X500 window at the center of the screen
    root.configure(bg='#feffbe', highlightcolor='#feffbe')
    root.geometry("500x500+500+100")

    # Making frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # Making buttons
    up_button = ttk.Button(frame1, text='UP')
    down_button = ttk.Button(frame1, text='DOWN')

    # Up button command
    def beep_once():
        ev3.Sound.beep(1)

    up_button['command'] = (lambda:beep_once())
    up_button.grid()

    # Down button command
    def beep_twice():
        ev3.Sound.beep(1)
        time.sleep(1)
        ev3.Sound.beep(1)

    up_button['command'] = (lambda:beep_twice())
    up_button.grid()

    root.mainloop()
    """

#########################

    root = tkinter.Tk()

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    button_up = ttk.Button(frame1, text='Up')
    def do_up():
        print("Up")
    button_up['command'] = (lambda:do_up())
    button_up.grid()

    button_down = ttk.Button(frame1, text='Down')

    def do_down():
        print("Down")

    button_down['command'] = (lambda: do_down())
    button_down.grid()

    root.mainloop()

# Timothy

def main():
    """ Runs YOUR specific part of the project """
    #robot = rb.Snatch3rRobot()

    # Sprint 1
    #polygon(robot,5,20)
    #time.sleep(2)
    #polygon(robot,3,20)
    #time.sleep(2)
    #polygon(robot,6,15)

    # Sprint 2
    #beep_when_hand(robot)

    # Sprint 3
    brick_GUI()


main()
