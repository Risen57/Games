import random
import time
from os import system

def main():
    print("Welcome to Whack-a-Mole Game!")
    input("Press ENTER to begin")

    tries = 1
    hits = 0
    loss = 0
    while tries <= 10:
        system('clear')
        
        try:
            grid = [[7,8,9],
                    [4,5,6],
                    [1,2,3]]

            mole_x = random.randint(0, 2)
            mole_y = random.randint(0, 2)

            grid[mole_x][mole_y] = "0"

            print("Tries:", tries)
            for item in grid: print(item)

            initial = time.time()
            
            loc = int(input("Enter the number of the box of the mole\n: "))

            time_req = time.time() - initial

            if loc == 1:
                loc = [2, 0]
            elif loc == 2:
                loc = [2, 1]
            elif loc == 3:
                loc = [2, 2]
            elif loc == 4:
                loc = [1, 0]
            elif loc == 5:
                loc = [1, 1]
            elif loc == 6:
                loc = [1, 2]
            elif loc == 7:
                loc = [0, 0]
            elif loc == 8:
                loc = [0, 1]
            elif loc == 9:
                loc = [0, 2]
            else:
                tries += 1
                loss += 1
                print("You've missed")
                input("Hit ENTER to continue")
                continue


            if time_req > 1.3:
                tries += 1
                loss += 1
                print("You're Late!")
                input("Hit ENTER to continue")
            else:
                if loc[0] == mole_x and loc[1] == mole_y:
                    tries += 1
                    hits += 1
                    print("HIT!")
                else:
                    loss += 1
                    print("You've missed")
                input("Hit ENTER to continue")
        
        except ValueError:
            print("Please enter a num, this will not be counted as a try.")
            input("Hit ENTER to continue")

    print(f"You hit {hits} times")
    print(f"You lost {loss} times")

    if hits > loss:
        print("You WON!")
    elif hits == loss:
        print("It's a Tie!")
    else:
        print("You LOST!")

if __name__ == "__main__":
    main()