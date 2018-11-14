import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    root.title('Ready for user input!')
    root.geometry('500x300')

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui_line_following(root, mqtt_client)
    setup_gui_remote_control(root, mqtt_client)
    # handle_found_home()

    root.mainloop()


def setup_gui_line_following(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()
    style1 = ttk.Style()
    style1.configure("TButton", foreground="green", background="red")

    speed_entry_box = ttk.Entry(frame)
    color_entry_box = ttk.Entry(frame)
    speed_color_button = ttk.Button(frame, text="Enter color, speed and GO!", style="TButton")
    text = tkinter.Text(root_window, height=3, width=50)
    text.insert(tkinter.INSERT, " Every color has a corresponding number so please\n"
                                " enter the NUMBER for the color you want:"
                                "\n BLUE = 2, GREEN = 3, YELLOW = 4, RED = 5")
    text.config(state='disabled')
    text.grid()

    speed_entry_box.grid()
    color_entry_box.grid()
    speed_color_button.grid()

    speed_color_button['command'] = \
        lambda: handle_find_line(speed_entry_box, color_entry_box, mqtt_client)


def setup_gui_remote_control(root_window, mqtt_client):
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    beep_button = ttk.Button(frame, text="Beep")
    greet_button = ttk.Button(frame, text="Greeting")
    beep_button.grid()
    greet_button.grid()

    beep_button['command'] = lambda: handle_robot_beep(mqtt_client)
    greet_button['command'] = lambda: handle_robot_greeting(mqtt_client)


def handle_robot_beep(mqtt_client):
    mqtt_client.send_message('robot_beep', [])


def handle_robot_greeting(mqtt_client):
    mqtt_client.send_message('robot_greeting', [])


def handle_find_line(entry_box1, entry_box2, mqtt_client):
    """
    Tells the robot to go forward at the speed specified in the given entry box and to find the starting point with the
    specific color.
    """
    speed = entry_box1.get()
    color = entry_box2.get()
    print("Sending 'find_line' to the robot with a speed of", speed, "and a color of", color)
    mqtt_client.send_message('find_line', [speed, color])


def handle_found_home():
    # constructs the window for the final "home" screen
    window = tkinter.Tk()
    window.configure(background='yellow')
    window.title("Home!")
    window.geometry("300x300")
    window.configure(background='grey')

    path = "welcome_home.gif"

    # makes a Tkinter photo image
    image = tkinter.PhotoImage(file=path)
    image

    # The Label widget is used to display the image on the window
    label = ttk.Label(window, image=image)

    # The Pack manger packs the image and any text together
    label.pack(side="bottom", fill="both", expand="yes")

    # used to start the GUI running
    window.mainloop()


main()
