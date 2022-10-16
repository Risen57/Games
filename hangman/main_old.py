import random

with open("words.txt", "r") as f:
    file = f.readlines()
    words = [line.strip() for line in file]
    word = random.choice(words)
    word_sliced = [a for a in word]

health = 7
display = ["_" for a in word_sliced]
guesses_found = 0
word_len = len(word)

while True:
    print(health)
    print(display)
    print(word)
    print(word_len)
    guess = input("Enter a guess: ")

    if guess in word:
        if guess not in display:
            for a in word_sliced:
                print(a)
                if a == guess:
                    location = word_sliced.index(a)
                    display[location] = guess
                    guessess_found += 1
                else:
                    continue
        else:
            print("guess already used!")
    else:
        print("Oh no! Its not in the word!")
        health -= 1
