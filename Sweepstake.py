from Contestant import Contestant
import random


class Sweepstake:

    def __init__(self):
        self.contestants = []
        self.name = ''

    def choose_sweepstakes_name(self):
        self.name = input("What would you like to name the sweepstakes?")

    def register_contestant(self, person):  ##Person should be collected as first_name,last_name, email, etc..
        self.contestants.append(Contestant(person))

    def pick_winner(self):
        i = range(0, len(self.contestants))
        self.contestants[i].winner = True

    def display_outcome(self):
        for person in self.contestants:
            if person.winner == False:
                print("Sorry, no winner!")
            if person.winner == True:
                print(f"{person.first_name} {person.last_name} is the winner.")
