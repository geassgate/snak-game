import turtle
import time
from food import Food 
from scorebord import Scorebord

STRING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
##########################################
screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My snake game")
MOVE_DESTANSE = 20
###########################################

class Snake(object):
    """docstring for Snake"""
    def __init__(self):
        self.part_list = []
        self.make_snake()
        self.head = self.part_list[0]

    def make_snake(self):
        for position in STRING_POSITION :
            self.add_segment(position)

    def add_segment(self, position):
        part = turtle.Turtle("square")
        part.color("white")
        part.penup()
        part.goto(position)
        self.part_list.append(part)

    def extend(self):
        self.add_segment(self.part_list[-1].position())

    def move(self) :
        for part in range(len(self.part_list)-1, 0, -1):
            new_x = self.part_list[part-1].xcor()
            new_y = self.part_list[part-1].ycor()
            self.part_list[part].goto(new_x, new_y)
        self.head.forward(MOVE_DESTANSE)

    def up(self):
       self.head.setheading(90)

    def down(self):
       self.head.setheading(270)

    def right(self):
       self.head.setheading(0)

    def left(self):
       self.head.setheading(180)

screen.tracer(0)

snake = Snake()
food = Food()
score = Scorebord()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect the collision with food
    if snake.head.distance(food) < 15 :
        score.inc_score()
        snake.extend()
        food.refresh()
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        score.  game_over()
    #Detect collision with tail
    for segments in snake.part_list[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick() 