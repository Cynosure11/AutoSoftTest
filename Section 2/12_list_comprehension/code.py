numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]
# print(doubled)


friends = ["Rolf", "Sam", "Samantha", "Saurah", "Jennie"]
start_s = [friend for friend in friends if friend.startswith("S")]
print(start_s)
print(friends is start_s)
print("friends: ", id(friends), "start_s: ", id(start_s))
