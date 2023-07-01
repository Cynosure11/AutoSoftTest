class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight


print(Book.TYPES)

book = Book("Harry Potter", "hardcover", 1500)
book2 = Book("Tomskiy", "hardcover", 1200)

print(book.name, book.weight)
print(book2.name, book2.book_type)


