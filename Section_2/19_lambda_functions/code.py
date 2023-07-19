# def add(x, y):
#     return x + y
#
#
# print(add(5, 7))


# it's not usable
print((lambda x, y: x + y)(5, 7))


# better option to use lambda
def double(x):
    return x * 2
sequence = [1, 3, 5, 9]
# doubled = [double(x) for x in sequence]
# lambda is vey confusing, instead of these needs to use map
doubled = [(lambda x: x * 2)(x) for x in sequence]
# doubled = list(map(double, sequence))
print(doubled)

'''
Checking
doubled = [(lambda x: x * 2)(x) f x in sequence]
x*2 in [1,3,5,9] = 1*2, 3*2, 5*2, 9*2
'''







