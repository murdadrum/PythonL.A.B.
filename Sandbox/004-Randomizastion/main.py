import random

ROCK = 0
PAPER = 1
SCISSORS = 2

CHOICES = [''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']


def determine_game_result(player_choice, opponent_choice):
    if player_choice >= 3 or player_choice < 0:
        return "You typed an invalid number, you lose!"
    elif player_choice == ROCK and opponent_choice == SCISSORS:
        return "You win!"
    elif opponent_choice == ROCK and player_choice == SCISSORS:
        return "You lose"
    elif opponent_choice > player_choice:
        return "You lose"
    elif player_choice > opponent_choice:
        return "You win!"
    elif opponent_choice == player_choice:
        return "It's a draw"


player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(CHOICES[player_choice])

opponent_choice = random.randint(0, 2)

print("Computer chose:")
print(CHOICES[opponent_choice])

print(determine_game_result(player_choice, opponent_choice))
