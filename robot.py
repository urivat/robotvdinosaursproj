from dinosaur import Dinosaurs
from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.weapon = Weapon('Laser Gun', 50)
        # self.create_a_weapon()

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f'Good hit, will feel that one you did {self.weapon.attack_power} damage')
            
        

    # def create_a_weapon(self):
    #     weapon_one = Weapon('Laser Gun', 20)
    #     self.weapon.append(weapon_one)
    #     weapon_two = Weapon('light saber', 40)
    #     self.weapon.append(weapon_two)
    #     weapon_three = Weapon('Photon Cannon', 30)
    #     self.weapon.append(weapon_three)
   