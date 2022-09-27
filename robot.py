from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def choose_weapon(self):
        user_weapon_select = input('CHOOSE YOUR WEAPON!!! \n "Lazer" \n "Saber Sword" \n "Hand Cannon" \n')
        if user_weapon_select == "Lazer":
            self.active_weapon = Weapon('Lazer', 5)
            print(F'\n {self.active_weapon.name} SELECTED ! \n')
        elif user_weapon_select == "Saber Sword":
            self.active_weapon = Weapon('Saber Sword', 25)
            print(F'\n {self.active_weapon.name} SELECTED ! \n')
        elif user_weapon_select == "Hand Cannon":
            self.active_weapon = Weapon('Hand Cannon', 10)
            print(F'\n {self.active_weapon.name} SELECTED ! \n')


    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f"Robot has attacked Dinosaur using a {self.active_weapon.name} with {self.active_weapon.attack_power}, Dinosaur now has a {dinosaur.health} health. \n")


       