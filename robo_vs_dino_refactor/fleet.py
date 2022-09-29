from time import sleep
from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.terminator_1999 = Robot('Terminator 1999')
        self.terminator_2010 = Robot('Terminator 2010')
        self.terminator_2100 = Robot('Terminator 2100')

        self.robolist = [self.terminator_1999.name,self.terminator_2010.name,self.terminator_2100.name]


    def character_selection(self):
        i = 0
        print()
        for robot in self.robolist:
            i += 1
            print(f'{[i]} {robot}')
            sleep(.3)
        print()
        user_robo_selection = input(f'Choose your Robot [1]-[3] \n\n')
        if user_robo_selection == "1":
            self.user_robo_selection = self.terminator_1999
            print(f'\nYOU HAVE SELECTED: {self.terminator_1999.name}\n')
        elif user_robo_selection == "2":
            self.user_robo_selection = self.terminator_2010
            print(f'\nYOU HAVE SELECTED: {self.terminator_2010.name}\n')
        elif user_robo_selection == "3":
            self.user_robo_selection = self.terminator_2100
            print(f'\nYOU HAVE SELECTED: {self.terminator_2100.name}\n')


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
        print(f"{self.user_robo_selection.name} has attacked {dinosaur.name} using a {self.active_weapon.name} with {self.active_weapon.attack_power}, {dinosaur.name} now has a {dinosaur.health} health. \n")
        sleep(.5)