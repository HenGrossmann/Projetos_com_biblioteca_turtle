from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('arial',24,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.sety(267)
        self.ht()
        self.color('white')
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        #self.ht()
    
    def update_text(self):
        self.clear()
        
        
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    

    def game_over(self):
        
        self.goto(0,0)
        self.write('GAME OVER',align=ALIGNMENT,font=FONT)