from turtle import Screen, Turtle
import random


def create_screen():
    my_screen = Screen()
    my_screen.title("snake game")
    my_screen.setup(600, 600)
    my_screen.bgcolor("black")
    return my_screen


def create_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_food_position(snake_food):
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    snake_food.goto(x, y)
