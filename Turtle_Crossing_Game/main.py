import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, SafeZone
s = Screen()
s.setup(width=600, height=600)
s.tracer(0)
p = Player()
c = CarManager()
b = Scoreboard()
z = SafeZone()

s.listen()
s.onkeypress(fun=p.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()
    c.generate_car()
    c.move_car()
    if p.finish_level():
        p.reset()
        c.next_level()
        b.level_up()
    for cars in c.car_list:
        if p.distance(cars) < 20:
            z.game_over()
            game_is_on = False
s.exitonclick()
