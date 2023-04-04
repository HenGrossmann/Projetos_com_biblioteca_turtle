from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-220,260)
        self.level = 1
        self.write(f'LEVEL: {self.level}',align='center',font=FONT)
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.level +=1
        self.write(f'LEVEL: {self.level}',align='center',font=FONT)

    
    def game_over(self):  
        self.goto(0,0)
        self.write(f'GAME OVER',align='center',font=FONT)