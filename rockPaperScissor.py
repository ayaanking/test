import random

# random number generator, storing the computers moves and the players moves
computerMove = ""
playerInput = ""

# rules
print("Rules: Enter r, p or s for rock paper of scissor respectively. Enter x if you would like to quit")
print("(In case you were wondering it would be a best of 5 so good luck)")

# main variables
limit = 3
run = True
playerWinCount = 0
computerWinCount = 0

# main game logic
while run and limit != 0:
    random_number = random.randrange(1, 4)

    if random_number == 1:
        computerMove = "Rock"
    elif random_number == 2:
        computerMove = "Paper"
    elif random_number == 3:
        computerMove = "Scissor"

    playerInput = input('Enter your move: ')
    print('Computer move: ' + computerMove)
    if computerMove == playerInput.lower():
        print('Draw')
    elif computerMove == 'Rock' and playerInput.lower() == 'p':
        print('You got it!')
        playerWinCount = playerWinCount + 1

    elif computerMove == 'Rock' and playerInput.lower() == 's':
        print('The computer wins')
        computerWinCount = computerWinCount + 1

    elif computerMove == 'Paper' and playerInput.lower() == 'r':
        print("The Computer won")
        computerWinCount = computerWinCount + 1

    elif computerMove == 'Paper' and playerInput.lower() == 's':
        print('You got it!')
        playerWinCount = playerWinCount + 1

    elif computerMove == 'Scissor' and playerInput.lower() == 'p':
        print('The computer won')
        print('Try Again')
        computerWinCount = computerWinCount + 1

    elif computerMove == 'Scissor' and playerInput.lower() == 'r':
        print('You got it!')
        playerWinCount = playerWinCount + 1

    elif playerInput == 'x':
        run = False

    limit = limit - 1

# result logic
if limit == 0:
    print(" ")
    print('Here are the results')
else:
    pass

print('The computer has ' + str(computerWinCount) + ' point/points')
print('You have ' + str(playerWinCount) + ' point/points')

# final comparison
if computerWinCount > playerWinCount:
    print('So, the computer won')
elif playerWinCount > computerWinCount:
    print('You Won')
else:
    print("It's a draw")