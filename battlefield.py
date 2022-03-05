from fleet import Fleet
from herd import Herd
from robot import Robot
from dinosaur import Dinosaurs

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.dinosaurs_index= 0
        self.robots_index = 0
    
    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()

            
    
           
           
           
         

            

    def display_welcome(self):
        print('Hello and welcome to the Competion between dinosaurs and robots\n ')

    def battle(self):
        while self.fleet.robots or self.herd.dinosaurs > 0 and self.fleet.robots or self.herd.dinosaurs <= 3: 
            self.show_dino_opponent_options()
            self.show_robo_opponent_options()
            self.dino_turn()
            self.robo_turn()
            if self.fleet.robots[self.robots_index].health <= 0:
                self.fleet.robots.pop(self.robots_index)
                print(f'{self.fleet.robots[self.robots_index].name} has died ')
            if self.herd.dinosaurs[self.dinosaurs_index].health <= 0:
                self.herd.dinosaurs.pop(self.dinosaurs_index)
                print(f'{self.herd.dinosaurs[self.dinosaurs_index].name} has died ')
            

    def dino_turn(self):
        self.herd.dinosaurs[self.dinosaurs_index].attack(self.fleet.robots[self.robots_index])
        print(f'Now {self.fleet.robots[self.robots_index].name} has {self.fleet.robots[self.robots_index].health} remaining ')
        
        
        

    def robo_turn(self):
        self.fleet.robots[self.robots_index].attack(self.herd.dinosaurs[self.dinosaurs_index])
        print(f'Now {self.herd.dinosaurs[self.dinosaurs_index].name} has {self.herd.dinosaurs[self.dinosaurs_index].health} remaining ')
        

    def show_dino_opponent_options(self):
        print(f'pick a dinosaur:\nselect 0 {self.herd.dinosaurs[0].name}\nselect 1 for {self.herd.dinosaurs[1].name}\nselect 2 {self.herd.dinosaurs[2].name}')
        pick_a_dino = input()
        return (int(pick_a_dino))
            
     


        

    def show_robo_opponent_options(self):
        pick_a_robo = input(f'pick a Robot:\nselect 0 for {self.fleet.robots[0].name} \nselect 1 for {self.fleet.robots[1].name} \nselect 2 for {self.fleet.robots[2].name}')
        return (int(pick_a_robo))


    def display_winners(self): 
        if self.fleet.robots[0].health <= 0 and  self.fleet.robots[1].health <=0 and self.fleet.robots[2].health <= 0:
            print('The winner is decided. Our fearsome reptiles are the champions ')
        elif self.herd.dinosaurs[0].health <= 0 and self.herd.dinosaurs[1].health <= 0 and self.herd.dinosaurs[2].health <= 0:
            print('The winner is decided. Our fearsome robos are the champions ')
    
    # print('We have the robot fleet')
    # select_robot = input(f'''select 0 for {self.fleet.robots[0].name}\nselect 1 for {self.fleet.robots[1].name}\nselect 2 for {self.fleet.robots[2].name}\n vs\n the dinosaur herd
    # Select 0 for {self.herd.dinosaurs[0].name}\nselect 1 for {self.herd.dinosaurs[1].name}\nselect 2 for {self.herd.dinosaurs[2].name} ''')
    # print(select_robot)
                
                
    # print(self.fleet.robots[0].name)
    
    # print(self.fleet.robots[1].name)
    # print(self.fleet.robots[2].name)
    # print('vs')
    # print(self.herd.dinosaurs[0].name)
    # print(self.herd.dinosaurs[1].name)
    # print(self.herd.dinosaurs[2].name)
# robot_fleet = Fleet()
            # print(robot_fleet.robots[0].name)
            # robot_fleet.robots[0].death()   

            # self.fleet.robots[0].attack(self.herd.dinosaurs[0])
            # self.herd.dinosaurs[0].death()
            # print(self.herd.dinosaurs[0])
            # self.fleet.robots[1].attack(self.herd.dinosaurs[1])
            # self.fleet.robots[2].attack(self.herd.dinosaurs[2])

            # self.herd.dinosaurs[0].attack(self.fleet.robots[0])
            # self.herd.dinosaurs[1].attack(self.fleet.robots[1])
            # self.herd.dinosaurs[2].attack(self.fleet.robots[2])

            # dinosaur_two.attack(robot_two)

            # dinosaur_three.attack(robot_three)

            # robot_one.attack(dinosaur_one)

            # robot_two.attack(dinosaur_two)

            # robot_three.attack(dinosaur_three)
            # robot_one.test
# def death(self):
#         while True:
#             if (self.fleet.robots[0].health <= 0):
#                 self.fleet.robots.pop[0]
#                 print(f'{self.fleet.robots[0].name} has been slain')
#             elif (self.fleet.robots[1].health <= 0):
#                 self.fleet.robots.pop[1]
#                 print(f'{self.fleet.robots[1]} has been slain')
#             elif (self.fleet.robots[2].health <= 0):
#                 self.fleet.robots.pop[2]
#                 print(f'{self.fleet.robots[2]} has been slain')
#             elif (self.herd.dinosaurs[0].health <= 0):
#                 self.herd.dinosaurs.pop[0]
#                 print(f'{self.herd.dinosaurs[0].name} has fallen')
#             elif (self.herd.dinosaurs[1].health <= 0):
#                 self.herd.dinosaurs.pop[1]
#                 print(f'{self.herd.dinosaurs[1].name} has fallen')
#             elif (self.herd.dinosaurs[2].health <= 0):
#                 self.herd.dinosaurs.pop[2]
#                 print(f'{self.herd.dinosaurs[2]} has fallen')
        
  
            # print(f'sorry {self.fleet.robots[0]}has been destroyed')
        
            
            
            
            
             # health = self.fleet.robots[0],[1],[2].health
              # self.fleet.robots[0].health <= 0 or self.fleet.robots[1].health <= 0 or self.fleet.robots[3] <= 0
            # robot.health or dinosaur.health <= 0
            # x    -= robot.name or dinosaur.name  
            # print('robot has been destroyed')
            # if robot.health <= 0

