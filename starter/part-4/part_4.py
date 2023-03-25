### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# def create_book():
#     title = input("What is the title of the book you wish to add? - ")
#     author = input("Who is the Author of this book? - ")
#     year = input("When was the book published? - ")
#     rating = input("What rating out of 5 would you give this book? - ")
#     pages = input("What is the page count of this book? - ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(create_book())


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def create_new_book():
#     title = input("What is the title of the book you wish to add? - ")
#     author = input("Who is the Author of this book? - ")
#     year = int(input("When was the book published? - "))
#     rating = float(input("What rating out of 5 would you give this book? - "))
#     pages = int(input("What is the page count of this book? - "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(create_new_book())



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# def create_new_book():
#     title = input("What is the title of the book you wish to add? - ")
#     author = input("Who is the Author of this book? - ")
#     try:
#         year = int(input("When was the book published? - "))
#     except:
#         year = int(input("Please type a number for the year? - "))
#     try:
#         rating = float(input("What rating out of 5 would you give this book? - "))
#     except:
#         rating = float(input("Please type a number between 0-5 for the rating? - "))
#     try: 
#         pages = int(input("What is the page count of this book? - "))
#     except:
#         pages = int(input("Please type a number for the amount of pages? - "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(create_new_book())





### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

books = []

while True:
    print("Main Menu:")
    print("1. Add a new book")
    print("2. See all books on the shelf")
    print("3. Search for a book by title")
    print("4. Exit")

    choice = input("Enter the number of you choice (1-4): ")

    if choice == "1":
        title = input("What is the title of the book you wish to add? - ")
        author = input("Who is the author of the book? - ")

        try:
            year = int(input("When was the book published? - "))
        except:
            year = int(input("Please type a number for the year? - "))
        try:
            rating = float(input("What rating out of 5 would you give this book? - "))
        except:
            rating = float(input("Please type a number between 0-5 for the rating? - "))
        try: 
            pages = int(input("What is the page count of this book? - "))
        except:
            pages = int(input("Please type a number for the amount of pages? - "))

        book = {
            "title": title,
            "author": author,
            "year": year,
            "rating": rating,
            "pages": pages
        }
        books.append(book)
        print("The book has been added to the shelf.")

    elif choice == "2":
        print("Books on the shelf:")
        for book in books:
            print(book["title"] + " by " + book["author"])

    elif choice == "3":
        search_title = input("Enter the title of the book: ")
        found_books = []

        for book in books:
            if book["title"].lower() == search_title.lower():
                found_books.append(book)

        if len(found_books) == 0:
            print("No books with that title were found.")
        else:
            print("Books with the title \"" + search_title + "\":")
            for book in found_books:
                print(book["title"] + " by " + book["author"])
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose an option by entering its number.")

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

## This code is Added Above.  Thanks 