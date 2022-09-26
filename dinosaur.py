class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = int(attack_power)
        self.health = 100

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"Dinosaur has attacked Robot with {self.attack_power} attack power, Robot's health is now {robot.health}. ")