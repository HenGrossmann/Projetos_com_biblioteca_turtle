from turtle import Turtle,Screen
import random

race_on = True
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet',prompt='Which turtle will win the race?').lower()
colors = ['red','orange','yellow','green','blue','purple']
turtle_list = []
x = -230
y = -100


for c in colors:
    turtle = Turtle(shape='turtle')
    turtle.color(c)
    turtle.penup()
    turtle.goto(x=-230,y=y)
    
    y+=30
    turtle_list.append(turtle)


while race_on:
    for turtle in turtle_list:
        distance = random.randrange(1,10)
        turtle.forward(distance)
        
        if turtle.pos()[0] > 230:
            print('aaaa')
            winning_turtle = turtle
            race_on = False

print('You were right'if user_bet == winning_turtle.color()[0] else 'You were wrong')


print(f'{winning_turtle.color()[0].title()} Won the race')




screen.exitonclick()