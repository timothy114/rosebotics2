"""
  Capstone Project.  Code written by Jess Thuer.
  Fall term, 2018-2019.
"""

# import rosebotics_even_newer as rb
# import time
import tkinter
from tkinter import ttk
import rosegraphics as rg

def follow_line(robot):
    while True:
        while robot.touch_sensor.get_value() == 0:
            spin = 5
            robot.color_sensor.wait_until_intensity_is_greater_than(95)
            robot.drive_system.start_moving()
            robot.color_sensor.wait_until_intensity_is_less_than(95)
            robot.drive_system.stop_moving()
            for k in range(360):
                if spin < 360:
                    robot.drive_system.spin_in_place_degrees(spin)
                    if robot.color_sensor.get_reflected_intensity() >= (95):
                        spin = spin + 360
                    spin = spin * (-k+2)
        if robot.touch_sensor.wait_until_pressed():
            break



def build_your_own_pizza():
    pizza_window = rg.RoseWindow(500, 500, 'Pizza Time!')
    Pizza = pizza()
    window = tkinter.Tk()
    frame = ttk.Frame(window, padding=25)
    frame.grid()

    crust_button = ttk.Button(frame, text='Crust')
    crust_button['command'] = (lambda: Pizza.crust_frame(pizza_window))
    crust_button.grid()

    sauce_button = ttk.Button(frame, text='Sauce')
    sauce_button['command'] = (lambda: Pizza.sauce_frame(pizza_window))
    sauce_button.grid()

    cheese_button = ttk.Button(frame, text='Cheese')
    cheese_button['command'] = (lambda: Pizza.cheese_frame(pizza_window))
    cheese_button.grid()

    toppings_button = ttk.Button(frame, text='Toppings')
    toppings_button['command'] = (lambda: Pizza.toppings_frame(pizza_window))
    toppings_button.grid()

    pizza_window.close_on_mouse_click()
    window.mainloop()

