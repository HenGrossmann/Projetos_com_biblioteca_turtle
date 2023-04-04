from turtle import Turtle
STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        self.current_direction = RIGHT


    def create_snake(self):
        for c in STARTING_POS:
            self.add_segment(c)
        
    def add_segment(self,position):
        snake = Turtle('square')
        snake.penup()
        snake.color('white')
        snake.goto(position)       
        self.snakes.append(snake)
    
    def extend(self):
        self.add_segment(self.snakes[-1].position())
        
    
    
    def move(self):
        
        for seg_num in range(len(self.snakes)-1,0,-1):
            new_x = self.snakes[seg_num-1].xcor()
            new_y = self.snakes[seg_num-1].ycor()
            self.snakes[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading()!=UP:
            
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)