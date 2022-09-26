from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.robot_health = 100
        self.active_weapon = Weapon('Lazer', 15)

    def attack(self, dinosaur):
        dinosaur_health = dinosaur
        dinosaur_health -= self.active_weapon.attack_power
        print(f"Robot has attacked Dinosaur using {self.active_weapon.name} with {self.active_weapon.attack_power}, Dinosaur now has a {dinosaur_health} health.")