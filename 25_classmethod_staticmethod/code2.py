class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, Book.TYPES[1], page_weight)


print(Book.TYPES)

book = Book.hardcover("Harry Potter", 1500)
# ook2 = Book("Tomskiy", "hardcover", 1200)
light = Book.paperback("Python 101", 600)
print(book)
# In this situation print(book) __repr__ will return
# print(book2.name, book2.book_type)
print(light)


