import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():

    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    # mqtt_client.send_message('Your pizza is ready')

    # time.sleep(0.01)  # For the delegate to do its work
    # ev3.Sound.beep(1)
    # robot.drive_system.move_for_seconds()
    # ev3.Sound.speak("It's time for pizzaaaa!")


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        Stores a robot.
            :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def go_forward(self, sec_string, speed_string1, speed_string2):
        sec = int(sec_string)
        speed1 = int(speed_string1)
        speed2 = int(speed_string2)
        ev3.Sound.beep(1)
        self.robot.drive_system.move_for_seconds(sec, speed1, speed2)
        ev3.Sound.speak("It's time for pizzaaaa!")

main()