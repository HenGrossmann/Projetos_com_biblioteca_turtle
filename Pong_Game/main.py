from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def run_robot_paddle():
    right_paddle.robot_paddle(HEIGHT=HEIGHT,speed=ENEMY_SPEED)


#definir a altura e largura da tela
WIDTH = 800
HEIGHT = 600    
ENEMY_SPEED = 30
OUT_OF_BOUNDS = (WIDTH-40)
def print_x_position(x, y):
    print(f"X position: {x}")

#criar a tela e seus componentes
screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

#criar um paddle e configurar ele
paddle = Paddle()
paddle.setpos(-WIDTH/2+40,0)
paddle.showturtle()

#Outro paddle
right_paddle = Paddle()
right_paddle.setpos(WIDTH/2-40,0)
right_paddle.showturtle()


ball = Ball()
scoreboard = Scoreboard()
#inputs de botoes paddle
screen.listen()


screen.onkeypress(paddle.move_up, "Up")
screen.onkeypress(paddle.move_down, "Down")


two_player = str(input('Two player? (Y/N) ')).upper()
if two_player == 'Y':
    screen.onkeypress(right_paddle.move_up, "w")
    screen.onkeypress(right_paddle.move_down, "s")

screen.onscreenclick(print_x_position, 3)
screen.update()

game_is_on = True
while game_is_on:
    if two_player !='Y':
        right_paddle.robot_paddle(HEIGHT=HEIGHT,speed=ENEMY_SPEED)

    screen.update()
    ball.moving_ball()
    time.sleep(0.1)
    #makes the ball bounces top and bottom
    if ball.ycor() > HEIGHT/2-20 or ball.ycor()<-HEIGHT/2+20:
        ball.bounce_y()
    
    #if ball goes out of bounds
    if ball.xcor() > WIDTH/2-35 or ball.xcor()<-WIDTH/2+35:
        score = ball.reset(WIDTH)
        print('a')
        if score == 'left':
            scoreboard.l_score += 1
        else:
            scoreboard.r_score += 1
    scoreboard.update_scoreboard()
        
    
    # If distance is less than or equal to sum of radii, there is a collision
    if ball.distance(right_paddle) < 50 and ball.xcor()> WIDTH/2-60 or ball.distance(paddle) < 50 and ball.xcor() < (-WIDTH/2)+60:
        
        ball.bounce_x()

screen.exitonclick()