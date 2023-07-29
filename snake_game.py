from snake_game_utils import *

main_surface = create_screen()


snake_head = create_turtle("square", "blue")

snake_food = create_turtle("circle", "red")
change_food_position(snake_food)



running = True
while running:
    main_surface.update()