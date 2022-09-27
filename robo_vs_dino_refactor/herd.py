from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.tyrannosaurus = Dinosaur('Tyrannosaurus Rex', 15)
        self.stegosaurus = Dinosaur('Stegosaurus', 10)
        self.velociraptor = Dinosaur('Velociraptor', 5)

        self.dinolist = [self.tyrannosaurus.name, self.stegosaurus.name,self.velociraptor.name]

    def character_selection(self):
        user_dino_selection = input(f'Choose your Dinosaur {self.dinolist}')
        if user_dino_selection == "Tyrannosaurus Rex":
            self.user_dino_selection = self.tyrannosaurus
            print(f'YOU HAVE SELECTED: {self.tyrannosaurus.name}')
        elif user_dino_selection == "Stegosaurus":
            self.user_dino_selection = self.stegosaurus
            print(f'YOU HAVE SELECTED: {self.stegosaurus.name}')
        elif user_dino_selection == "Velociraptor":
            self.user_dino_selection = self.velociraptor
            print(f'YOU HAVE SELECTED: {self.velociraptor.name}')

    def attack(self, robot):
        robot.health -= self.user_dino_selection.attack_power
        print(f"Dinosaur has attacked Robot with {self.user_dino_selection.attack_power} attack power, Robot's health is now {robot.health}. \n")
