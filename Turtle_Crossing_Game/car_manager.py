from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.generate_car()

    def generate_car(self):
        # This means every 6 cycles about 1 car will generate
        car_frequency = random.randint(1, 6)
        if car_frequency == 1:
            t = Turtle("square")
            t.shapesize(stretch_wid=1, stretch_len=2)
            t.color(random.choice(COLORS))
            t.setheading(180)
            t.penup()
            t.setpos(300, random.randint(-240, 240))
            self.car_list.append(t)

    def move_car(self):
        for cars in self.car_list:
            cars.forward(self.move_speed)

    def next_level(self):
        self.move_speed += MOVE_INCREMENT





