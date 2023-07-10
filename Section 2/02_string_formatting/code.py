name = "Bob"
print(f"Hello, {name}")

name = "Rolf"
print(f"Hello, {name}")


name = "Abel"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_2 = greeting.format("Rolf")
print(with_name)
print(with_name_2)


longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)


