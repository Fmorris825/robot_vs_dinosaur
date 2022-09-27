from dinosaur import Dinosaur
from fleet import Fleet
from robot import Robot
from herd import Herd
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robots = Fleet()
        self.dinosaurs = Herd()

    def display_welcome(self):
        print('\n Greetings, this is a battle between the past and the future! \n \n See who will prevail! \n')

    def get_characters(self):
        self.dinosaurs.character_selection()
        self.robots.character_selection()
        
    def battle_phase(self):
        self.robots.choose_weapon()
        while self.dinosaurs.user_dino_selection.health > 0 and self.robots.user_robo_selection.health > 0:
            self.dinosaurs.attack(self.robots.user_robo_selection)           
            self.robots.attack(self.dinosaurs.user_dino_selection)
        self.display_winner()
        

    def display_winner(self):
        if self.robots.user_robo_selection.health <= 0:
            print(f'{self.dinosaurs.user_dino_selection.name} has overcame the {self.robots.user_robo_selection.name} and turned it to metal scrap')
        elif self.dinosaurs.user_dino_selection.health <= 0:
            print(f'{self.robots.user_robo_selection.name} has put an end to {self.dinosaurs.user_dino_selection.name} for the second time history.')
        else:
            print(f'{self.robots.user_robo_selection.name} & {self.dinosaurs.user_dino_selection.name} have both fallen, the battle results in a stalemate. ')


    def run_game(self):
        self.display_welcome()
        self.get_characters()
        self.battle_phase()
