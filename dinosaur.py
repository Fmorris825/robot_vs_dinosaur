class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = int(attack_power)
        self.dino_health = 100

    def attack(self, robot):
        robot_health = robot
        robot_health -= self.attack_power
        print(f"Dinoaur has attacked Robot with {self.attack_power} attack power, Robot's health is now {robot_health}. ")