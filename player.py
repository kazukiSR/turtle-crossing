from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEADING = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(HEADING)

    def move(self):
        newY = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), newY)

    def checkGoal(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goal()
            return True
        return False

    def goal(self):
        self.goto(STARTING_POSITION)

