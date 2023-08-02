from matplotlib.pyplot import xlim
from snake_game_utils import *
from time import sleep
main_surface = create_screen()
snake_head = create_turtle("square", "blue")
snake_head.direction = ""

snake_food = create_turtle("circle", "red")
change_food_position(snake_food)


def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)

def go_up():
    snake_head.direction = "up"

def go_down():
    snake_head.direction = "down"

def go_right():
    snake_head.direction = "right"

def go_left():
    snake_head.direction = "left"

main_surface.listen()
main_surface.onkeypress(go_up,"Up")
main_surface.onkeypress(go_down,"Down")
main_surface.onkeypress(go_right,"Right")
main_surface.onkeypress(go_left,"Left")

running = True
while running:
    main_surface.update()
    move()
    sleep(0.2)