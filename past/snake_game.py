from runpy import run_module
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
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


main_surface.listen()
main_surface.onkeypress(go_up, "Up")
main_surface.onkeypress(go_down, "Down")
main_surface.onkeypress(go_right, "Right")
main_surface.onkeypress(go_left, "Left")
main_surface.tracer(False)

score = 0
high_score = 0
score_board = create_turtle("square", "white")
score_board.ht()
score_board.goto(0, 260)

def onclose():
    global running
    running = False

root = main_surface._root
root.protocol("WM_DELETE_WINDOW", onclose)


snake_tails = []
running = True
while running:
    score_board.clear()
    score_board.write(f"Score:{score}, HighScore:{high_score}", font=("arial", 22), align="center")
    main_surface.update()
    if snake_head.distance(snake_food) < 20:
        change_food_position(snake_food)
        score += 1
        if score > high_score:
            high_score = score
        new_tail = create_turtle("square", "blue")
        snake_tails.append(new_tail)
    for i in range(len(snake_tails) - 1, 0, -1):
        x = snake_tails[i-1].xcor()
        y = snake_tails[i-1].ycor()
        snake_tails[i].goto(x, y)

    if len(snake_tails) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_tails[0].goto(x, y)

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or\
            snake_head.ycor() > 290 or snake_head.ycor() < -290:
        snake_head.goto(0, 0)
        snake_head.direction = ""
        score = 0
        for tail in snake_tails:
            tail.ht()

        snake_tails.clear()

    

    move()

    for tail in snake_tails:
        if snake_head.distance(tail) < 20:
            snake_head.goto(0, 0)
            snake_head.direction = ""
            score = 0
            for tail in snake_tails:
                tail.ht()

            snake_tails.clear()
            break

    sleep(0.2)
