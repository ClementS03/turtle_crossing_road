import time
import threading
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup the screen
screen = Screen()
screen.setup(width=600, height=600)

# Screen animations
screen.tracer(0)

# Initialize Player, Cars and Scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen keyboard events
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    # Refresh every 0.1 seconds
    time.sleep(0.1)

    # Update the screen
    screen.update()

    # Generate and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            # Display Game Over if lose
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.reset_player()

        # Increase speed when reached the other side
        car_manager.level_up()

        # Display score and Level up the score if player reached the other side
        scoreboard.level_up()


screen.exitonclick()