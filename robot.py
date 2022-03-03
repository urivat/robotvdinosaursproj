from dinosaur import Dinosaurs
from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Laser Gun', 50)
    
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f'Good hit, they will feel that one you did{self.weapon.attack_power} damage')
