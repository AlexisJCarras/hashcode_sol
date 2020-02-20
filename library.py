class Library:


    def __init__(self, lib_num, time_scan, max_bookscanned):
        self.lib_id = lib_num #instance attributes here
        self.time_scan = time_scan
        self.max_bookscanned = max_bookscanned
        self.books = []


    def add_book(self, book):

       self.books.append(book)