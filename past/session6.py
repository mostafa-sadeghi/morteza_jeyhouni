import turtle

main_surface = turtle.Screen()
main_surface.title("My Application")
main_surface.setup(600, 600)
main_surface.bgcolor("cyan")
# main_surface.bgpic("my.png")


my_pen = turtle.Pen()
my_pen.pensize(3)
my_pen.color("red")
my_pen.forward(100)
my_pen.left(90)
my_pen.forward(100)
my_pen.left(90)
my_pen.forward(100)
my_pen.left(90)
my_pen.forward(100)

# main_surface.exitonclick()
turtle.done()


# TODO   write a program with turtle that draws a triangle (size of each side is 100 and pen color is green)
# TODO   write a program with turtle that draws a pentagon (size of each side is 90 and pen size is 4)
# TODO   write a program with turtle that draws a hexagon  (size of each side is 80 and pen color is black)
