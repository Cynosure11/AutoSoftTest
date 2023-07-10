''' Magic methods: __str__ and __repr__ '''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self):
        return f"<Person {self.name}, {self.age}>"


aial = Person("Aial", 27)
print(aial)


''' Information 
    Of course, like with any other method, you can also call it manually like this:
     bob.__repr__() '''
