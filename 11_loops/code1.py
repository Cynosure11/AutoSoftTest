friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")


grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)
for grade in grades:
    total += grade
# total / amount will give us average
# сумма всех цифр и деленная на 5
print(total / amount)


grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)
average = total / amount
print(average)
