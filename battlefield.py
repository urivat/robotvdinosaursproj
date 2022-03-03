from fleet import Fleet
from herd import Herd
from robot import Robot
from dinosaur import Dinosaurs

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

robot_one = Robot('Blitz')
robot_two = Robot('Tim')
robot_three = Robot('Scrappy')
print(robot_one.name)
print(robot_one.health)
print(robot_one.weapon)
dinosaur_one = Dinosaurs('Big Head', 50)
dinosaur_two = Dinosaurs('Choppy', 20)
dinosaur_three = Dinosaurs('Stompy', 30)

    def run_game(self):
        pass
    def display_welcome(self):
        pass
    def battle(self):
        pass
    def dino_turn(self, dinosaur):
        pass
    def robo_turn(self, robot):
        pass
    def show_dino_opponent_options(self):
        pass
    def show_robo_opponent_options(self):
        pass
    def display_winners(self): 
        pass