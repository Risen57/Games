import random
from os import system

def gengrid(grid):
    x = 1

    while x <= 5:
        ship_y = random.randint(0, 3)
        ship_x = random.randint(0, 3)

        if grid[ship_y][ship_x] != "0":
            grid[ship_y][ship_x] = "0"
            x += 1
        else:
            continue

    return grid

def attack(x, y, grid, cpu_killed, attacker, points):
    if attacker == "You":
        if [y, x] not in cpu_killed:
            if grid[y][x] == "0":
                hit = True
                points += 1
                print(attacker, "hit!")
            else:
                hit = False
                print(attacker, "couldn't hit!")
    else:
        if grid[y][x] == "0":
            hit = True
            points += 1
            print(attacker, "hit!")
        else:
            hit = False
            print(attacker, "couldn't hit!")

    return [hit, points]

def print_grids(user_grid, cpu_grid, cpu_killed, user_killed, user_points, cpu_points):
    print("Your points:", user_points)
    print("Your grid:")
    print("\n")

    for item in user_killed:
        killed_y = item[0]
        killed_x = item[1]
        user_grid[killed_y][killed_x] = "X"
    for item in user_grid: print(item)
    print("\n")

    print("Enemy points:", cpu_points)
    print("Enemy grid:")
    print("\n")

    cpu_grid_display = [["#", "#", "#", "#"] for y in range(4)]
    for item in cpu_killed:
        killed_y = item[0]
        killed_x = item[1]
        cpu_grid_display[killed_y][killed_x] = "X"
    for item in cpu_grid_display: print(item)
    print("\n")

def user_choice():
            try:
                user_attack_x = int(input("Enter X coorinate of the location you wanna fire: "))
                user_attack_y = int(input("Enter Y coorinate of the location you wanna fire: ")) 
                user_attack_y -= 1
                user_attack_x -= 1
            except ValueError:
                user_attack_y = -1
                user_attack_x = -1

            return [user_attack_y, user_attack_x]

def cpu_choice():
        cpu_attack_y = random.randint(0, 3)
        cpu_attack_x = random.randint(0, 3)

        return [cpu_attack_y, cpu_attack_x]

def main():
        user_grid = [["#", "#", "#", "#"] for y in range(4)]
        cpu_grid = [["#", "#", "#", "#"] for y in range(4)]
        
        user_points = 0
        cpu_points = 0

        user_grid = gengrid(user_grid)
        cpu_grid = gengrid(cpu_grid)

        cpu_killed = []
        user_killed = []

        play = True
        while play:
            # user's turn:
            system('clear')

            if cpu_points == 5:
                play = False
            
            print_grids(user_grid, cpu_grid, cpu_killed, user_killed, user_points, cpu_points)
                
            while True:
                user_attacks = user_choice()
                
                if [user_attacks[0], user_attacks[1]] in cpu_killed:
                    print("This was already hit! Please retry!")
                    continue
                else:
                    break
            
            if user_attacks[0] < 0 or user_attacks[0] > 4:
                if user_attacks[1] < 0 or user_attacks[1] > 4:
                    print("Please enter a number in range 1 to 4")
                    user_choice()

            result = attack(user_attacks[0], user_attacks[1], cpu_grid, cpu_killed, "You", user_points)

            if result[0] == True:
                cpu_killed.append([user_attacks[0], user_attacks[1]])

            user_points = result[1]

            input("Print ENTER to continue")

            #cpu turn:
            if user_points == 5:
                play = False

            while True:
                cpu_attacks = cpu_choice()
                
                if [cpu_attacks[0], cpu_attacks[1]] in user_killed:
                    continue
                else:
                    break
            
            result = attack(cpu_attacks[0], cpu_attacks[1], user_grid, cpu_killed, "Enemy", cpu_points)

            if result[0] == True:
                user_killed.append([cpu_attacks[0], cpu_attacks[1]])

            cpu_points = result[1]

            input("Print ENTER to continue")

        if user_points > cpu_points:
            print("YOU WIN!")
            print(">C")
            print("Your points:", user_points)
            print("Enemy points:", cpu_points)
        else:
            print("YOU LOSE!")
            print(":D")
            print("Your points:", user_points)
            print("Enemy points:", cpu_points)

if __name__ == "__main__":
    main()