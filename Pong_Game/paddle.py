from turtle import Turtle,ontimer
SPEED = 15
going = 'up'
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed('fastest')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.shape("square")
        self.setheading(90)
        self.penup()
        

    def move_up(self):
        self.setheading(90)
        self.forward(SPEED)
          
    def move_down(self):
        self.setheading(270)
        self.forward(SPEED)
         
    def robot_paddle(self,HEIGHT,speed):
        global going
       
        if self.ycor() <= HEIGHT /2-50 and going == 'up':
            self.setheading(90)
            distance_to_top = HEIGHT/2 - self.ycor() - 50  # distance from paddle to top edge of screen
            forward_amount = speed  # amount to move the paddle forward
            if distance_to_top < forward_amount:  # if moving forward would go off the screen
                forward_amount = distance_to_top  # set the forward amount to the distance to the top
            self.forward(forward_amount)
            if self.ycor() == HEIGHT /2-50:
                going='down'
        

        elif self.ycor() >= -HEIGHT/2+50 and going == 'down':
            self.setheading(270)
            distance_to_bottom = distance_to_bottom =  HEIGHT/2 + self.ycor() - 50  
            forward_amount = speed  # amount to move the paddle forward
            
            if distance_to_bottom < forward_amount:  # if moving forward would go off the screen
                forward_amount = distance_to_bottom  # set the forward amount to the distance to the top
            print(forward_amount)
            self.forward(forward_amount)
            if self.ycor() == -HEIGHT/2+50:
                going = 'up'