# Written by Timothy Li (Wei Jonah Li)

import tkinter
from tkinter import ttk
from tkinter import *
import mqtt_remote_method_calls as com

def main():
    # Making a GUI
    root = tkinter.Tk()

    # mqtt stuff
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    # Setting up the GUI
    setup_gui(root,mqtt_client)

    # Running the GUI
    root.mainloop()

# Set up GUI
def setup_gui(root_window,mqtt_client):

    """ Constructs and sets up widgets on the given window. """

    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    # Number of boxes entry
    num_boxes_entry = (ttk.Entry(frame))
    num_boxes_entry.grid()

    # Start sorting button
    start_sort_button = ttk.Button(frame, text="Start Sorting")
    start_sort_button.grid()
    start_sort_button['command'] = \
        lambda: start_sort_function(mqtt_client,check_val)

    # Num boxes button
    num_boxes_button = ttk.Button(frame, text="Get number of boxes")
    num_boxes_button.grid()
    num_boxes_button['command'] = \
        lambda: num_box_function(mqtt_client,num_boxes_entry)

    # Making a checkbox
    check_val = IntVar()
    check_1 = Checkbutton(root_window, text="Place on right", variable=check_val, \
                     onvalue=1, offvalue=0)
    check_1.grid()


# Number of boxes function
def num_box_function(mqtt_client,num_boxes_entry):
    # Function for the number of boxes

    # Get the number of boxes from the entry
    num_boxes_str = num_boxes_entry.get()

    # Prints the number of boxes to sort
    print("There are " + str(num_boxes_str) + " boxes to sort")

    # Sends the number of boxes to the other file
    mqtt_client.send_message('num_box_function',[num_boxes_str])

# Starting the sort function
def start_sort_function(mqtt_client,check_val):

    # Getting the check button place on right stuff
    place_on_right = check_val.get()
    print("The check box value is: " + str(place_on_right))

    # This is the program to start sorting
    mqtt_client.send_message('start_sort_function', [place_on_right])


main()
