"""
  Capstone Project.  Code written by Jess Thuer.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time

import tkinter
from tkinter import ttk
import rosegraphics as rg


"""
def follow_line(robot):
    while True:
        while robot.touch_sensor.get_value() == 0:
            spin = 1
            robot.color_sensor.wait_until_intensity_is_less_than(5)
            robot.drive_system.start_moving()
            robot.color_sensor.wait_until_intensity_is_greater_than(5)
            robot.drive_system.stop_moving()
            for k in range(360):
                if spin < 360:
                    robot.drive_system.spin_in_place_degrees(spin)
                    if robot.color_sensor.get_reflected_intensity() <= (5):
                        spin = spin + 360
                    spin = -spin * (-k+2)
        if robot.touch_sensor.wait_until_pressed():
            time.sleep(0.1)
            break
"""


def build_your_own_pizza():
    pizza_window = rg.RoseWindow(500, 500, 'Pizza Time!')
    Pizza = pizza()
    window = tkinter.Tk()
    frame = ttk.Frame(window, padding = 25)
    frame.grid()
    txt = rg.Text(rg.Point(250, 50), 'Choose your crust size')
    txt.attach_to(pizza_window)
    pizza_window.render()

    crust_button = ttk.Button(frame, text='Crust')
    crust_button['command'] = (lambda: Pizza.crust_frame(pizza_window, txt))
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

    bake_button = ttk.Button(frame, text='BAKE PIZZA')
    bake_button['command'] = (lambda: bake())
    bake_button.grid()

    # reset_button = ttk.Button(frame, text='Reset')
    # reset_button['command'] = (lambda: Pizza.reset(pizza_window))
    # reset_button.grid()

    # pizza_window.close_on_mouse_click()
    window.mainloop()


class pizza(object):
    def __init__(self):
        self.button_click_counter = 0
        self.ratio_number = 0
        self.num = 0
        self.cheese_color = 'tan'
        self.txt = ' '
        self.total = 0

    def crust_frame(self, pizza_window, txt):
        self.txt = str(txt)
        window = tkinter.Tk()
        frame = ttk.Frame(window, padding=25)
        frame.grid()

        small_button = ttk.Button(frame, text='Small (10")')
        small_button['command'] = (lambda: self.crust(pizza_window, 1, txt))
        small_button.grid()

        medium_button = ttk.Button(frame, text='Medium (13")')
        medium_button['command'] = (lambda: self.crust(pizza_window, 2, txt))
        medium_button.grid()

        large_button = ttk.Button(frame, text='Large (15")')
        large_button['command'] = (lambda: self.crust(pizza_window, 3, txt))
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

        pepperoni_button = ttk.Button(frame, text='Pepperoni')
        pepperoni_button['command'] = (lambda: self.toppings(pizza_window, 1))
        pepperoni_button.grid()

        sausage_button = ttk.Button(frame, text='Sausage')
        sausage_button['command'] = (lambda: self.toppings(pizza_window, 2))
        sausage_button.grid()

        ham_button = ttk.Button(frame, text='Ham')
        ham_button['command'] = (lambda: self.toppings(pizza_window, 3))
        ham_button.grid()

        chicken_button = ttk.Button(frame, text='Chicken')
        chicken_button['command'] = (lambda: self.toppings(pizza_window, 4))
        chicken_button.grid()

        anchovies_button = ttk.Button(frame, text='Anchovies')
        anchovies_button['command'] = (lambda: self.toppings(pizza_window, 5))
        anchovies_button.grid()

        tofu_button = ttk.Button(frame, text='Tofu')
        tofu_button['command'] = (lambda: self.toppings(pizza_window, 6))
        tofu_button.grid()

        green_pep_button = ttk.Button(frame, text='Green Peppers')
        green_pep_button['command'] = (lambda: self.toppings(pizza_window, 7))
        green_pep_button.grid()

        red_pep_button = ttk.Button(frame, text='Red Peppers')
        red_pep_button['command'] = (lambda: self.toppings(pizza_window, 8))
        red_pep_button.grid()

        tomatoes_button = ttk.Button(frame, text='Tomatoes')
        tomatoes_button['command'] = (lambda: self.toppings(pizza_window, 9))
        tomatoes_button.grid()

        onions_button = ttk.Button(frame, text='Onions')
        onions_button['command'] = (lambda: self.toppings(pizza_window, 10))
        onions_button.grid()

        olives_button = ttk.Button(frame, text='Olives')
        olives_button['command'] = (lambda: self.toppings(pizza_window, 11))
        olives_button.grid()

        pineapple_button = ttk.Button(frame, text='Pineapple')
        pineapple_button['command'] = (lambda: self.toppings(pizza_window, 12))
        pineapple_button.grid()

        spinach_button = ttk.Button(frame, text='Spinach')
        spinach_button['command'] = (lambda: self.toppings(pizza_window, 13))
        spinach_button.grid()

        mushroom_button = ttk.Button(frame, text='Mushrooms')
        mushroom_button['command'] = (lambda: self.toppings(pizza_window, 14))
        mushroom_button.grid()

    def crust(self, window, value, txt):
        if self.button_click_counter == 0:
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
            self.button_click_counter = self.button_click_counter + 1
            txt.detach_from(window)
            self.txt = rg.Text(rg.Point(250, 50), 'Choose your sauce')
            self.txt.attach_to(window)
            window.render()

    def sauce(self, window, value):
        if self.button_click_counter == 1:
            point = rg.Point(250, 250)
            radius = (self.ratio_number) - 15
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
            self.button_click_counter = self.button_click_counter + 1
            self.txt.detach_from(window)
            self.txt = rg.Text(rg.Point(250, 50), 'Choose your cheese')
            self.txt.attach_to(window)
            window.render()

    def cheese(self, window, value):
        if self.button_click_counter == 2:
            point = rg.Point(250, 250)
            radius = (self.ratio_number) - 20
            circle = rg.Circle(point, radius)
            if value == 1:
                circle.fill_color = 'light grey'
                self.cheese_color = 'light grey'
            if value == 2:
                circle.fill_color = 'orange'
                self.cheese_color = 'orange'
            if value == 3:
                circle.fill_color = 'light blue'
                self.cheese_color = 'light blue'
            if value == 4:
                circle.fill_color = 'light grey'
                self.cheese_color = 'light grey'
            if value == 5:
                circle.fill_color = 'light grey'
                self.cheese_color = 'light grey'
            circle.attach_to(window)
            window.render()
            self.button_click_counter = self.button_click_counter + 1
            self.txt.detach_from(window)
            self.txt = rg.Text(rg.Point(250, 50), 'Choose up to 4 toppings')
            self.txt.attach_to(window)
            window.render()

    def toppings(self, window, value):
        if self.button_click_counter >= 3:
            radius = int(self.ratio_number / 2)
            point = pt(radius, self.num)
            if value == 1:
                obj = rg.Circle(point, 12)
                obj.fill_color = 'dark red'
                obj.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 2:
                p1 = rg.Point(point.x, point.y + 4)
                p2 = rg.Point(point.x + 4, point.y - 2)
                p3 = rg.Point(point.x - 4, point.y - 4)
                obj1 = rg.Circle(p1, 8)
                obj2 = rg.Circle(p2, 8)
                obj3 = rg.Circle(p3, 8)
                obj1.fill_color = obj2.fill_color = obj3.fill_color = 'grey'
                obj1.attach_to(window)
                obj2.attach_to(window)
                obj3.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 3:
                obj = rg.Square(point, 24)
                obj.fill_color = 'pink'
                obj.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 4:
                p11 = rg.Point(point.x - 20, point.y - 10)
                p12 = rg.Point(point.x + 20, point.y + 10)
                obj1 = rg.Rectangle(p11, p12)
                obj1.fill_color = 'tan'
                obj1.attach_to(window)
                p21 = rg.Point(point.x - 16, point.y - 5)
                p22 = rg.Point(point.x + 16, point.y - 2)
                obj2 = rg.Rectangle(p21, p22)
                obj2.fill_color = 'black'
                obj2.attach_to(window)
                p31 = rg.Point(point.x - 16, point.y + 5)
                p32 = rg.Point(point.x + 16, point.y + 2)
                obj3 = rg.Rectangle(p31, p32)
                obj3.fill_color = 'black'
                obj3.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 5:
                p1 = rg.Point(point.x - 35, point.y)
                p2 = rg.Point(point.x, point.y - 15)
                obj = rg.Ellipse(p1, p2)
                obj.fill_color = 'grey'
                obj.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 6:
                obj = rg.Square(point, 24)
                obj.fill_color = 'tan'
                obj.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 7:
                p1 = rg.Point(point.x - 25, point.y - 5)
                p2 = rg.Point(point.x + 25, point.y + 5)
                obj = rg.Rectangle(p1, p2)
                obj.fill_color = 'dark green'
                obj.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 8:
                p1 = rg.Point(point.x - 25, point.y - 5)
                p2 = rg.Point(point.x + 25, point.y + 5)
                obj = rg.Rectangle(p1, p2)
                obj.fill_color = 'red'
                obj.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 9:
                obj = rg.Circle(point, 15)
                obj.fill_color = 'red'
                obj.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 10:
                p1 = rg.Point(point.x - 25, point.y - 5)
                p2 = rg.Point(point.x + 25, point.y + 5)
                obj = rg.Rectangle(p1, p2)
                obj.fill_color = 'purple'
                obj.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 11:
                obj = rg.Circle(point, 12)
                obj.fill_color = 'black'
                obj.attach_to(window)
                obj = rg.Circle(point, 7)
                obj.fill_color = self.cheese_color
                obj.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 12:
                p1 = rg.Point(point.x - 10, point.y - 15)
                p2 = rg.Point(point.x + 10, point.x + 10)
                obj = rg.Rectangle(p1, p2)
                obj.fill_color = 'yellow'
                obj.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 13:
                p1 = rg.Point(point.x - 30, point.y)
                p2 = rg.Point(point.x, point.y - 25)
                obj = rg.Ellipse(p1, p2)
                obj.fill_color = 'dark green'
                obj.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if value == 14:
                p21 = rg.Point(point.x - 25, point.y - 5)
                p22 = rg.Point(point.x - 5, point.y + 5)
                obj2 = rg.Rectangle(p21, p22)
                obj2.fill_color = 'grey'
                obj2.attach_to(window)
                p11 = rg.Point(point.x - 30, point.y)
                p12 = rg.Point(point.x, point.y - 25)
                obj1 = rg.Ellipse(p11, p12)
                obj1.fill_color = 'grey'
                obj1.attach_to(window)
                self.num = self.num + 1
                self.total = self.total + 1
                window.render()
            if self.total >=3:
                self.txt.detach_from(window)
                self.txt = rg.Text(rg.Point(250, 50), 'Bake your Pizza!')
                self.txt.attach_to(window)
                window.render()


def pt(radius, num):
    point = rg.Point(250, 250)
    if num == 0:
        ptt = rg.Point(point.x + radius, point.y)
        return ptt
    if num == 1:
        ptt = rg.Point(point.x, point.y + radius)
        return ptt
    if num == 2:
        ptt = rg.Point(point.x - radius, point.y)
        return ptt
    if num == 3:
        ptt = rg.Point(point.x, point.y - radius)
        return ptt

# def bake()
#     ...











def main():
    """ Runs YOUR specific part of the project """
    """
    robot = rb.Snatch3rRobot()
    follow_line(robot)
    """

    build_your_own_pizza()


main()
