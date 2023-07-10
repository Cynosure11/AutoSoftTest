# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you've watched recently: ")
#
# if user_movie in movies_watched:
#     print(f" I've watched {user_movie} too")
# else:
#     print("I have not watched that yet.")

import random

number = random.randint(1, 3)
user_input = input("Enter 'y' if you would like to play. ").lower()

if user_input == "y":
    user_number = int(input("Guess our number, please: "))
    if user_number == number:
        print("You guessed correctly! \nGreat job!")
    elif abs(number - user_number) == 1:
        print(f"You were off by me. Correct number is {number}")
    else:
        print(f"Sorry. It is wrong. Correct number is {number}")
else:
    print("Have a good one. See you later!")