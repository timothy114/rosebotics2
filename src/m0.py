"""
  Capstone Project.  Code for testing basics.
  Author:  David Mutchler, based on work by Dave Fisher and others.
  READ and RUN this module but ** DO NOT MODIFY IT. **
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
    run_test_drive_system()
    #run_test_touch_sensor()
    #run_test_color_sensor()

def run_test_drive_system():
    """ Tests the  drive_system  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    """
    print()
    print("Testing the  drive_system  of the robot.")
    print("Move at (20, 50) - that is, veer left slowly")
    robot.drive_system.start_moving(20, 10)
    time.sleep(2)
    robot.drive_system.stop_moving()

    print("Left/right wheel positions:",
          robot.drive_system.left_wheel.get_degrees_spun(),
          robot.drive_system.right_wheel.get_degrees_spun())
    
    time.sleep(1)
    print()
    print("Spin clockwise at half speed for 1 seconds")
    robot.drive_system.move_for_seconds(1, 100, -100)

    print("Left/right wheel positions:",
          robot.drive_system.left_wheel.get_degrees_spun(),
          robot.drive_system.right_wheel.get_degrees_spun())

    robot.drive_system.left_wheel.reset_degrees_spun()
    robot.drive_system.right_wheel.reset_degrees_spun(2000)

    time.sleep(1)
    print()
    print("Move forward at full speed for 1.5 seconds, coast to stop")
    robot.drive_system.start_moving()
    time.sleep(1.5)
    robot.drive_system.stop_moving(rb.StopAction.COAST)

    print("Left/right wheel positions:",
          robot.drive_system.left_wheel.get_degrees_spun(),
          robot.drive_system.right_wheel.get_degrees_spun())

    """

    """
    while robot.drive_system.left_wheel.get_degrees_spun() < 360:
        robot.drive_system.move_for_seconds(0.001, 100, 100)
    print("Wheel spun 360 degrees: ")
    print(robot.drive_system.left_wheel.get_degrees_spun())
    """


    #Move forward for 1 second
    #robot.drive_system.move_for_seconds(1, 100, 100)

    #Move forward 10 inches at 50% speed
    #robot.drive_system.go_straight_inches(10,50)

    #Delay 5 seconds
    #time.sleep(5)

    # Move forward 5 inches
    #robot.drive_system.go_straight_inches(5)

    #Spin in place 90 degrees
    #robot.drive_system.spin_in_place_degrees(90)

    #Turn 180 degrees
    #robot.drive_system.turn_degrees(90)

def run_test_touch_sensor():
    """ Tests the  touch_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  touch_sensor  of the robot.")
    print("Repeatedly press and release the touch sensor.")
    print("Press Control-C when you are ready to stop testing.")
    time.sleep(1)
    count = 1
    while True:
        print("{:4}.".format(count),
              "Touch sensor value is: ", robot.touch_sensor.get_value())
        time.sleep(0.5)
        count = count + 1


def run_test_color_sensor():
    """ Tests the  color_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  color_sensor  of the robot.")
    print("Repeatedly move the robot to different surfaces.")
    print("Press Control-C when you are ready to stop testing.")
    time.sleep(1)
    count = 1
    while True:
        print("{:4}.".format(count),
              "Color sensor value/color/intensity is: ",
              "{:3} {:3} {:3}".format(robot.color_sensor.get_value()[0],
                                      robot.color_sensor.get_value()[1],
                                      robot.color_sensor.get_value()[2]),
              "{:4}".format(robot.color_sensor.get_color()),
              "{:4}".format(robot.color_sensor.get_reflected_intensity()))
        time.sleep(0.5)
        count = count + 1


main()
