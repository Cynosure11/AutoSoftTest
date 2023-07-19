number = 7

while True:
    user_input = input("Would you like to play? (y/n) ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by me.")
    else:
        print("Sorry. It is wrong!")