class pizza(object):
    def __init__(self):
        self.counter = 0
        self.ratio_number = 0

    def crust_frame(self, pizza_window):
        window = tkinter.Tk()
        frame = ttk.Frame(window, padding=25)
        frame.grid()

        small_button = ttk.Button(frame, text='Small (10")')
        small_button['command'] = (lambda: self.crust(pizza_window, 1))
        small_button.grid()

        medium_button = ttk.Button(frame, text='Medium (13")')
        medium_button['command'] = (lambda: self.crust(pizza_window, 2))
        medium_button.grid()

        large_button = ttk.Button(frame, text='Large (15")')
        large_button['command'] = (lambda: self.crust(pizza_window, 3))
        large_button.grid()

    def sauce_frame(self, pizza_window):
        window = tkinter.Tk()
        frame = ttk.Frame(window, padding=25)
        frame.grid()

        marinara_button = ttk.Button(frame, text='Marinara')
        marinara_button['command'] = (lambda: self.sauce(pizza_window, 1))
        marinara_button.grid()

        barbeque_button = ttk.Button(frame, text='Barbeque')
        barbeque_button['command'] = (lambda: self.sauce(pizza_window, 2))
        barbeque_button.grid()

        pesto_button = ttk.Button(frame, text='Pesto')
        pesto_button['command'] = (lambda: self.sauce(pizza_window, 3))
        pesto_button.grid()

        alfredo_button = ttk.Button(frame, text='Alfredo')
        alfredo_button['command'] = (lambda: self.sauce(pizza_window, 4))
        alfredo_button.grid()

    def cheese_frame(self, pizza_window):
        window = tkinter.Tk()
        frame = ttk.Frame(window, padding=25)
        frame.grid()

        mozz_button = ttk.Button(frame, text='Mozzarella')
        mozz_button['command'] = (lambda: self.cheese(pizza_window, 1))
        mozz_button.grid()

        ched_button = ttk.Button(frame, text='Cheddar')
        ched_button['command'] = (lambda: self.cheese(pizza_window, 2))
        ched_button.grid()

        blue_button = ttk.Button(frame, text='Blue Cheese')
        blue_button['command'] = (lambda: self.cheese(pizza_window, 3))
        blue_button.grid()

        gouda_button = ttk.Button(frame, text='Gouda')
        gouda_button['command'] = (lambda: self.cheese(pizza_window, 4))
        gouda_button.grid()

        ricotta_button = ttk.Button(frame, text='Ricotta')
        ricotta_button['command'] = (lambda: self.cheese(pizza_window, 5))
        ricotta_button.grid()

    def toppings_frame(self, pizza_window):
        window = tkinter.Tk()
        frame = ttk.Frame(window, padding=25)
        frame.grid()

        meats_button = ttk.Button(frame, text='Meats')
        meats_button['command'] = (lambda: self.meats_frame(pizza_window))
        meats_button.grid()

        vegetables_button = ttk.Button(frame, text='Vegetables')
        vegetables_button['command'] = (lambda: self.vegetables_frame(pizza_window))
        vegetables_button.grid()

    def meats_frame(self, pizza_window):
        window = tkinter.Tk()
        frame = ttk.Frame(window, padding=25)
        frame.grid()

        pepperoni_button = ttk.Button(frame, text='Pepperoni')
        pepperoni_button['command'] = (lambda: self.meats(pizza_window, 1))
        pepperoni_button.grid()

        sausage_button = ttk.Button(frame, text='Sausage')
        sausage_button['command'] = (lambda: self.meats(pizza_window, 2))
        sausage_button.grid()

        ham_button = ttk.Button(frame, text='Ham')
        ham_button['command'] = (lambda: self.meats(pizza_window, 3))
        ham_button.grid()

        chicken_button = ttk.Button(frame, text='Chicken')
        chicken_button['command'] = (lambda: self.meats(pizza_window, 4))
        chicken_button.grid()

        anchovies_button = ttk.Button(frame, text='Anchovies')
        anchovies_button['command'] = (lambda: self.meats(pizza_window, 5))
        anchovies_button.grid()

        tofu_button = ttk.Button(frame, text='Tofu')
        tofu_button['command'] = (lambda: self.meats(pizza_window, 6))
        tofu_button.grid()

    def vegetables_frame(self, pizza_window):
        window = tkinter.Tk()
        frame = ttk.Frame(window, padding=25)
        frame.grid()

        green_pep_button = ttk.Button(frame, text='Green Peppers')
        green_pep_button['command'] = (lambda: self.vegetables(pizza_window, 1))
        green_pep_button.grid()

        red_pep_button = ttk.Button(frame, text='Red Peppers')
        red_pep_button['command'] = (lambda: self.vegetables(pizza_window, 2))
        red_pep_button.grid()

        tomatoes_button = ttk.Button(frame, text='Tomatoes')
        tomatoes_button['command'] = (lambda: self.vegetables(pizza_window, 3))
        tomatoes_button.grid()

        onions_button = ttk.Button(frame, text='Onions')
        onions_button['command'] = (lambda: self.vegetables(pizza_window, 4))
        onions_button.grid()

        olives_button = ttk.Button(frame, text='Olives')
        olives_button['command'] = (lambda: self.vegetables(pizza_window, 5))
        olives_button.grid()

        pineapple_button = ttk.Button(frame, text='Pineapple')
        pineapple_button['command'] = (lambda: self.vegetables(pizza_window, 6))
        pineapple_button.grid()

        spinach_button = ttk.Button(frame, text='Spinach')
        spinach_button['command'] = (lambda: self.vegetables(pizza_window, 7))
        spinach_button.grid()

        mushroom_button = ttk.Button(frame, text='Mushrooms')
        mushroom_button['command'] = (lambda: self.vegetables(pizza_window, 8))
        mushroom_button.grid()

    def crust(self, window, value):
        if self.counter == 0:
            point = rg.Point(250, 250)
            radius = 0
            if value == 1:
                radius = 100
                self.ratio_number = 100
            if value == 2:
                radius = 130
                self.ratio_number = 130
            if value == 3:
                radius = 150
                self.ratio_number = 150
            circle = rg.Circle(point, radius)
            circle.fill_color = 'tan'
            circle.attach_to(window)
            window.render()
        self.counter = self.counter + 1

    def sauce(self, window, value):
        if self.counter == 1:
            point = rg.Point(250, 250)
            radius = (self.ratio_number) - 10
            circle = rg.Circle(point, radius)
            if value == 1:
                circle.fill_color = 'red'
            if value == 2:
                circle.fill_color = 'brown'
            if value == 3:
                circle.fill_color = 'green'
            if value == 4:
                circle.fill_color = 'white'
            circle.attach_to(window)
            window.render()
        self.counter = self.counter + 1







