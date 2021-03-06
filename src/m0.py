"""
  Capstone Project.  Code for testing basics.
  Author:  David Mutchler, based on work by Dave Fisher and others.
  READ and RUN this module but ** DO NOT MODIFY IT. **
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
    run_test_drive_system()
    # run_test_touch_sensor()
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
    robot.drive_system.spin_in_place_degrees(360)
    #time.sleep(5)
    #robot.drive_system.spin_in_place_degrees(90)
    #time.sleep(5)
    #robot.drive_system.spin_in_place_degrees(45)
    #time.sleep(5)
    #robot.drive_system.spin_in_place_degrees(180)
    #time.sleep(5)


    #Turn 180 degrees
    #robot.drive_system.turn_degrees(90)


def run_test_touch_sensor():
    """ Tests the  touch_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    """
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
    """
    # Wait until the touch sensor is pressed
    robot.touch_sensor.wait_until_pressed()

    # Wait until the touch sensor is released
    robot.touch_sensor.wait_until_released()


def run_test_color_sensor():
    """ Tests the  color_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()
    """
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
    """

        # Test reading colors with light intensity < 30
    robot.drive_system.start_moving(5,5)
    robot.color_sensor.wait_until_intensity_is_less_than(30)
    robot.drive_system.stop_moving()

    """
        # Test reading colors with light intensity > 80
    robot.color_sensor.wait_until_intensity_is_greater_than(80)

        # Tests reading colors [green]
        robot.color_sensor.wait_until_color_is(3)

        # Tests reading colors [blue]
        robot.color_sensor.wait_until_color_is(2)

        # Tests reading colors [red]
        robot.color_sensor.wait_until_color_is(5)

        # Tests with one of the given colors is "read" [blue, green, red]
        colors = [2, 3, 1]
        robot.color_sensor.wait_until_color_is_one_of(colors)

        # Tests with one of the given colors is "read" [yellow, red, white]
        colors = [4, 5, 6]
        robot.color_sensor.wait_until_color_is_one_of(colors)
    """

main()
