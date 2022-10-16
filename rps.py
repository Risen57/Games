import random
from os import system

def printer(you, cpu, res):
    print(f"You chose: {you}")
    print(f"Computer chose: {cpu}")
    print(f"You {res}!")

def main(money):
    print("Welcome to Rock Paper Scissors Game!")
    print("Press\nR for rock\nP for Paper\nS for Scissors\n")
    input("Press ENTER to start")
    system('clear')

    tries = 1
    user_points = 0
    cpu_points = 0
    
    while tries <= 5:
        user_choice = input("Enter your choice:\n").upper()
        cpu_choice = random.choice(['R', 'P', 'S'])

        if user_choice == cpu_choice:
            printer(user_choice, cpu_choice, "Tied")
            print("This won't be considered a try")

        elif user_choice == 'R' and cpu_choice == 'P':
            printer(user_choice, cpu_choice, "Lost")
            tries += 1
            cpu_points += 1
        elif user_choice == 'R' and cpu_choice == 'S':
            printer(user_choice, cpu_choice, "Won")
            tries += 1
            user_points += 1
        elif user_choice == 'P' and cpu_choice == 'S':
            printer(user_choice, cpu_choice, "Lost")
            tries += 1
            cpu_points += 1
        elif user_choice == 'P' and cpu_choice == 'R':
            printer(user_choice, cpu_choice, "Won")
            tries += 1
            user_points += 1
        elif user_choice == 'S' and cpu_choice == 'R':
            printer(user_choice, cpu_choice, "Lost")
            tries += 1
            cpu_points += 1
        elif user_choice == 'S' and cpu_choice == 'P':
            printer(user_choice, cpu_choice, "Won")
            tries += 1
            user_points += 1

    print(f"Your points: {user_points}")
    print(f"Computer points: {cpu_points}")

    if user_points > cpu_points:
        print("You Won!")
    else:
        print("You Lost!")
        
if __name__ == "__main__":
    main()
    