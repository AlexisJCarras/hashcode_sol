class Library:


    def __init__(self, id,  num_of_books, signup_time, max_bookscanned):
        self.id = id
        self.signup_time = signup_time
        self.max_bookscanned = max_bookscanned
        self.num_of_books = num_of_books
        self.books = []


    def add_book(self, book):
       self.books.append(book)


    def __str__(self):
        strin = str(self.signup_time) + " " + str(self.max_bookscanned) + " " + str(self.num_of_books)
        return strin