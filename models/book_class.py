class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre  = genre
        self.checked_out = False

    def check_out(self, user_name):
        self.checked_out = user_name

    def check_in(self):
        self.checked_out = False