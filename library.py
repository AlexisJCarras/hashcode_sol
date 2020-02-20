class Library:


    def __init__(self, num_of_books, signup_process, max_bookscanned):
        self.signup_process = signup_process
        self.max_bookscanned = max_bookscanned
        self.num_of_books = num_of_books
        self.books = []


    def add_book(self, book):
       self.books.append(book)


    def __str__(self):
        strin = str(self.signup_process) + " " + str(self.max_bookscanned) + " " + str(self.num_of_books)
        return strin