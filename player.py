from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 12
FINISH_LINE_y = 280
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
    def go_up(self):

        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)














