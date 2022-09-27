from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.terminator_1999 = Robot('Terminator 1999')
        self.terminator_2010 = Robot('Terminator 2010')
        self.terminator_2100 = Robot('Terminator 2100')

        self.robolist = [self.terminator_1999.name,self.terminator_2010.name,self.terminator_2100.name]


    def character_selection(self):
        user_robo_selection = input(f'Choose your Robot {self.robolist}')
        if user_robo_selection == "Terminator 1999":
            self.user_robo_selection = self.terminator_1999
            print(f'YOU HAVE SELECTED: {self.terminator_1999.name}')
        elif user_robo_selection == "Terminator 2010":
            self.user_robo_selection = self.terminator_2010
            print(f'YOU HAVE SELECTED: {self.terminator_2010.name}')
        elif user_robo_selection == "Terminator 2100":
            self.user_robo_selection = self.terminator_2100
            print(f'YOU HAVE SELECTED: {self.terminator_2100.name}')


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