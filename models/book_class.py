class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre  = genre
        self.checked_out = False

    def check_out(self):
        self.checked_out = True

    def check_in(self):
        self.checked_out = False