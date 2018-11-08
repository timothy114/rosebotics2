# Written by Timothy Li (Wei Jonah Li)

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():

    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    while True:

        time.sleep(0.01)  # For the delegate to do its work

        if robot.beacon_button_sensor.is_top_red_button_pressed():
            # Code for starting the sort
            print("Starting the sorting process")
            ev3.Sound.speak("Starting the sorting process")
            # Write code for this

        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak("Hello. How are you?")

class RemoteControlEtc(object):

    def __init__(self,robot):
        """
        Stores a robot.
        :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    # Number of boxes function
    def num_box_function(self,num_string):
        num_boxes = int(num_string)
        print("num_box_function running")
        for i in range(num_boxes):
            ev3.Sound.beep(1)
            time.sleep(1)

    # Start sort function
    def start_sort_function(self, ignore):
        print("Starting the sorting process...")

main()