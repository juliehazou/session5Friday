# you have 3 lives. I roll the dice. If I roll 6, you win.
# If not a 6, you lose a life.

from random import randint

lives = 3
while lives:
    roll = randint(1, 6) #make sure not to put a: and b: (they were just added by the computer)
    if roll == 6:
        print("You rolled a 6, you win!")
        break #this exits the while even if the lives are still > 0 (cuz i won)
    #there is no other way to get here unless i DID NOT roll a 6 so there was an else and i will remove it and remove indent
    print(f"You rolled a {roll}! You lose a life")
    lives -= 1 #minus 1
    print(f"Lives left: {lives}")

# if lives == 0:
#     print("You lost!")
#     or
else: #else from while!!
    print("You lose!")


