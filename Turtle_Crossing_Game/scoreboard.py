from turtle import Turtle
SCORE_FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Algerian", 24, "bold")


class SafeZone(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.draw_safe_zone(-250)
        self.draw_safe_zone(250)

    def draw_safe_zone(self, y_cor):
        self.penup()
        self.setpos(-300, y_cor)
        self.pendown()
        self.forward(600)

    def game_over(self):
        self.penup()
        self.home()
        self.pendown()
        self.color("red")
        self.write(arg=f"Game Over!", align="center", font=GAME_OVER_FONT)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.score()

    def score(self):
        self.clear()
        self.penup()
        self.setpos(-230, 260)
        self.write(arg=f"Level {self.level}", align="center", font=SCORE_FONT)

    def level_up(self):
        self.level += 1
        self.score()

