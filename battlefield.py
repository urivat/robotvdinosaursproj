from fleet import Fleet
from herd import Herd
from robot import Robot
from dinosaur import Dinosaurs

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
       
            print(self.fleet.robots[0].name)
            print(self.fleet.robots[1].name)
            print(self.fleet.robots[2].name)
            print('vs')
            print(self.herd.dinosaurs[0].name)
            print(self.herd.dinosaurs[1].name)
            print(self.herd.dinosaurs[2].name)
            
            self.fleet.robots[0].attack(self.herd.dinosaurs[0])
            self.fleet.robots[1].attack(self.herd.dinosaurs[1])
            self.fleet.robots[2].attack(self.herd.dinosaurs[2])

            # dinosaur_two.attack(robot_two)

            # dinosaur_three.attack(robot_three)

            # robot_one.attack(dinosaur_one)

            # robot_two.attack(dinosaur_two)

            # robot_three.attack(dinosaur_three)
            # robot_one.test


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