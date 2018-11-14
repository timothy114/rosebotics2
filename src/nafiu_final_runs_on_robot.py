import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time
import mqtt_remote_method_calls as com


def main():
    robot = rb.Snatch3rRobot()
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    # mqtt_client.find_home()
    while True:
        time.sleep(0.01)  # Gives time for the delegate to do its work
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep(1).wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('Hi, how are you?')


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

    def find_line(self, speed_string, color_string):
        speed = int(speed_string)
        color = int(color_string)
        print('Robot should start moving')
        self.robot.drive_system.start_moving(speed, speed)
        while True:
            if self.robot.color_sensor.get_color() == color:
                self.robot.drive_system.stop_moving()
                break
            else:
                while self.robot.touch_sensor.get_value() == 0:
                    spin = 1
                    self.robot.color_sensor.wait_until_intensity_is_less_than(5)
                    self.robot.drive_system.start_moving()
                    self.robot.color_sensor.wait_until_intensity_is_greater_than(5)
                    self.robot.drive_system.stop_moving()
                    for k in range(360):
                        if spin < 360:
                            self.robot.drive_system.spin_in_place_degrees(spin)
                            if self.robot.color_sensor.get_reflected_intensity() <= (5):
                                spin = spin + 360
                            spin = -spin * (-k + 2)

    def find_home(self, mqtt_client):
        while True:
            while self.robot.touch_sensor.get_value() == 0:
                spin = 1
                self.robot.color_sensor.wait_until_intensity_is_less_than(5)
                self.robot.drive_system.start_moving()
                self.robot.color_sensor.wait_until_intensity_is_greater_than(5)
                self.robot.drive_system.stop_moving()
                for k in range(360):
                    if spin < 360:
                        self.robot.drive_system.spin_in_place_degrees(spin)
                        if self.robot.color_sensor.get_reflected_intensity() <= (5):
                            spin = spin + 360
                        spin = -spin * (-k + 2)
            if self.robot.camera:
                time.sleep(0.1)
                # mqtt_client.send_message('handle_found_home', [])
                break


main()
