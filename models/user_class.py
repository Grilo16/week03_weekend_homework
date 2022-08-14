class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.userid = self.encript(self.name)
        self.books = []
        self.login_auth = False
        self.admin = False

    def encript(self, string):
        encription = {
            "a": "z",
            "b": "w",
            "c": "y",
            "d": "x",
            "e": "v",
            "f": "u",
            "g": "t",
            "h": "s",
            "i": "r",
            "j": "q",
            "k": "p",
            "l": "o",
            "m": "n",
            "n": "m",
            "o": "l",
            "p": "k",
            "q": "j",
            "r": "i",
            "s": "h",
            "t": "g",
            "u": "f",
            "v": "e",
            "x": "d",
            "y": "c",
            "w": "b",
            "z": "a",
        }
        clean_input = string.lower().replace(" ", "")

        output = ""
        for char in clean_input:
            output = output + encription[char]
        return output

    def rent_a_book(self, book):
        self.books.append(book)

    def return_a_book(self, book):
        self.books.remove(book)

    def login(self):
        self.login_auth = True

    def log_out(self):
        self.login_auth = False