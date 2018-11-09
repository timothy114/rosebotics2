"""
  Capstone Project.  Code written by Toluwa Nafiu.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time
# import tkinter
# from tkinter import ttk


def main():
    """ Runs YOUR specific part of the project """
    robot_stop_when_color(3)
    # camera_beep()
    # move_with_beacon_buttons()
    robot = rb.Snatch3rRobot()
    while True:
        time.sleep(0.01)  # For the delegate to do its work
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep(1).wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('Hi Tim')


def robot_stop_when_color(color):
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(50, 50)
    print(color)
    while True:
        if robot.color_sensor.get_color() == color:
            robot.drive_system.stop_moving()


def camera_beep():
    camera = rb.Camera()
    blob_area = camera.get_biggest_blob().get_area()
    print(blob_area)
    ev3.Sound.beep(1).wait()
    if blob_area >= 600:
        ev3.Sound.beep(1).wait()
    else:
        time.sleep(1)


def follow_line_color(color):
    print("follow " + color + "line")

"""
def move_with_beacon_buttons():
    robot = rb.Snatch3rRobot()
    window = tkinter.Tk()
    frame = ttk.Frame(window, padding=10)
    frame.grid()
    button1 = ttk.Button(window, text='Red Up Button')
    button2 = ttk.Button(window, text='Blue Up Button')
    button1.grid()
    button2.grid()

    if robot.beacon_button_sensor.is_top_red_button_pressed():
        print('move forward 11 inches')
        robot.drive_system.go_straight_inches(11)
    elif robot.beacon_button_sensor.is_top_blue_button_pressed():
        print('move backward 11 inches')
        robot.drive_system.go_straight_inches(-11)

    window.mainloop()

# Sprint 3 work


def sprint_three(robot):
    window = tkinter.Tk()
    frame = ttk.Frame(window, padding=10)
    frame.grid()
    button = ttk.Button(window, text='Go Forward')
    entry_box = ttk.Entry(frame)
    entry_box.grid()
    button.grid()
    button['command'] = lambda: go_forward(robot, entry_box)
"""

def go_forward(robot, entry_box):
    speed = int(entry_box.get())
    robot.drive_system.start_moving(speed, speed)


main()
