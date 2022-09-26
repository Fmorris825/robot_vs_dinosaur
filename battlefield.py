from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot('Terminator 999')
        self.dinosaur = Dinosaur('Supergigantosaurs', 10)

    def display_welcome(self):
        print('\n Greetings, this is a battle between the past and the future! \n \n See who will prevail! \n')

    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.dinosaur.attack(self.robot)           
            self.robot.attack(self.dinosaur)
        self.display_winner()
        

    def display_winner(self):
        if self.robot.health < 0:
            print(f'{self.dinosaur.name} has overcame the {self.robot.name} and turned it to metal scrap')
        if self.dinosaur.health < 0:
            print(f'{self.robot.name} has put an end to {self.dinosaur.name} for the second time history.')


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        

