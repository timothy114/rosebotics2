import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time
import mqtt_remote_method_calls as com


def main():
    robot = rb.Snatch3rRobot()
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    while True:
        time.sleep(0.01)  # Gives time for the delegate to do its work


class RemoteControlEtc(object):

    def __init__(self, robot):
        """
        Stores a robot.
            :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def robot_beep(self):
        ev3.Sound.beep(1).wait()

    def robot_greeting(self):
        ev3.Sound.speak('Hi, how are you?')

    def find_line(self, speed_string, color_string, mqtt_client):
        speed = int(speed_string)
        color = int(color_string)
        print('Robot should start moving')
        self.robot.drive_system.start_moving(speed, speed)
        while True:
            if self.robot.color_sensor.get_color() == color:
                self.robot.drive_system.stop_moving()
                self.find_home(mqtt_client)
                break
            else:
                print(self.robot.color_sensor.get_reflected_intensity())
                if self.robot.color_sensor.get_reflected_intensity() <= 5:
                    self.robot.drive_system.start_moving(speed, speed)
                else:
                    self.robot.drive_system.start_moving(100, 15)

    def find_home(self, mqtt_client):
        message = "We made it!"
        mqtt_client.send_message('handle_found_home', [message])



main()
