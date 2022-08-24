import random

# 1 = Rock
# 2 = Paper
# 3 = Scissors
# Rock beats Scissors  || 1 > 3
# Paper beats Rock     || 2 > 1
# Scissors beats Paper || 3 > 2
# Draw                 || 1 = 1 || 2 = 2 || 3 = 3

def gameDict(choice):
    value = ''
    if choice == 1:
        value = 'Rock'
    elif choice == 2:
        value = 'Paper'
    elif choice == 3:
        value = 'Scissors'
    else:
        value = 'Failure'
    return value
    
def gameResult(cpuGamer, cringeGamer):
    cpuChoice = gameDict(cpuGamer)
    playerChoice = gameDict(int(cringeGamer))
    if cpuChoice == playerChoice:
        print(f"Result is a Draw: {playerChoice} == {cpuChoice}")
    elif cpuChoice == 'Rock' and playerChoice == 'Paper':
        print(f"Result is a Win: {playerChoice} >> {cpuChoice}")
    elif cpuChoice == 'Rock' and playerChoice == 'Scissors':
        print(f"Result is a Loss: {playerChoice} << {cpuChoice}")
    elif cpuChoice == 'Paper' and playerChoice == 'Rock':
        print(f"Result is a Loss: {playerChoice} << {cpuChoice}")
    elif cpuChoice == 'Paper' and playerChoice == 'Scissors':
        print(f"Result is a Win: {playerChoice} >> {cpuChoice}")
    elif cpuChoice == 'Scissors' and playerChoice == 'Rock':
        print(f"Result is a Win: {playerChoice} >> {cpuChoice}")
    elif cpuChoice == 'Scissors' and playerChoice == 'Paper':
        print(f"Result is a Loss: {playerChoice} << {cpuChoice}")
    else:
        print("Ultra Cringe Failure")
    print("===========\nMenu:\n===========\n1. Play Again\nQ. Quit")

def cringeGame():
    # display a random number between 1 and 3:
    cpugamer = random.randrange(1,4)
    print("\n===========\nOptions:\n===========\n1. Rock\n2. Paper\n3. Scissors")
    game_option = input("Game Option: ").lower()
    gameResult(cpugamer, game_option)

def main():  
    print("======================================")
    print("==      CRINGE PAPER SNIPPER        ==")
    print("======================================")
    print("\n===========\nMenu:\n===========\n1. Play\nQ. Quit")
    
    while True:
        menu_option = input("Menu Option: ").lower()
        if menu_option == '1':
            try:
                cringeGame()
            except ValueError:
                print(f"Cringe Failure: {ValueError}")
        elif menu_option == 'q':
            exit()
        else:
            pass

if __name__ == '__main__':
    main()