# 100 Days of Code
# Turtle Crossing Game

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

turt = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(turt.move_up, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.drive()
    car_manager.create_car()

    # detect car collision
    for car in car_manager.all_cars:
        if car.distance(turt) < 17:
            score.game_over()
            game_is_on = False

    # new level
    if turt.ycor() > 280:
        score.new_level()
        turt.level_up()
        car_manager.speed_up()

screen.exitonclick()
