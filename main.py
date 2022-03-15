import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "w")

loopTracker = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.delCar()
    if loopTracker % 5 == 0:
        carManager.createCar()
    # Turtle Goal
    if player.checkGoal():
        carManager.increaseSpeed()
        scoreboard.increase_score()

    for car in carManager.carList:
        absY = abs(car.ycor() - player.ycor())
        absX = abs(car.xcor())
        if absY < 18 and absX <= 20:
            game_is_on = False
            scoreboard.game_over()


    # Car move
    carManager.move()
    loopTracker += 1


screen.exitonclick()
