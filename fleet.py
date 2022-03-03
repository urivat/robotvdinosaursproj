from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_one= Robot("Mega Man")
        self.robots.append(robot_one)
        robot_two = Robot("Big O")
        self.robots.append(robot_two)
        robot_three = Robot("Astro Boy")
        self.robots.append(robot_three)