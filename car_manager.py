from turtle import Turtle
import random

random.randint(-250, 250)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 15)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(COLORS[random.randint(0, 5)])
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.forward(self.move_speed)
            if car.xcor() < - 300:
                car.goto(300, random.randint(-250, 250))

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT


