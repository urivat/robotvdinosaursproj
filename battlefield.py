from fleet import Fleet
from herd import Herd
from robot import Robot
from dinosaur import Dinosaurs

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
       
            self.display_welcome()
#             print('We have the robot fleet')
#             select_robot = input(f'''select 0 for {self.fleet.robots[0].name}\nselect 1 for {self.fleet.robots[1].name}\nselect 2 for {self.fleet.robots[2].name}\n vs\n the dinosaur herd
# Select 0 for {self.herd.dinosaurs[0].name}\nselect 1 for {self.herd.dinosaurs[1].name}\nselect 2 for {self.herd.dinosaurs[2].name} ''')
#             print(select_robot)
            
            
            print(self.fleet.robots[0].name)
            
            print(self.fleet.robots[1].name)
            print(self.fleet.robots[2].name)
            print('vs')
            print(self.herd.dinosaurs[0].name)
            print(self.herd.dinosaurs[1].name)
            print(self.herd.dinosaurs[2].name)
            
            self.fleet.robots[0].attack(self.herd.dinosaurs[0])
            self.fleet.robots[0].death
            self.fleet.robots[1].attack(self.herd.dinosaurs[1])
            self.fleet.robots[2].attack(self.herd.dinosaurs[2])

            self.herd.dinosaurs[0].attack(self.fleet.robots[0])
            self.herd.dinosaurs[1].attack(self.fleet.robots[1])
            self.herd.dinosaurs[2].attack(self.fleet.robots[2])

            # dinosaur_two.attack(robot_two)

            # dinosaur_three.attack(robot_three)

            # robot_one.attack(dinosaur_one)

            # robot_two.attack(dinosaur_two)

            # robot_three.attack(dinosaur_three)
            # robot_one.test
    def death(self, robot, dinosaur):
       
        while True:
            robot.health or dinosaur.health <= 0
            print(f'sorry {self.fleet.robots[0],[1],[2].name}has been destroyed')
            self.fleet.robots.remove[0] or self.fleet.robots.remove[1] or self.fleet.robots.remove[2]
        
            
            
            
            
             # health = self.fleet.robots[0],[1],[2].health
              # self.fleet.robots[0].health <= 0 or self.fleet.robots[1].health <= 0 or self.fleet.robots[3] <= 0
            # robot.health or dinosaur.health <= 0
            # x    -= robot.name or dinosaur.name  
            # print('robot has been destroyed')
            # if robot.health <= 0

            

    def display_welcome(self):
        print('Hello and welcome to the Competion between dinosaurs and robots\n ')

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