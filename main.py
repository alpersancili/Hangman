secret_key = "Parkour"
lives = 10
guess_string = ""

name = input("Name: ")
print(f"Hello {name} time to play hangman!")

while lives > 0:

    character_left = 0

    for character in secret_key:
        if character in guess_string:
            print(character)
        else:
            print("-")
            character_left += 1

    if character_left == 0:
        print("YOU WON!")
        break

    guess = input("Guess a word: ")
    guess_string+=guess

    if guess not in secret_key:
        lives -= 1
        print("Wrong!")
        print(f"You have {lives} left")
        if lives == 0:
            print("GAME OVER!")
            break

