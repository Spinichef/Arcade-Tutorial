import arcade

def test():

    user_name = (input("What is your name? "))
    if user_name.lower() == "jonas":
        print("You have a good name!")
    elif user_name.lower() == "bene" or user_name.lower() == "benedikt":
        print("You have a bad name!")
    elif user_name.lower() == "fickdich" or user_name.lower() == "fick dich":
        for i in range(5):
            print("Bene sei leise.")
    else:
        print("You have an ok name!")

def test2():
    for i in range(10):
        for j in range(10):
            print("Bene sei leise.")








SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ball:
    def __init__(self):
        # --- Class Attributes ---
        # Ball position
        self.x = 0
        self.y = 0

        # Ball's vector
        self.change_x = 0
        self.change_y = 0

        # Ball size
        self.size = 10

        # Ball color
        self.color = [255, 255, 255]

    # --- Class Methods ---
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color )

def on_draw(delta_time):

    arcade.start_render()
    draw_sky()
    the_ball.draw()
    the_ball.move()

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,)

def draw_sky():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def main():
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()

the_ball = Ball()
the_ball.x = 100
the_ball.y = 100
the_ball.change_x = 2
the_ball.change_y = 1
the_ball.color = [255, 0, 0]




class Person:
        def __init__(self):
            self.name = ""
            self.money = 0

def main2():
    bob = Person()
    bob.name = "Bob"
    bob.money = 100

    nancy = bob
    nancy.name = "Nancy"

    print(bob.name, "has", bob.money, "dollars.")
    print(nancy.name, "has", nancy.money, "dollars.")

test2()