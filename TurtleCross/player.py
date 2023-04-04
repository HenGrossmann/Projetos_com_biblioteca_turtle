from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
        self.forwardspeed = 15
        self.won = False
    def move(self):
        
        
        
        distance_to_top = 280 - self.ycor()
        if distance_to_top < self.forwardspeed:
            self.goto(0,280)
            self.reset()
        else:
            self.forward(self.forwardspeed)
        
        

    def reset(self):
        self.goto(0,-280)
        self.won = True
        