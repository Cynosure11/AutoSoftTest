def add(x, y):
    return x + y


result = add(5, 8)
print(result)


def divide(divided, divisor):
    if divisor != 0:
        return divided / divisor
    else:
        return "You fool"


result = divide(15, 3)
print(result)
result = divide(15, 0)
print(result)

