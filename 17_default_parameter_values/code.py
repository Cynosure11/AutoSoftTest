def  add(x, y=8):
    print(x + y)


add(5)


# x is required parameter and y is optional


default_y = 3 # default parameter should be in the end, for example y


def add(x, y=default_y):
    sum = x + y
    print(sum)

add(33)


default_y = 4
add(2)
