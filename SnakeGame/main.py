from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


WIDTH = 600
HEIGHT = 600    

#SNAKE_NUMBER = 3




screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()

food = Food()


scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #colisao com comida
    if snake.head.distance(food) < 15:
        print('NHON NHON NHON')
        food.refresh()
        scoreboard.score += 1
        scoreboard.update_text()
        snake.extend()
    #colisao com parede
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False

    #colisao com cauda
    for segment in snake.snakes[1:]:
        #if segment == snake.head:
            #pass

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

scoreboard.game_over()







screen.exitonclick()