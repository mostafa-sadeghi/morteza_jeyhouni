from turtle import Screen, Turtle
import turtle
from time import sleep

main_screen = Screen()
# main_screen.register_shape("strawberry.gif")


turtle1 = Turtle()
turtle1.color("cyan")
turtle1.speed("fastest")
# turtle1.shape("strawberry.gif")
turtle1.shape("turtle")
turtle1.shapesize(2, 2)


turtle1.forward(50)
sleep(1)
turtle1.left(180)
sleep(1)
turtle1.fd(100)

# turtle1.begin_fill()
# turtle1.circle(30)
# turtle1.end_fill()

# turtle1.hideturtle()

turtle.done()
