import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)

    root.mainloop()


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    color_entry_box = ttk.Entry(frame)
    speed_button = ttk.Button(frame, text="Enter speed")
    follow_color_button = ttk.Button(frame, text="Enter color")
    beep_button = ttk.Button(frame, text="Beep")
    greet_button = ttk.Button(frame, text="Greeting")

    speed_entry_box.grid()
    speed_button.grid()
    color_entry_box.grid()
    follow_color_button.grid()
    beep_button.grid()
    greet_button.grid()
    """
    How do I send BOTH the color and the speed data to 'handle_find_line'? I want 'handle_find_line' to receive the speed
    value when the speed button is pressed and the color value when the color is pressed but I don't want it to run the 
    program both times.
    """
    speed_button['command'] = \
        lambda: handle_find_line(speed_entry_box, color_entry_box, mqtt_client)
    follow_color_button['command'] = \
        lambda: handle_find_line(speed_entry_box,color_entry_box, mqtt_client)


def handle_find_line(entry_box1, entry_box2, mqtt_client):
    """
    Tells the robot to go forward at the speed specified in the given entry box and to find the starting point with the
    specific color.
    """
    speed = entry_box1.get()
    color = entry_box2.get()
    print("Sending 'find_line' to the robot with a speed of", speed, "and a color of", color)
    mqtt_client.send_message('find_line', [speed, color])


main()