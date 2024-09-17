import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def game():
    high_score = 0
    while True:
        print("Current High Score:", high_score, "\n")
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice: ")
        if choice == "1":
            roll1, roll2 = roll_dice()
            total = roll1 + roll2
            print(f"You rolled a {roll1} and a {roll2}. Total: {total}\n")
            if total > high_score:
                high_score = total
                print("New high score!\n")
        elif choice == "2":
            print("Thanks for playing!\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

game()