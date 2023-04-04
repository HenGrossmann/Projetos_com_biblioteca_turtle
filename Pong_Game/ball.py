from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.speed('slow')
        self.shape('circle')
        
        self.y_move = 10
        self.x_move = 10

    def moving_ball(self):
        x,y = self.pos()
        x += self.x_move
        y += self.y_move
        self.goto(x,y)
        

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        if self.x_move >0:
            self.x_move +=5
        else:
            self.x_move -=5

    def reset(self,WIDTH):
        #right misses
        if self.xcor() > WIDTH/2-35:
            
            self.x_move = -10
            self.y_move = 10
            self.goto(0,0)
            return 'left'
        elif self.xcor()<-WIDTH/2+35:
            self.x_move = 10
            self.y_move = 10
            self.goto(0,0)
            return 'right'
        