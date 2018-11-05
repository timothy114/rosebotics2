"""
  Capstone Project.  Code written by Jess Thuer.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time

def follow_line(robot):
    while True:
        while robot.touch_sensor.get_value() == 0:
            spin = 5
            robot.color_sensor.wait_until_intensity_is_greater_than(95)
            robot.drive_system.start_moving()
            robot.color_sensor.wait_until_intensity_is_less_than(95)
            robot.drive_system.stop_moving()
            for k in range(360):
                if spin < 360:
                    robot.drive_system.spin_in_place_degrees(spin)
                    if robot.color_sensor.get_reflected_intensity() >= (95):
                        spin = spin + 360
                    spin = spin * (-k+2)
        if robot.touch_sensor.wait_until_pressed():
            break

def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    follow_line(robot)


main()
