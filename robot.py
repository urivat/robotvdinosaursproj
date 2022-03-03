from dinosaur import Dinosaurs
from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Laser Gun', 50)
    
    def attack(self, dinosaur):
        self.weapon.attack_power -= dinosaur

