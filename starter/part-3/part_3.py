my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_parser(book_dictionary):
    book_string = f"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor"
    return book_string

print(book_parser(my_book))



# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def get_title(book_dictionary):
    return my_book["title"]
print(my_book["title"])

def get_author(book_dictionary):
    return my_book["author"]
print(my_book["author"])

def get_year(book_dictionary):
    return my_book["year"]
print(my_book["year"])

def get_rating(book_dictionary):
    return my_book["rating"]
print(my_book["rating"])

def get_pages(book_dictionary):
    return my_book["pages"]
print(my_book["pages"])


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def get_average_rating(book_dictionary):
    total_rating = sum(book["rating"] for book in my_book)
    return total_rating / len(my_book)

def get_books_author(book_dictionary, author):
    return [book for book in my_book if book["author"] == author]

def best_rating(book_dictionary):
    return max(my_book, key=lambda book: book["rating"])