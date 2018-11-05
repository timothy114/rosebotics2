"""
  Capstone Project.  Code written by Toluwa Nafiu.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time


def main():
    """ Runs YOUR specific part of the project """
    robot_stop_when_color(3)
    camera_beep()


def robot_stop_when_color(color):
    robot = rb.Snatch3rRobot()
    if robot.color_sensor.get_color() == color:
        robot.drive_system.stop_moving()


def camera_beep():
    camera = rb.Camera()
    blob_area = camera.get_biggest_blob().get_area()
    if blob_area >= 600:
        ev3.Sound.beep().wait()
    else:
        time.sleep(1)


main()
