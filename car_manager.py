from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
HEADING = 180
XSTART = 340
WIDTH = 1
LENGTH = 2


class CarManager():

    def __init__(self):
        self.carList = []
        self.moveDistance = STARTING_MOVE_DISTANCE

    def createCar(self):
        newCar = Turtle(shape="square")
        newCar.color(random.choice(COLORS))
        newCar.penup()
        newCar.setheading(HEADING)
        newCar.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        newCar.goto(XSTART, random.randint(-250, 250))
        self.carList.append(newCar)

    def move(self):
        for car in self.carList:
            car.forward(self.moveDistance)

    def delCar(self):
        for i in range(len(self.carList)-1, 0, -1):  # iterating in reverse
            if self.carList[i].xcor() < -340:
                self.carList.pop(i)

    def increaseSpeed(self):
        self.moveDistance += MOVE_INCREMENT

