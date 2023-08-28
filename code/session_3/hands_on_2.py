import random

player1_dice1= random.randint(1, 6)
player1_dice2= random.randint(1, 6)
player1_sum = player1_dice1 + player1_dice2
print("Player 1 has rolled: ", player1_dice1, ",", player1_dice2) # Print out the generated numbers in order to check the result.

player2_dice1= random.randint(1, 6)
player2_dice2= random.randint(1, 6)
player2_sum = player2_dice1 + player2_dice2
print("Player 2 has rolled: ", player2_dice1, ",", player2_dice2)

if player1_sum > player2_sum:
    print("\nPlayer 1 wins!")
elif player1_sum < player2_sum:
    print("\nPlayer 2 wins!")
else:
    print("\nTie!")
