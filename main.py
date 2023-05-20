import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

image = "space.gif"

screen = Screen()
screen.bgpic(image)
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")

screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

car = CarManager()
score = Scoreboard()

while game_is_on:
    car.create_car()
    car.driving()
    time.sleep(0.04)
    screen.update()
    if player.ycor() >= player.finish_line:
        player.starting_point()
        car.speeding()
        score.level_up()
        score.high_level()

    for car_unit in car.car_list:
        if player.distance(car_unit) < 26 and car_unit.xcor() not in range(-10, 10) or player.distance(car_unit) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
