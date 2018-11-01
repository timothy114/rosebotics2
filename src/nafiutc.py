"""
  Capstone Project.  Code written by Toluwa Nafiu.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev as ev3
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    if robot.color_sensor.get_color() == 3:
        robot.drive_system.stop_moving()

    camera = rb.Camera()
    blob_area = camera.get_biggest_blob().get_area()
    if blob_area >= 600:
        ev3.Sound.beep(1).wait(1)
    else:
        camera.get_biggest_blob()


main()
