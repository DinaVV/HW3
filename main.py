# Task1

def count_vowels(text):
    if isinstance(text, str):
        num_vowels = 0
        for x in text:
            if x in "aeiouAEIOU":
                num_vowels += 1
        return num_vowels
    else:
        return 42


print(count_vowels("Learning Python is fun"))
print(count_vowels(1))


# Task2.1

def hamming(text1, text2):
    if len(text1) == len(text2):
        hamming_distance = 0
        for i in range(len(text1)):
            if text1[i] != text2[i]:
                hamming_distance += 1
        return hamming_distance
    else:
        return 0


print(hamming('LION', 'PITON'))
print(hamming('Moon', 'Loop'))


# Task 2.2

def hamming_distance(str1, str2):
    if len(str1) == len(str2):
        x = 0
        count = 0
        while x < len(str1):
            if str1[x] != str2[x]:
                count = count + 1
            x = x + 1
        return count
    else:
        return 0


str1 = "star"
str2 = "dust"

# function call
print(hamming_distance(str1, str2))



# Task3
class Vehicle:
    # constructor
    # is called when you create an instance of the class
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, ".format(self.color, self.fuel_type)


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return super().__str__() + "Doors: {0}".format(self.doors)
        # return "Color: {0}, Fuel Type: {1}, Doors: {2}".format(self.color, self.fuel_type, self.doors)


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return super().__str__() + "Passengers: {0}".format(self.passengers)
        # return "Color: {0}, Fuel Type: {1}, Passengers: {2}".format(self.color, self.fuel_type, self.passengers)


car = Car('green', 'benzin', 2)
print(car)

bus = Bus('blue', 'diesel', 27)
print(bus)


# Task4

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return "{0}, {1}".format(self.name, self.author)


book1 = Book('Lord of the Rings', 'John Tolkien')
print(book1)


# Task5

class BookShelf:
    def __init__(self):
        self.booklist = list()

    def add_book_list(self, books):
        for book in books:
            if isinstance(book, Book):
                self.booklist.append(book)

    def books_by_author(self, author):
        # using "list comprehension" to filter list for books of author
        return [book.name for book in self.booklist if book.author == author]

    def get_books(self):
        # using "list comprehension" return list of book-names
        return [book.name for book in self.booklist]

    def clear_shelf(self):
        self.booklist.clear()


booksList = list()
booksList.append(Book('Lord of the Rings', 'John Tolkien'))
booksList.append(Book('Harry Potter', 'Joanne Rowling'))
booksList.append(Book('The Hobbit', 'John Tolkien'))
booksList.append(Book('Master and Margarita', 'Mikhail Bulgakov'))
booksList.append(Book('Über Menschen', 'Juli Zeh'))

book_shelf1 = BookShelf();
book_shelf1.add_book_list(booksList)
books_from_tolkien = book_shelf1.books_by_author('John Tolkien')
print(books_from_tolkien)
print(book_shelf1.get_books())
book_shelf1.clear_shelf()
print(book_shelf1.get_books())
