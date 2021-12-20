import random 

def play():
    user = input("What is your choice ? \nr for Rock \np for Paper \ns for scissors\n")
    user = user.lower()

    computer = random.choice(['r','p','s'])

    if user == computer:
        return "You and computer have chosen the same"
    
    elif user == 's' and computer == 'r':
        return "Computer have won" 

    elif user == 'r' and computer == 's':
        return "You have won"

    elif user == 'p' and computer == 's':
        return "Computer have won" 

    elif user == 's' and computer == 'p':
        return "You have won"

    elif user == 'r' and computer == 'p':
        return "Computer have won" 

    elif user == 'p' and computer == 'r':
        return "You have won"
game = 'y'
while game == 'y':
    result = play()
    print(result)
    game = input('Do you want to play the game again(y/n) : ')
    game = game.lower()