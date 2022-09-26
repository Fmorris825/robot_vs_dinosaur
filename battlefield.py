from turtle import done
from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot('robot')
        self.dinosaur = Dinosaur('dino', 10)

    def display_welcome(self):
        print('\n Greetings, this is a battle between the past and the future! \n \n See who will prevail! \n')

    def battle_phase(self):
        above_100 = False
        while True:
            if self.dinosaur.health > 0 or self.robot.health > 0:
                self.dinosaur.attack(self.robot)           
                self.robot.attack(self.dinosaur)
            if self.dinosaur.health < 0 or self.robot.health < 0:
                print('done')
                break
        

    def display_winner(self):
        pass

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        # display_winner(self)

