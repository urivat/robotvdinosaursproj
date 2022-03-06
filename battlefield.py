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
        while self.robots_index or self.dinosaurs_index != 3: 
           
            self.show_dino_opponent_options()
            self.show_robo_opponent_options()
            self.dino_turn()
            self.robo_turn()
        else:
            self.display_winners    
            
            

    def dino_turn(self):
        self.herd.dinosaurs[self.dinosaurs_index].attack(self.fleet.robots[self.robots_index])
        print(f'Now {self.fleet.robots[self.robots_index].name} has {self.fleet.robots[self.robots_index].health} remaining ')
        if self.fleet.robots[self.robots_index].health <= 0:
                self.fleet.robots.pop(self.robots_index)
                print(f'{self.fleet.robots[self.robots_index].name} has died ')
        

    def robo_turn(self):
        self.fleet.robots[self.robots_index].attack(self.herd.dinosaurs[self.dinosaurs_index])
        print(f'Now {self.herd.dinosaurs[self.dinosaurs_index].name} has {self.herd.dinosaurs[self.dinosaurs_index].health} remaining ')
        if self.herd.dinosaurs[self.dinosaurs_index].health <= 0:
            print(f'{self.herd.dinosaurs[self.dinosaurs_index].name} has died ')
            self.herd.dinosaurs.pop(self.dinosaurs_index)
        
        
    def show_dino_opponent_options(self):
        print(f'pick a dinosaur:\nselect 0 Basilisk\nselect 1 for Inferno\nselect 2 for Godzilla')
        pick_a_dino = input()
        return (int(pick_a_dino))
            
     


        

    def show_robo_opponent_options(self):
        print(f'pick a Robot:\nselect 0 for Mega Man \nselect 1 for Big O \nselect 2 for Astro Boy')
        pick_a_robo = input()
        return (int(pick_a_robo))


    def display_winners(self): 
        if self.fleet.robots[0].health <= 0 and  self.fleet.robots[1].health <=0 and self.fleet.robots[2].health <= 0:
            print('The winner is decided. Our fearsome reptiles are the champions ')
        elif self.herd.dinosaurs[0].health <= 0 and self.herd.dinosaurs[1].health <= 0 and self.herd.dinosaurs[2].health <= 0:
            print('The winner is decided. Our fearsome robos are the champions ')
    


  
        
  
            
