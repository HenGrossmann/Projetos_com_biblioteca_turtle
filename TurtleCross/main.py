import time
from turtle import Screen
from player import Player
from car_manager import CarManager,increase_speed
from scoreboard import Scoreboard
WIDTH = 600
HEIGHT = 600
# Criar a janela onde fica o programa
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

#Criar a tartaruga
player = Player()

#Movimento da tartaruga vinculado ao w
screen.listen()
screen.onkey(player.move,'w')

scoreboard = Scoreboard()
car_list = []
count = 0

#Jogo rodando
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if count % 5 == 0 and len(car_list)<13:
        car = CarManager()
        car_list.append(car)
        #print(len(car_list))
    if count < 70:
        count+=1

    for c in car_list:
        c.car_move()
        if c.distance(player) < 50 and player.ycor() <= c.ycor()+10 and player.ycor() >= c.ycor() - 10:
            game_is_on = False
    
    if player.won:
        scoreboard.update_score()
        player.won = False
        increase_speed(car_list)

    screen.update()

scoreboard.game_over()
screen.mainloop()
