from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.new()

    def move(self):
        self.forward(10)

    def finish_level(self):
        if self.ycor() > 280:
            return True

    def reset(self):
        self.setpos(STARTING_POSITION)

    def new(self):
        self.shape("turtle")
        self.pencolor("green")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)




