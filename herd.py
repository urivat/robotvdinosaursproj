from dinosaur import Dinosaurs

class Herd:

    def __init__(self):
        self.dinosaurs = []
        self.create_herd()


    def create_herd(self):   
        dinosaur_one = Dinosaurs('Basilisk', 50)
        self.dinosaurs.append(dinosaur_one)

        dinosaur_two = Dinosaurs('Inferno', 20)
        self.dinosaurs.append(dinosaur_two)

        dinosaur_three = Dinosaurs('Godzilla', 30)
        self.dinosaurs.append(dinosaur_three)