def hello():
    print("hello")
# hello()


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}")


print("Welcome to the age in seconds program")
# user_age_in_seconds()
print("Goodbye!")


friends = ["Rolf", "Bob"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    f = friends + [friend_name]
    print(f)
# add_friend()


friends = []


def add_friend():
    friends.append("Rolf") #append - добавить


add_friend()
add_friend()
add_friend()

print(friends) # ['Rolf']

