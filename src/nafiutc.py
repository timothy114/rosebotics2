"""
  Capstone Project.  Code written by Toluwa Nafiu.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    if robot.color_sensor.get_color() == 3:
        robot.drive_system.stop_moving()


main()
