import random
from Winner import Winner
from Game import Game



if __name__ == '__main__':

    outcome = [None]
    choices = ["Paper", "Scissors", "Rock"]
    i = 0
    for i in range(3):
        comp_move = random.choice(choices)
        user_move = input("Please provide your choice as Paper or Scissors or Rock:")
        while user_move not in choices:
            user_move = input("Invalid Choice.Please select again you choice as Paper or Scissors or Rock:")
        outcome.append(Game.play(user_move, comp_move))
    Winner.winner(outcome[0], outcome[1], outcome[2])