# def crust_frame(pizza_window):
#     window = tkinter.Tk()
#     frame = ttk.Frame(window, padding = 25)
#     frame.grid()
#
#     small_button = ttk.Button(frame, text = 'Small (10")')
#     small_button['command'] = (lambda: crust(pizza_window, 1))
#     small_button.grid()
#
#     medium_button = ttk.Button(frame, text = 'Medium (13")')
#     medium_button['command'] = (lambda: crust(pizza_window, 2))
#     medium_button.grid()
#
#     large_button = ttk.Button(frame, text = 'Large (15")')
#     large_button['command'] = (lambda: crust(pizza_window, 3))
#     large_button.grid()
#
# def sauce_frame(pizza_window):
#     window = tkinter.Tk()
#     frame = ttk.Frame(window, padding = 25)
#     frame.grid()
#
#     marinara_button = ttk.Button(frame, text = 'Marinara')
#     marinara_button['command'] = (lambda: sauce(pizza_window, 1))
#     marinara_button.grid()
#
#     barbeque_button = ttk.Button(frame, text = 'Barbeque')
#     barbeque_button['command'] = (lambda: sauce(pizza_window, 2))
#     barbeque_button.grid()
#
#     pesto_button = ttk.Button(frame, text = 'Pesto')
#     pesto_button['command'] = (lambda: sauce(pizza_window, 3))
#     pesto_button.grid()
#
#     alfredo_button = ttk.Button(frame, text = 'Alfredo')
#     alfredo_button['command'] = (lambda: sauce(pizza_window, 4))
#     alfredo_button.grid()
#
# def cheese_frame(pizza_window):
#     window = tkinter.Tk()
#     frame = ttk.Frame(window, padding = 25)
#     frame.grid()
#
#     mozz_button = ttk.Button(frame, text = 'Mozzarella')
#     mozz_button['command'] = (lambda: cheese(pizza_window, 1))
#     mozz_button.grid()
#
#     ched_button = ttk.Button(frame, text = 'Cheddar')
#     ched_button['command'] = (lambda: cheese(pizza_window, 2))
#     ched_button.grid()
#
#     blue_button = ttk.Button(frame, text = 'Blue Cheese')
#     blue_button['command'] = (lambda: cheese(pizza_window, 3))
#     blue_button.grid()
#
#     gouda_button = ttk.Button(frame, text = 'Gouda')
#     gouda_button['command'] = (lambda: cheese(pizza_window, 4))
#     gouda_button.grid()
#
#     ricotta_button = ttk.Button(frame, text = 'Ricotta')
#     ricotta_button['command'] = (lambda: cheese(pizza_window, 5))
#     ricotta_button.grid()
#
# def toppings_frame(pizza_window):
#     window = tkinter.Tk()
#     frame = ttk.Frame(window, padding = 25)
#     frame.grid()
#
#     meats_button = ttk.Button(frame, text = 'Meats')
#     meats_button['command'] = (lambda: meats_frame(pizza_window))
#     meats_button.grid()
#
#     vegetables_button = ttk.Button(frame, text = 'Vegetables')
#     vegetables_button['command'] = (lambda: vegetables_frame(pizza_window))
#     vegetables_button.grid()
#
# def meats_frame(pizza_window):
#     window = tkinter.Tk()
#     frame = ttk.Frame(window, padding = 25)
#     frame.grid()
#
#     pepperoni_button = ttk.Button(frame, text = 'Pepperoni')
#     pepperoni_button['command'] = (lambda: meats(pizza_window, 1))
#     pepperoni_button.grid()
#
#     sausage_button = ttk.Button(frame, text = 'Sausage')
#     sausage_button['command'] = (lambda: meats(pizza_window, 2))
#     sausage_button.grid()
#
#     ham_button = ttk.Button(frame, text = 'Ham')
#     ham_button['command'] = (lambda: meats(pizza_window, 3))
#     ham_button.grid()
#
#     chicken_button = ttk.Button(frame, text = 'Chicken')
#     chicken_button['command'] = (lambda: meats(pizza_window, 4))
#     chicken_button.grid()
#
#     anchovies_button = ttk.Button(frame, text = 'Anchovies')
#     anchovies_button['command'] = (lambda: meats(pizza_window, 5))
#     anchovies_button.grid()
#
#     tofu_button = ttk.Button(frame, text = 'Tofu')
#     tofu_button['command'] = (lambda: meats(pizza_window, 6))
#     tofu_button.grid()
#
# def vegetables_frame(pizza_window):
#     window = tkinter.Tk()
#     frame = ttk.Frame(window, padding = 25)
#     frame.grid()
#
#     green_pep_button = ttk.Button(frame, text = 'Green Peppers')
#     green_pep_button['command'] = (lambda: vegetables(pizza_window, 1))
#     green_pep_button.grid()
#
#     red_pep_button = ttk.Button(frame, text = 'Red Peppers')
#     red_pep_button['command'] = (lambda: vegetables(pizza_window, 2))
#     red_pep_button.grid()
#
#     tomatoes_button = ttk.Button(frame, text = 'Tomatoes')
#     tomatoes_button['command'] = (lambda: vegetables(pizza_window, 3))
#     tomatoes_button.grid()
#
#     onions_button = ttk.Button(frame, text = 'Onions')
#     onions_button['command'] = (lambda: vegetables(pizza_window, 4))
#     onions_button.grid()
#
#     olives_button = ttk.Button(frame, text = 'Olives')
#     olives_button['command'] = (lambda: vegetables(pizza_window, 5))
#     olives_button.grid()
#
#     pineapple_button = ttk.Button(frame, text = 'Pineapple')
#     pineapple_button['command'] = (lambda: vegetables(pizza_window, 6))
#     pineapple_button.grid()
#
#     spinach_button = ttk.Button(frame, text = 'Spinach')
#     spinach_button['command'] = (lambda: vegetables(pizza_window, 7))
#     spinach_button.grid()
#
#     mushroom_button = ttk.Button(frame, text = 'Mushrooms')
#     mushroom_button['command'] = (lambda: vegetables(pizza_window, 8))
#     mushroom_button.grid()
#
# def crust(window, value):
#     point = rg.Point(250, 250)
#     radius = 0
#     if value == 1:
#         radius = 100
#     if value == 2:
#         radius = 130
#     if value == 3:
#         radius = 150
#     circle = rg.Circle(point, radius)
#     circle.fill_color = 'tan'
#     circle.attach_to(window)
#     window.render()
#
# def sauce(window, value):
#     point = rg.Point(250, 250)
#     circle = rg.Circle(point, 100)
#     if value == 1:
#         circle.fill_color = 'red'
#     if value == 2:
#         circle.fill_color = 'brown'
#     if value == 3:
#         circle.fill_color = 'green'
#     if value == 4:
#         circle.fill_color = 'white'
#     circle.attach_to(window)
#     window.render()





def main():
    """ Runs YOUR specific part of the project """
    # robot = rb.Snatch3rRobot()
    # follow_line(robot)
    build_your_own_pizza()


main()
