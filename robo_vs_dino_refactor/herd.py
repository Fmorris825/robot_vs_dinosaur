from time import sleep
from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.tyrannosaurus = Dinosaur('Tyrannosaurus Rex', 15)
        self.stegosaurus = Dinosaur('Stegosaurus', 10)
        self.velociraptor = Dinosaur('Velociraptor', 5)

        self.dinolist = [self.tyrannosaurus.name, self.stegosaurus.name,self.velociraptor.name]

    def character_selection(self):
        i = 0
        print()
        for dino in self.dinolist:
            i += 1
            print(f'{[i]} {dino}')
            sleep(.3)
        print()
        user_dino_selection = input(f'Choose your Dinosaur [1]-[3] \n\n')
        if user_dino_selection == "1":
            self.user_dino_selection = self.tyrannosaurus
            print(f'\nYOU HAVE SELECTED: {self.tyrannosaurus.name}\n')
        elif user_dino_selection == "2":
            self.user_dino_selection = self.stegosaurus
            print(f'\nYOU HAVE SELECTED: {self.stegosaurus.name}\n')
        elif user_dino_selection == "3":
            self.user_dino_selection = self.velociraptor
            print(f'\nYOU HAVE SELECTED: {self.velociraptor.name}\n')

    def attack(self, robot):
        robot.health -= self.user_dino_selection.attack_power
        print(f"{self.user_dino_selection.name} has attacked {robot.name} with {self.user_dino_selection.attack_power} attack power, {robot.name}'s health is now {robot.health}. \n")
        sleep(.5)
