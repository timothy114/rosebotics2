"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Jess Thuer
"""
# ------------------------------------------------------------------------------
# DONE 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# DONE 2. With your instructor, review the "big picture" of laptop-robot
#     communication, per the comment in mqtt_sender.py.
#     Once you understand the "big picture", delete this.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # DONE 3. Construct a Snatch3rRobot.  Test.  When OK, delete this.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()

    # --------------------------------------------------------------------------
    # DONE 4. Add code that constructs a   com.MqttClient   that will
    #     be used to receive commands sent by the laptop.
    #     Connect it to this robot.  Test.  When OK, delete this.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    # --------------------------------------------------------------------------
    # DONE 5. Add a class for your "delegate" object that will handle messages
    #     sent from the laptop.  Construct an instance of the class and
    #     pass it to the MqttClient constructor above.  Augment the class
    #     as needed for that, and also to handle the go_forward message.
    #     Test by PRINTING, then with robot.  When OK, delete this.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # DONE 6. With your instructor, discuss why the following WHILE loop,
    #     that appears to do nothing, is necessary.
    #     When you understand this, delete this.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # DONE 7. Add code that makes the robot beep if the top-red button
        #     on the Beacon is pressed.  Add code that makes the robot
        #     speak "Hello. How are you?" if the top-blue button on the
        #     Beacon is pressed.  Test.  When done, delete this.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
            ev3.Sound.speak("It's time for pizzaaaa!")



class RemoteControlEtc(object):
    def __init__(self, robot):
        self.robot = robot
        """
        Stores a robot.
            :type robot: rb.Snatch3rRobot
        """

    def go_forward(self, speed_string):
        speed = int(speed_string)
        print('Robot should start moving.')
        self.robot.drive_system.start_moving(speed, speed)


main()