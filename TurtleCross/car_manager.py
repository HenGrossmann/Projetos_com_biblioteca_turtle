from turtle import Turtle,register_shape
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
rectangle_coords = ((-10, -30), (-10, 30), (10, 30), (10, -30))

register_shape("rectangle", rectangle_coords)
def increase_speed(car_list):
        for c in car_list:
            c.min_speed +=3
            c.max_speed +=3

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color_choice = random.choice(COLORS)
        self.color(self.color_choice)
        self.penup()
        self.shape('rectangle')
        self.min_speed = 5
        self.max_speed = 10
        self.car_speed = random.randint(self.min_speed, self.max_speed)
        self.new_position()
        
         
    
    def new_position(self):
        self.y = random.randint(-240,270)
        self.setpos(280,self.y)
        self.x = self.xcor()  
        self.car_speed = random.randint(self.min_speed, self.max_speed)   

   


    def car_move(self):
        self.x -= self.car_speed
        self.goto(self.x,self.y)
        if self.x < -300:
            self.new_position()
