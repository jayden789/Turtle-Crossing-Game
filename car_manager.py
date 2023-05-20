from turtle import Turtle
from random import choice


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 15
Y_RANGE = []
for y1 in range(-250, 250):
    Y_RANGE.append(y1)
for y2 in range(400, 3000):
    Y_RANGE.append(y2)

X_RANGE = []
for x_range in range(300, 1500, 100):
    X_RANGE.append(x_range)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.moving = STARTING_MOVE_DISTANCE
        self.car_list = []

    def create_car(self):
        car_unit = Turtle()
        car_unit.penup()
        car_unit.shape("square")
        car_unit.shapesize(stretch_wid=1, stretch_len=2)
        car_unit.color(choice(COLORS))
        car_unit.goto(choice(X_RANGE), choice(Y_RANGE))
        self.car_list.append(car_unit)

    def speeding(self):
        self.moving += STARTING_MOVE_DISTANCE

    def driving(self):
        for car in self.car_list:
            car.setheading(180)
            car.forward(self.moving)

