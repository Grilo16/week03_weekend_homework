from models.book_class import Book


hp = Book("Harry potter", "jk rolling", "reality show")
lotr = Book("Lord of the rings", "its pronounced tolkieeeen", "family drama")


book_list = [hp, lotr]

def available_books(book_list):
    available_books = [book for book in book_list if book.checked_out == False]
    return available_books