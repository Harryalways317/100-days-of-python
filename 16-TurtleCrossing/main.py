from pydoc import plain
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Roads")
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(player.up,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    


    #player collison with car
    for car in car_manager.all_cars:
        if(car.distance(player) < 20):
            game_is_on = False
            scoreboard.game_over()

    #sucessful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_score()
    
screen.exitonclick()